import socket

protocol = socket.SOCK_DGRAM 
sock = socket.socket(socket.AF_INET,protocol)
sock.settimeout(2)

address = ("localhost", 8881)

data = ""

if protocol == socket.SOCK_DGRAM:
    sock.sendto('1', address)
    data, server = sock.recvfrom(100000)
else:
    sock.connect_ex(address)
    data = sock.recv(100000)

print(data)