#Testing file for connection and user authentication.
import Global as G #global variables
import FileRead as F
import UserAuth as U
Fl_Usr = open("Usr.txt", "r") #User File
F.FileRead(Fl_Usr, G.L_User)
print(G.L_User)
neel = "neel"
print(U.UserAuth(['thomas', 'Thomas']))
print(U.UserAuth(['thomas', 'Thomas']))
print(G.L_User)
print(G.L_Used)
