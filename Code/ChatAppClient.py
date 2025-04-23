import socket
print("*************************")
print("*   C H A T     A P P   *")
print("*     C L I E N T       *")
print("*************************")
HOST = '127.0.0.1'
PORT = 65432
dataToSend = ()
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((HOST, PORT))
print("connection done... %s" % (str(clientSocket)))
while(not("quit" in dataToSend)):
    dataToSend = input("input data ")
    print("sending data...")
    clientSocket.send(dataToSend.encode('utf-8'))
clientSocket.close()