#Main class for server.
#Owner :- Neel

from socket import *
from threading import Thread

import Global as G #global variables
import FileRead as F #reading file module
import UserAuth as U #Authentication Module
import Options as O #Options Module

class Server(Thread):
    def __init__(self,client):
        Thread.__init__(client)
        self.__client = client

    def run(self):
        Welc_mess = "Welcome"
        Ack = "Recieved"
        Log_count = 0
        self.__client.send(Welc_mess.encode("utf-8"))
        while True:
            print("Waiting for message....")
            U_Nm = self.__client.recv(1024).decode("utf-8") #recieve username
            self.__client.send(Ack.encode("utf-8"))
            Pswd = self.__client.recv(1024).decode("utf-8") #recieve password
            Tst = [str(U_Nm), str(Pswd)]
            while Log_count <3:
                if U.UserAuth(Tst) == True:
                    self.__client.send("Success".encode("utf-8"))
                    opt = int(self.__client.recv(1024).decode("utf-8")) #recieve Option
                    self.__client.send(Ack.encode("utf-8"))
                    while opt != 6:                    
                        if opt == '1':
                            Org_nme = self.__client.recv(1024).decode("utf-8") #recieve org name
                            Output1 = O.Option1(Org_nme)
                            self.__client.send(Output1.encode("utf-8"))
                        else if opt == '2':
                            Output2 = O.Option2()
                            self.__client.send(Output2.encode("utf-8"))
                        else if opt == '3':
                            choice = int(self.__client.recv(1024).decode("utf-8"))
                            Output3 = O.Option3(choice)
                            self.__client.send(Output3.encode("utf-8"))
                        else if opt == '4':
                            op_cnt = 0
                            for op_cnt in range(3):
                                Org-nme = self.__client.recv(1024).decode("utf-8")
                                Dom-nme = self.__client.recv(1024).decode("utf-8")
                                IP = self.__client.recv(1024).decode("utf-8")
                                Minute = self.__client.recv(1024).decode("utf-8")
                                Tmp = [str(Org-nme), str(Dom-nme), str(IP), str(Minute)]
                                Output4 = O.Option4(Tmp)
                                if Output4 == "Success":
                                    self.__client.send(Output4.encode("utf-8"))
                                    break
                                else :
                                    self.__client.send("Exist".encode("utf-8"))
                                    op_cnt ++
                            else :
                                self.__client.send("Error".encode("utf-8"))
                                self.__client.close()
                                    
                        else if opt == '5':
                             op_cnt = 0
                            for op_cnt in range(3):
                                OrgNme = self.__client.recv(1024).decode("utf-8") #recieve org name
                                Output5 = O.Option5(OrgNme)
                                if Output5 == "Success":
                                    self.__client.send(Output5.encode("utf-8"))
                                    break
                                else :
                                    self.__client.send("NotExist".encode("utf-8"))
                                    op_cnt ++
                            else :
                                self.__client.send("Error".encode("utf-8"))
                                self.__client.close()
                        
                        else :
                            self.__client.send("Invalid".encode("utf-8"))
                    else if opt == 6:
                        self.__client.send("Good Bye".encode("utf-8"))
                        self.__client.close()
# write reamining code here
                    break
                else :
                    self.__client.send("Failure".encode("utf-8"))
                    Log_count ++
            else:
                self.__client.send("Exceeded".encode("utf-8"))
                self.__client.close()
                



def main():
    Fl_Usr = open("Usr.txt", "r") #User File
    F.FileRead(Fl_Usr, G.L_User)
    Fl_Org = open("Org.txt", "r")
    F.FileRead(Fl_Org, G.L_Org)
    
    print(G.L_Org)
    print(G.L_User)

    serName = gethostname()
    serPort = 5000

    serSock = socket(AF_INET4,SOCK_STREAM)
    serSock.bind((serName, serPort))
    serSock.listen()


    print("HI from server \n\n")
    print(serName + "  "+ str(serPort))
    while True :
        client, Address = serSock.accept()
        print("connected from :  ", Address)
        cl_hndle = Server(client)
        cl_hndle.start()

    Fl_Usr.close()
    Fl_Org.close()
        
    
