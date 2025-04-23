import socket

class Server:
    def __init__(self):
        self.c = None


    def serverStart(self):
        HOST = '127.0.0.1'
        PORT = 65431
        socket.SOCK_STREAM

        print("*************************")
        print("*   Motor Calculating   *")
        print("*     S E R V E R       *")
        print("*************************")

        pythonserver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        pythonserver.bind((HOST, PORT))
        pythonserver.listen(10)
        c, addr = pythonserver.accept()
        self.c = c
        print("connection established")
        print(addr)
        return

    def Close(self):
        pythonserver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        pythonserver.close()
        print("Stop Server...")
        pass

    def SendData(self):
        g = open("MotorValuesString.txt", "r")
        MotorValuesString = str(g.read())
        print("MotorValuesString")
        self.c.send(MotorValuesString.encode())
        print(MotorValuesString)
        print("Data Sending...")
        pass

    def main(self):
        start = Server()
        start.serverStart()