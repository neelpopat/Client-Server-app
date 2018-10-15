import Global as G
def UserAuth(list):
    for element in G.L_User:
        if G.L_User[element] == list:
            Auth = True
            G.L_Used.append(G.L_User[element])
            G.L_User.pop(element)
            
