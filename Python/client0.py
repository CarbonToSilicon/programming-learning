import socket
import os

# This matches the permanent Static IP you just configured on the Server PC
SERVER_IP = '192.168.31.222' 
PORT = 65432
BUFFER_SIZE = 4096

def receive_string(sock):
    """Helper function to read dynamic length data from the server."""
    # Read the 8-byte length header first
    data_len_bytes = sock.recv(8)
    if not data_len_bytes:
        return ""
    data_len = int(data_len_bytes.decode('utf-8'))
    
    # Keep assembling data packets until we hit the total character length
    chunks = []
    bytes_recvd = 0
    while bytes_recvd < data_len:
        chunk = sock.recv(min(data_len - bytes_recvd, BUFFER_SIZE))
        if not chunk:
            break
        chunks.append(chunk)
        bytes_recvd += len(chunk)
    return b"".join(chunks).decode('utf-8')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    try:
        print(f"Connecting to server at {SERVER_IP}:{PORT}...")
        client_socket.connect((SERVER_IP, PORT))
        print("Connected successfully!")
        
        while True:
            print("\n" + "="*50)
            print(" REMOTE FILE NAVIGATOR")
            print("="*50)
            print("[1] View current directory contents (LIST)")
            print("[2] Enter into a folder (CD)")
            print("[3] Go back to parent folder (CD ..)")
            print("[4] Download a specific file")
            print("[5] Exit")
            print("="*50)
            
            choice = input("Select an option (1-5): ").strip()
            
            if choice == "1":
                client_socket.sendall(b"LIST")
                contents = receive_string(client_socket)
                print("\n--- REMOTE SERVER DIRECTORY ---")
                print(contents)
                
            elif choice == "2":
                folder_name = input("Enter folder name to open: ").strip()
                client_socket.sendall(f"CD {folder_name}".encode('utf-8'))
                result = receive_string(client_socket)
                if result.startswith("SUCCESS:"):
                    print(f"\n[MOVED] Remote path is now: {result[8:]}")
                else:
                    print(f"\n[FAILED] {result}")
                    
            elif choice == "3":
                client_socket.sendall(b"CD ..")
                result = receive_string(client_socket)
                if result.startswith("SUCCESS:"):
                    print(f"\n[MOVED UP] Remote path is now: {result[8:]}")
                    
            elif choice == "4":
                file_name = input("Enter file name to download: ").strip()
                client_socket.sendall(f"DOWNLOAD {file_name}".encode('utf-8'))
                
                status = client_socket.recv(9).decode('utf-8')
                if status == "EXISTS":
                    print(f"[FOUND] Downloading '{file_name}'...")
                    # Saves the downloaded file in the client's current folder
                    output_name = "downloaded_" + os.path.basename(file_name)
                    
                    with open(output_name, 'wb') as f:
                        while True:
                            bytes_in = client_socket.recv(BUFFER_SIZE)
                            if not bytes_in:
                                break
                            f.write(bytes_in)
                    print(f"[SUCCESS] Download completed! Saved locally as: '{output_name}'")
                    print("Socket closed safely. Restart the script if you want to pull another file!")
                    break
                else:
                    print("[ERROR] That file does not exist in the server's active folder.")
                    
            elif choice == "5":
                client_socket.sendall(b"EXIT")
                print("Exiting application.")
                break
            else:
                print("Invalid input option. Please choose 1-5.")
                
    except ConnectionRefusedError:
        print("[FAILURE] Could not reach the server application. Is server.py running on the server PC?")
    except Exception as e:
        print(f"[ERROR] Connection lost: {e}")