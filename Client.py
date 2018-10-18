from socket import *

import menu as m #menu module

def OP_T():
    try:
        ch = int(input("Enter you choice \n '1' if you want to sort by name '2' if you want to sort by minutes\n"))
        if ch == 1 or ch == 2:
            cSocket.send(str(ch).encode("utf-8"))
            print(cSocket.recv(1024).decode("utf-8"))
        else :
            print("enter valid number")
            OP_T()
    except ValueError:
        print("IT must be a number")
        OP_T()

def OP_F():
    Org_nme = input("Enter Organisation name ")
    cSocket.send(Org_nme.encode("utf-8"))
    Dom_nme = input("Enter Domain name ")
    cSocket.send(Dom_nme.encode("utf-8"))
    IP_A = input("Enter IP address ")
    cSocket.send(IP_A.encode("utf-8"))
    Minute = input("Enter minutes ")
    cSocket.send(Minute.encode("utf-8"))
    OP = cSocket.recv(1024).decode("utf-8")
    if OP == "Exist":
        print("Data Already Exist\n Try Again")
        OP_F()
    elif OP == "Error":
        print("Attepts exceeded")
        print("\n Disconnecting......")
        cSocket.close()

def OP_FI():
    Org_nme = input("Enter Organisation name ")
    cSocket.send(Org_nme.encode("utf-8"))
    OP = cSocket.recv(1024).decode("utf-8")
    if OP == "NotExist":
        print("Data Don't Exist\n Try Again")
        OP_FI()
    elif OP == "Error":
        print("Attepts exceeded")
        print("\n Disconnecting......")
        cSocket.close()


serverName = gethostname()
serverPort = 5000
cSocket = socket(AF_INET, SOCK_STREAM)
cSocket.connect((serverName, serverPort))
print("Connected to " + serverName + " at " + gethostbyname(serverName))
while True:
    cSocket.send("HI".encode("utf-8"))
    print(cSocket.recv(1024).decode("utf-8"))
   # U_nm = input("Enter Username ")
    cSocket.send(input("Enter Username ").encode("utf-8"))
    U_ack = cSocket.recv(1024).decode("utf-8")
    print(U_ack)
    if U_ack == "Recieved":
        Pswd = input("Enter password ").encode("utf-8")
        cSocket.send(Pswd)
        U_ack = cSocket.recv(1024).decode("utf-8")
        print(U_ack)
        if U_ack == "Success":
            while True:
                option = m.menu()
                cSocket.send(str(option).encode("utf-8"))
                U_acl = cSocket.recv(1024).decode("utf-8")
                print(U_acl)
                if option == 1:
                    cSocket.send(input("Enter organization name ").encode("utf-8"))
                    print(cSocket.recv(1024).decode("utf-8"))
                elif option == 2:
                    print(cSocket.recv(1024).decode("utf-8"))
                elif option == 3:
                    OP_T()
                elif option == 4:
                    OP_F()
                elif option == 5:
                    OP_FI()
                
                elif option == 6:
                    print("\n Disconnecting......")
                    cSocket.close()
                
        elif U_ack == "Failure":
            print("wrong Id password")
            print("\n Try Again")
        elif U_ack == "Exceeded":
            print("Attepts exceeded")
            print("\n Disconnecting......")
            cSocket.close()
            break

    
    
    
            
            
        
    
    
