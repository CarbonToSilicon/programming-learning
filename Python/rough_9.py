# rawanna_numbers =[]
# with open("rawanna_no.csv", "r") as data_file:
#     for f in data_file:
#         f = f.rstrip()
#         rawanna_numbers.append(f)
# print(rawanna_numbers)

######################################################################################

# import socket

# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('data.pr4e.org', 80))
# cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
# mysock.send(cmd)

# while True:
#     data = mysock.recv(512)
#     if len(data) < 1:
#         break
#     print(data.decode(),end='')

# mysock.close()

# import socket
# import time

# HOST = 'data.pr4e.org'
# PORT = 80
# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect((HOST, PORT))
# mysock.sendall(b'GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n')
# count = 0
# picture = b""

# while True:
#     data = mysock.recv(5120)
#     if len(data) < 1: break
#     time.sleep(0.25)
#     count = count + len(data)
#     print(len(data), count)
#     picture = picture + data
# print("\n\n\n")
# mysock.close()

# # Look for the end of the header (2 CRLF)
# pos = picture.find(b"\r\n\r\n")
# print('Header length', pos)
# print(picture[:pos].decode())

# # Skip past the header and save the picture data
# picture = picture[pos+4:]
# fhand = open("stuff.jpg", "wb")
# fhand.write(picture)
# fhand.close()


# import socket
# import ssl
# import json 

# HOST = 'api.github.com'
# PORT = 443 

# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# context = ssl.create_default_context()
# secure_sock = context.wrap_socket(mysock, server_hostname=HOST)
# secure_sock.connect((HOST, PORT))

# cmd = (
#     f'GET /users/octocat HTTP/1.1\r\n'
#     f'Host: {HOST}\r\n'
#     f'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)\r\n'
#     f'Connection: close\r\n\r\n'
# ).encode()

# secure_sock.send(cmd)

# # 1. Catch all data from the socket stream
# raw_response = ""
# while True:
#     data = secure_sock.recv(512)
#     if len(data) < 1: 
#         break
#     raw_response += data.decode()

# secure_sock.close()

# # 2. Split headers away from the payload body
# parts = raw_response.split("\r\n\r\n")
# meta_data = parts[0]
# json_body = parts[1]

# # 3. PRINT THE RAW JSON CONTENT FIRST
# print("\n\n\n"+meta_data)
# print("\n=== 1. RAW UNFILTERED JSON FROM SERVER ===")
# print(json_body)
# print("==========================================\n")

# # 4. Convert the JSON string into a Python Dictionary
# data_dict = json.loads(json_body)

# # 5. Print EVERY key and value dynamically as clean text
# print("=== 2. ALL PARSED AND FILTERED CONTENT ===")
# for key, value in data_dict.items():
#     clean_key = key.replace('_', ' ').title()
#     print(f"{clean_key:<25}: {value}")
# print("==========================================")



# import smtplib

# SENDER_EMAIL = "bajrangcrasher@gamil.com"
# SENDER_PASSWORD = "ubmjpervdnyfnoah".replace(" ", "").strip()

# print("Testing credentials...")
# with smtplib.SMTP("smtp.gmail.com", 587) as server:
#     server.ehlo()
#     server.starttls()
#     server.ehlo()
#     server.login(SENDER_EMAIL, SENDER_PASSWORD)
#     print("🎉 SUCCESS! Google accepted the password!")

# import smtplib

# # 1. Type your exact email address here
# SENDER_EMAIL = "bajrangcrasher@gmail.com"

# # 2. PASTE THE 16-LETTER CODE INSIDE THE QUOTES (Keep it lowercase, no spaces!)
# RAW_PASSWORD = "ubmjpervdnyfnoah"

# # This line forcefully strips any spaces, line breaks, or accidental tabs
# SENDER_PASSWORD = "".join(RAW_PASSWORD.split()).strip()

# print("--- DEBUGGING INFO ---")
# print(f"Connecting as: {SENDER_EMAIL}")
# print(f"Password character count: {len(SENDER_PASSWORD)} (Should be exactly 16)")
# print("----------------------\n")

# print("Connecting to the mail server on port 587...")
# try:
#     with smtplib.SMTP("smtp.gmail.com", 587, timeout=10) as server:
#         server.ehlo()
#         print("Upgrading connection to secure TLS encryption...")
#         server.starttls()
#         server.ehlo()
        
#         print("Logging in...")
#         server.login(SENDER_EMAIL, SENDER_PASSWORD)
#         print("🎉 SUCCESS! Google accepted the app password!")
        
# except smtplib.SMTPAuthenticationError:
#     print("\n❌ Google still rejected it. Double-check:")
#     print("1. Did you accidentally leave a space?")
#     print("2. Is your SENDER_EMAIL typed exactly right?")
# except Exception as e:
#     print(f"\n❌ Network error: {e}")













# import socket

# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# mysock.connect(("data.pr4e.org", 80))

# cmd = (f"GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n").encode()

# mysock.send(cmd)

# while True:
#     data = mysock.recv(1024)
#     if not data:
#         break
#     print(data.decode("utf-8"))

# mysock.close()












import socket
import ssl

HOST = "raw.githubusercontent.com"
PORT = 443

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
context = ssl._create_unverified_context()
secure_sock = context.wrap_socket(mysock, server_hostname=HOST)

try:
    secure_sock.connect((HOST, PORT))
except socket.gaierror:
    secure_sock.connect(("185.199.108.133", PORT))

# FIX: Stripped unnecessary header attributes and strictly separated lines
# Every single line must end exactly with \r\n without hidden f-string indentation spaces.
cmd = (
    "GET /vinta/awesome-python/master/website/static/og-image.png HTTP/1.1\r\n"
    f"Host: {HOST}\r\n"
    "User-Agent: Mozilla/5.0\r\n"
    "Connection: close\r\n\r\n"
).encode("utf-8")

secure_sock.sendall(cmd)

info = b""
while True:
    data = secure_sock.recv(8192)
    if not data:
        break
    info += data

secure_sock.close()

boundary = info.find(b"\r\n\r\n")
if boundary != -1:
    print("--- HTTP HEADERS ---")
    print(info[:boundary].decode("utf-8"))
    print("--------------------\n")
    
    image_bytes = info[boundary + 4:]
    
    # Extra safety check to see if we finally received the PNG file data
    if image_bytes.startswith(b"\x89PNG"):
        with open("og-image.png", "wb") as f:
            f.write(image_bytes)
        print(f"Success! Saved {len(image_bytes)} bytes to og-image.png")
    else:
        print("Error: The response metadata cleared, but the payload is not a PNG file image.")
else:
    print("Image data not found!")


#https://github.com/vinta/awesome-python/blob/master/website/static/og-image.png
#print(info.decode("utf-8")[:10000])

# from bs4 import BeautifulSoup

# # ... your existing socket code to get 'info' ...

# html_content = info.decode('utf-8')

# # Separate the HTTP headers from the actual HTML body
# html_body = html_content.split("\r\n\r\n", 1)[1]

# # Parse and extract text
# soup = BeautifulSoup(html_body, 'html.parser')
# print(soup.get_text())
