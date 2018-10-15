#FileRead.py
# This module is for file read and data stored into the list
#Owner :- Neel

def FileRead(file, list):
	for line in file:
		list.append(line.split())

