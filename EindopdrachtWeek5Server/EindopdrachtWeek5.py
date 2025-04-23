from ServerStart import Server
from ServerInterface import Interface
import threading

def main():
    threading.Thread(target=Server().main).start()
    threading.Thread(target=Interface().main).start()
    pass


if __name__ == "__main__":
        main()