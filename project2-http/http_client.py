import socket

host = "www.google.com"
port = 80

print("Đang kết nối...")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
print("Đã kết nối thành công!")

request = (
    "GET / HTTP/1.1\r\n"
    "Host: www.google.com\r\n"
    "User-Agent: SocketLab/1.0\r\n"
    "Connection: close\r\n"
    "\r\n"
)
s.sendall(request.encode())
print("Đã gửi request!")

response = b""
while True:
    chunk = s.recv(4096)
    print(f"Nhận được {len(chunk)} bytes")
    if not chunk:
        break
    response += chunk

print("--- RESPONSE ---")
print(response.decode(errors="replace"))
s.close()