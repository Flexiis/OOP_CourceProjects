from ClientInterface import Interface
import socket


class Client:
    global simulate
    def __init__(self):
        self.interface = Interface
        pass

    def clientStart(self):
        print("*************************")
        print("*   Motor Calculating   *")
        print("*     C L I E N T       *")
        print("*************************")
        HOST = '127.0.0.1'
        PORT = 65431
        global clientSocket
        clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientSocket.connect((HOST, PORT))
        print("connection done... %s" % (str(clientSocket)))
        self.MotorValuesString = []
        print("Recieving Data...")
        self.MotorValuesString = clientSocket.recv(1024).decode()
        print(self.MotorValuesString)
        self.writetxt()
        clientSocket.close()

    def writetxt(self):
        f = open("MotorValuesStringClient.txt", "w")
        f.write("{}".format(str(self.MotorValuesString)))

    def main(self):
        start = Client()
        start.clientStart()