# NAMA : IZAZAVA PUTRI ASARI 
# NIM : 24060122120038

import ast
Hisoka = ast.literal_eval(input()) #list_of_list berisikan list of list

def IsList(h):
    return type(h) == list

def IsAtom(h):
    if (IsList(h)):
        return len(h) == 1
    else:
        return True

def Kartu(H):
    if H == []:
        return 0
    else:
        if IsAtom(H[0]):
            return 1 + Kartu(H[1:])
        else:
            return Kartu(H[0]) + Kartu(H[1:])
    
print(Kartu(Hisoka))