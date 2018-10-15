import Global as G #global variables
import FileRead as F#reading file module
file = open("Org.txt", "r")
F.FileRead(file, G.L_Org)
print(G.L_Org)
