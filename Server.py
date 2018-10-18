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
        Thread.__init__(self)
        self.client = client

    def run(self):
        Welc_mess = "Welcome"
        Ack = "Recieved"
        Log_count = 0
        print(self.client.recv(1024).decode("utf-8"))
        self.client.send(Welc_mess.encode("utf-8"))
        while True:
            print("Waiting for message....")
            U_Nm = self.client.recv(1024).decode("utf-8")
            print(U_Nm)#recieve username
            self.client.send(Ack.encode("utf-8"))
            Pswd = self.client.recv(1024).decode("utf-8")
            #print(Pswd)#recieve password
            Tst = [str(U_Nm), str(Pswd)]
            while Log_count < 3:
                if U.UserAuth(Tst) == True:
                    self.client.send("Success".encode("utf-8"))
                    opt = int(self.client.recv(1024).decode("utf-8")) #recieve Option
                    self.client.send(Ack.encode("utf-8"))
                    while opt != 6:                    
                        if opt == '1':
                            Org_nme = self.client.recv(1024).decode("utf-8") #recieve org name
                            Output1 = O.Option1(Org_nme)
                            self.client.send(Output1.encode("utf-8"))
                        elif opt == '2':
                            Output2 = O.Option2()
                            self.client.send(Output2.encode("utf-8"))
                        elif opt == '3':
                            choice = int(self.client.recv(1024).decode("utf-8"))
                            Output3 = O.Option3(choice)
                            self.client.send(Output3.encode("utf-8"))
                        elif opt == '4':
                            op_cnt = 0
                            for op_cnt in range(3):
                                Org_nme = self.client.recv(1024).decode("utf-8")
                                Dom_nme = self.client.recv(1024).decode("utf-8")
                                IP = self.client.recv(1024).decode("utf-8")
                                Minute = self.client.recv(1024).decode("utf-8")
                                Tmp = [Org_nme, Dom_nme, IP, Minute]
                                Output4 = O.Option4(Tmp)
                                if Output4 == "Success":
                                    self.client.send(Output4.encode("utf-8"))
                                    break
                                else :
                                    self.client.send("Exist".encode("utf-8"))
                                    op_cnt = op_cnt + 1
                            else :
                                self.client.send("Error".encode("utf-8"))
                                self.client.close()
                                    
                        elif opt == '5':
                            op_cnt = 0
                            for op_cnt in range(3):
                                OrgNme = self.client.recv(1024).decode("utf-8") #recieve org name
                                Output5 = O.Option5(OrgNme)
                                if Output5 == "Success":
                                    self.client.send(Output5.encode("utf-8"))
                                    break
                                else :
                                    self.client.send("NotExist".encode("utf-8"))
                                    op_cnt = op_cnt + 1
                            else :
                                self.client.send("Error".encode("utf-8"))
                                self.client.close()
                                G.L_User.append(G.L_Used)
                                G.L_Used = []
                        
                         
                    else:
                        if opt == 6:
                            self.client.send("Good Bye".encode("utf-8"))
                            self.client.close()
                            G.L_User.append(G.L_Used)
                            G.L_Used = []
# write reamining code here
                    break
                else :
                    self.client.send("Failure".encode("utf-8"))
                    Log_count = Log_count + 1
            else:
                self.client.send("Exceeded".encode("utf-8"))
                self.client.close()
                G.L_User.append(G.L_Used)
                G.L_Used = []
                



def main():
    try:
        
        Fl_Usr = open("Usr.txt", "r") #User File
        F.FileRead(Fl_Usr, G.L_User)
        Fl_Org = open("Org.txt", "r")
        F.FileRead(Fl_Org, G.L_Org)

    except IOError:
        print("error occured opening the file")
    
    #print(G.L_Org)
   # print(G.L_User)

    serName = gethostname()
    serPort = 5000

    serSock = socket(AF_INET6,SOCK_STREAM)
    serSock.bind((serName, serPort))
    serSock.listen()

    print("HI from server \n\n")
    print(serName + "  "+ str(serPort))
    while True :
        client, Address = serSock.accept()
        print("connected from :  ", Address)
        try:
            hndle = Server(client)
            hndle.start()

        except IOError:
            print("Io error occured")

        except ValueError:
            print("Value error occured")

        except :
            print ("Something went wrong")

    Fl_Usr.close()
    Fl_Org.close()



main()
        
    
