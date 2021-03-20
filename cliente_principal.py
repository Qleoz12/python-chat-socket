from udp.receiver import  Receiver
from udp.sender import Sender



def main():
    print("Iniciando Chat!")
    #1 hilo
    receiver = Receiver(1, "Thread-1", 1)
    receiver.start()

    #2 hilo
    sender = Sender()
    sender.abrirsocket()
    sender.file("filename.txt")
    sender.enviarArchivo()

    receiver.apagar()

if __name__ == "__main__":
    main()

