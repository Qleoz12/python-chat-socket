import socket, threading

def accept_client():
    while True:
        #accept    
        cli_sock, cli_add = ser_sock.accept()
        uname = cli_sock.recv(1024)
        CONNECTION_LIST.append((uname, cli_sock))
        print('%s is now connected' %uname)
        thread_client = threading.Thread(target = broadcast_usr, args=[uname, cli_sock])
        thread_client.start()

def broadcast_usr(uname, cli_sock):
    while True:
        try:
            data = cli_sock.recv(1024)
            if data:
                print( "{} spoke".format(uname))
                #logica para uno o para todos 
                #/u nombreusuarioobjetivo mensaje
                cadenadepalabras = data.split()
                if cadenadepalabras[0].lower() == b'/u':
                    data=str(data).replace(cadenadepalabras[0].decode("utf-8") ,'')
                    data=str(data).replace(cadenadepalabras[1].decode("utf-8") ,'')
                    b_usr_specific(cli_sock, uname,  bytes(data, 'utf-8'),cadenadepalabras[1])
                else: 
                    b_usr(cli_sock, uname, data)

        except Exception as x:
            print(x.message)
            break
#metodo para enviar mensaje a todos los usuarios
def b_usr(cs_sock, sen_name, msg):
    for client in CONNECTION_LIST:
        if client[1] != cs_sock:
            client[1].send(sen_name)
            client[1].send(msg)

#metodo para enviar mensaje a usuario especifico
def b_usr_specific(cs_sock, sen_name, msg, usertarget):
    for client in CONNECTION_LIST:
        if client[1] != cs_sock and client[0] == usertarget:
            client[1].send(sen_name)
            client[1].send(msg)


if __name__ == "__main__":    
    CONNECTION_LIST = []

    # socket
    ser_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # bind
    HOST = 'localhost'
    PORT = 5023
    ser_sock.bind((HOST, PORT))

    # listen    
    ser_sock.listen(1)
    print('Chat server started on port : ' + str(PORT))

    thread_ac = threading.Thread(target = accept_client)
    thread_ac.start()

    #thread_bs = threading.Thread(target = broadcast_usr)
    #thread_bs.start()