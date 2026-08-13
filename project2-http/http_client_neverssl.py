import socket
import sys

# Cấu hình stdout để hỗ trợ in các ký tự UTF-8 trên Windows Console
sys.stdout.reconfigure(encoding='utf-8')

host = "neverssl.com"
port = 80
# 1. Create a TCP (stream) socket over IPv4
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 2. Open the connection (this triggers the TCP 3-way handshake)
s.connect((host, port))
# # 3. Build a minimal HTTP/1.1 GET request
# # Lines end in CRLF; a blank line marks the end of the headers.
# request = (
#     "GET / HTTP/1.1\r\n"
#     "Host: neverssl.com\r\n"
#     "User-Agent: SocketLab/1.0\r\n"
#     "Connection: close\r\n"
#     "\r\n"
# )
# # 4. Send the request bytes
# s.sendall(request.encode())
# # 5. Read the whole response until the server closes the connection
# response = b""
# while True:
#     chunk = s.recv(4096)
#     if not chunk:
#         break
#     response += chunk
# # 6. Print the response and close the socket
# print(response.decode(errors="replace"))
# s.close()
