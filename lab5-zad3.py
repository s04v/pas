import socket

sockUDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sockUDP.settimeout(2)

port = 0

while port < 64:
    try:
        sockUDP.connect_ex(("127.0.0.1", int(str(port) + "666")))
        sockUDP.send("PING")
        data = sockUDP.recv(4).decode( "UTF-8" )
        if data == "PONG":
            print(data)
    except:
        print("Connection failed")
    
    port = port + 1

sockUDP.close()

sockTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sockTCP.connect(("127.0.0.1", 2913))
data = sockTCP.recv(128).decode( "UTF-8" )
print(data)

sockTCP.close()