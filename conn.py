import socket
sock = socket.socket()
host = '10.10.10.48'
port = 80
sock.connect((host,port))
str = "GET / HTTP/1.1\r\nHOST: 10.10.15.163\r\n\r\n"
sock.send(str)
data = sock.recv(1024)
print(data)
