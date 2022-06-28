import socket
from timeit import default_timer as timer
from datetime import timedelta
import random

N = 100000
bits = random.getrandbits(N)

protocol = socket.SOCK_DGRAM 
sock = socket.socket(socket.AF_INET,protocol)


port = 8881
sock.bind(("localhost", port))

if protocol == socket.SOCK_STREAM:
    sock.listen(1)

try:
    while True:
        if protocol == socket.SOCK_DGRAM:
            start = timer()
           
            message, address = sock.recvfrom(1) 
            sock.sendto(str(bits), address)

            end = timer()
            print(timedelta(seconds=end-start))
        else:
            connection, address = sock.accept()
            start = timer()
            
            connection.send(str(bits))
        
            end = timer()
            print(timedelta(seconds=end-start))
            connection.close()
finally:
    sock.close(  )
