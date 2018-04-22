from scapy.all import *
from itertools import permutations

fin = "fin"
port_list = list()
#method to knock the ports
def sendpackets(ip,port):
    ip1 = IP(src="127.0.0.1",dst=ip)
    SYN = TCP(sport=9999,dport=port,flags="S",seq=13579)
    send(ip1/SYN)

#initializing the vectors
def main():
    ip = input("Enter the ip address:")
    while True:
        num = input("Enter the ports to be knocked and type fin if you are done:")
        if num == fin:
            break
        elif int(num) > 0 and int(num) < 65535:
            port_list.append(int(num))
        else:
            print("Invalid port!!! Try again")
    
    for ports in permutations(port_list):
        for port in ports:
            sendpackets(ip,port)
main()
