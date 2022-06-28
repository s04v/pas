import socket
import random

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 2912))
sock.listen(1)
c, addr = sock.accept()

while 1:
    data = conn.recv(64).decode( "UTF-8" )
    num = random.randrange(1, 10)
    if not data:
        break
        
    if type(data) != int:
        conn.send("You must send a number!")

    if num < data:
        conn.send("Your number is greater")

    if num > data:
        conn.send("Your number is less")
    
    if num == data:
        conn.send("You guessed")
        break

conn.close()