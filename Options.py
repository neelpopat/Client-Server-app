
#options are combined and kept here.
#code is done by Thomas, Ravjot, Augustine
#Merged by Neel
import Global as G
def Option1(name):
    for element in G.L_Org:
        if name in element:
            Tmp_string = "Name : " + element[0] + "Domain : " + element[1] + "Ip address : " + element[2] + "Minutes : " + element[3]
            return Tmp_string

def Option2():
    Tmp = []
    for element in G.L_Org:
        Tmp.append(int(element[3]))

    minimum = minimum(Tmp)
    maximum = maximum(Tmp)
    mean = mean(Tmp)
    Tmp_string = "Min value : " + str(minimum) + "Max value : " + str(maximum) + "Mean value : " + str(mean)
    return Tmp_string

def Option3(ch):
    Tmp_list = []
    if ch == 1:
        Tmp_list = sorted(G.L_Org, key=lambda x: x[0])
    elif ch == 2:
        Tmp_list = sorted(G.L_Org, key=lambda x: x[3], reverse = True)
    return Tmp_list

def Option4(list):
    if list not in G.L_Org:
        file = open("Org.txt", "a")
        for x in list:
            file.write(x)
            if x != list[3]:
                file.write("\t")
        file.write("\n")
        file.close()
        G.L_Org.append(list)
        return "Success"
    
def Option5(name):
    for element in G.L_Org:
        if name in element:
            G.L_Org.remove(element)
            file = open("Org.txt", "w")
            for el in G.L_Org:
                for x in el:
                    file.write(x)
                    if x != el[3]:
                        file.wirte("\t")
                file.write("\n")
            file.close()
            return "Success"
        
def minimum(list):
    mn = list[0]
    for x in list:
        if x < mn:
            mn = x

    return mn

def maximum(list):
    mx = list[0]
    for x in list:
        if x > mn:
            mn = x

def mean(list):
    total = 0
    for x in list:
        total = total + x
    mean = total/len(list)
    return mean
