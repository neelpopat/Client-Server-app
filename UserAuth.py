#This module is for password Authentication
#Owner :- Neel

import Global as G
def UserAuth(list):
    if list in G.L_User:
        element = G.L_User.index(list)
        G.L_Used.append(G.L_User[element])
        G.L_User.pop(element)
        return True
        
            
