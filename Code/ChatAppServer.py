import socket
HOST = '127.0.0.1'
PORT = 65432
socket.SOCK_STREAM


print("*************************")
print("*   C H A T     A P P   *")
print("*     S E R V E R       *")
print("*************************")

pythonserver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
pythonserver.bind((HOST, PORT))
pythonserver.listen(10)
c, addr = pythonserver.accept()
print("connection established")
print(addr)
data = ()
while(not ("quit" in data)):
    data = c.recv(1024).decode('utf-8')
    print(data)

pythonserver.close()
