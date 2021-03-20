# ----- sender.py ------

#!/usr/bin/env python

from socket import *
import sys


class Sender:

    def __init__(self): 
        self.enviar = False
        self.file_name = ""
        self.s=None
        self.addr=None
        self.buf=None

    def abrirsocket(self):
        self.s = socket(AF_INET,SOCK_DGRAM)
        host = "127.0.0.1"
        port = 9999
        self.buf = 1024
        self.addr = (host,port)

    def enviarArchivo(self):
        self.enviar=True
        self.s.sendto(self.file_name.encode(),self.addr)

        f=open(self.file_name,"rb")
        data = f.read(self.buf)
        while (self.enviar):
            if(self.s.sendto(data,self.addr)):
                print ("sending ...")
                data = f.read(self.buf)
        self.enviar=False
        f.close()
    
    def cerrarSocket(self):
        self.s.close()

    def file(self,file_name):
        self.file_name=file_name