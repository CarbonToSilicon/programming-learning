import socket
import os

# '0.0.0.0' allows the server to listen on all available network cards
HOST = '0.0.0.0'  
PORT = 65432
BUFFER_SIZE = 4096

def send_string(conn, text):
    """Helper function to cleanly pack and send text data over the socket."""
    encoded = text.encode('utf-8')
    # Prefixes data with a fixed 8-digit size header (e.g., 00000124 bytes)
    conn.sendall(f"{len(encoded):08d}".encode('utf-8'))
    conn.sendall(encoded)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    # Allow the socket to reuse the address instantly if restarted
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print(f"=== Interactive File Server Online ===")
    print(f"Listening for connections on port {PORT}...")

    while True:
        conn, addr = server_socket.accept()
        print(f"\n[CONNECTED] Client joined from: {addr}")
        
        # Start each new connection in the server's current folder
        current_dir = os.getcwd()
        
        try:
            while True:
                # Read the incoming string command from the client
                request = conn.recv(BUFFER_SIZE).decode('utf-8').strip()
                if not request:
                    break
                
                # --- COMMAND 1: LIST CONTENTS ---
                if request == "LIST":
                    try:
                        items = os.listdir(current_dir)
                        formatted_items = []
                        for item in items:
                            path = os.path.join(current_dir, item)
                            if os.path.isdir(path):
                                formatted_items.append(f"[DIR]  {item}")
                            else:
                                formatted_items.append(f"[FILE] {item}")
                        
                        response = "\n".join(formatted_items) if formatted_items else "(Empty Directory)"
                        send_string(conn, response)
                    except Exception as e:
                        send_string(conn, f"Error reading directory: {e}")

                # --- COMMAND 2: CHANGE DIRECTORY ---
                elif request.startswith("CD "):
                    target_dir = request[3:].strip()
                    try:
                        new_path = os.path.abspath(os.path.join(current_dir, target_dir))
                        if os.path.isdir(new_path):
                            current_dir = new_path
                            send_string(conn, f"SUCCESS:{current_dir}")
                        else:
                            send_string(conn, "ERROR:Not a valid directory.")
                    except Exception as e:
                        send_string(conn, f"ERROR:{e}")

                # --- COMMAND 3: DOWNLOAD FILE ---
                elif request.startswith("DOWNLOAD "):
                    filename = request[9:].strip()
                    file_path = os.path.join(current_dir, filename)
                    
                    if os.path.exists(file_path) and os.path.isfile(file_path):
                        conn.sendall(b"EXISTS")
                        print(f"[SENDING] Streaming '{filename}'...")
                        with open(file_path, 'rb') as f:
                            while True:
                                bytes_read = f.read(BUFFER_SIZE)
                                if not bytes_read:
                                    break
                                conn.sendall(bytes_read)
                        print("[SUCCESS] Transfer finished successfully.")
                        break  # Connection resets after a file streams to ensure file close
                    else:
                        conn.sendall(b"NOT_FOUND")
                
                elif request == "EXIT":
                    break
                    
        except Exception as e:
            print(f"[SYSTEM EXCEPTION] Error: {e}")
        finally:
            conn.close()
            print("[DISCONNECTED] Client connection closed.")