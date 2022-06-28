import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect_ex(("12.182.24.27", 2912))
    
number = input()

sock.send(number)

response = sock.recv(4)

print(response)