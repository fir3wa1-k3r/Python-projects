import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM);
while True:
	s.connect(('127.0.0.1',80))
	add,data = s.recv(1024)
	print(add)
	
	
