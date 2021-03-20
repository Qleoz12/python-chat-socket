# ----- receiver.py -----

#!/usr/bin/env python

from socket import *
import sys
import select
import threading

class Receiver(threading.Thread):
    
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.s = None
        self.addr=None
        self.leer=True
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
      print ("Starting " + self.name)
      print ("Exiting " + self.name)
      self.abrirsocket()

    def abrirsocket(self):
        host="0.0.0.0"
        port = 9999
        self.s = socket(AF_INET,SOCK_DGRAM)
        self.s.bind((host,port))

        self.addr = (host,port)
        buf=1024

        data,self.addr = self.s.recvfrom(buf)
        print ("Received File:",data.strip())
        f = open('archivorecibido.txt','wb')

        data,self.addr = self.s.recvfrom(buf)
        try:
            while(self.leer):
                f.write(data)
                self.s.settimeout(2)
                data,self.addr = self.s.recvfrom(buf)
        except timeout:
            f.close()
            self.s.close()
            print ("File Downloaded")


    def apagar(self):
        self.leer=false

