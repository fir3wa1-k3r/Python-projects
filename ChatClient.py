import socket

host = str(raw_input("Enter the host to connect:"))
port = int(raw_input("Enter the port to connect:"))

sock = socket.socket()
sock.connect((host,port))
data1 = sock.recv(1024)
print data1
while True:
	msg = str(raw_input("Client>"))
	sock.send(msg)
	data = sock.recv(1024)
	print "Server>"+data
sock.close()
