import ssl
import socket

HOST = "www.google.com"
PORT = 443

context = ssl.create_default_context()
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as raw_socket:
	print(f"Connecting to {HOST} over raw TCP . . .")
	raw_socket.connect((HOST, PORT))
	
	with context.wrap_socket(raw_socket, server_hostname = HOST) as secure_socket:
		print("TLS handshake complete. Connection is now secure.")
			
		http_request = (
			f"GET / HTTP/1.1\r\n"
			f"Host: {HOST}\r\n"
			f"User-Agent: LowLevelPythonClient/1.0\r\n"
			f"Connection: close\r\n\r\n"
		)
		secure_socket.sendall(http_request.encode("utf-8"))
		print(f"HTTP Request sent successful.\n" + "-" * 90)
		response_bytes = b""
		while True:
			chunk = secure_socket.recv(4096)
			if not chunk:
				break
			response_bytes += chunk
			#print(response_bytes.decode, end=' ')
response_text = response_bytes.decode("utf-8")
print(response_text)