# NAMA : IZAZAVA PUTRI ASARI 
# NIM : 24060122120038

import ast
Hero = ast.literal_eval(input()) #list_of_list berisikan list of list

def IsList(b):
    return type(b) == list

def IsAtom(b):
    if (IsList(b)):
        return len(b) == 1
    else:
        return True

def Deku(d):
    if d == []:
        return 0
    else:
        if IsList(d[0]):
            return Deku(d[0]) + Deku(d[1:])
        else:
            if d[0] % 2 != 0:
                return d[0] + Deku(d[1:])
            else:
                return Deku(d[1:])

print(Deku(Hero))