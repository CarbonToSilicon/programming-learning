import socket
import ssl
# HOST = 'data.pr4e.org'
# PORT = 80

# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# mysock.connect((HOST, PORT))

# cmd = (
#     f"GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n"
# ).encode()

# mysock.sendall(cmd)

# while True:
#     data = mysock.recv(1000)
#     if not data:
#         break
#     print(data.decode("utf-8"))

# mysock.close()




HOST = "www.py4e.com"
PORT = 443

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
context = ssl.create_default_context()
secure_sock = context.wrap_socket(mysock, server_hostname = HOST)
secure_sock.connect((HOST, PORT))

cmd = (
    f"GET /lectures3/Pythonlearn-12-HTTP.pdf HTTP/1.1\r\n"
    f"Host: {HOST}\r\n"
    f"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)\r\n"
    f"Connection: Close\r\n\r\n"
).encode()
secure_sock.sendall(cmd)

pdf = b""
while True:
    data = secure_sock.recv(8192)
    if not data:
        break
    pdf += data

secure_sock.close()

header_end = pdf.find(b"\r\n\r\n")
print(pdf[:header_end].decode())
pdf_data = pdf[header_end + 4:]

with open("Pythonlearn-12-HTTP.pdf", "wb") as f:
    f.write(pdf_data)

print("\nPDF downloaded and saved successfully!\n")