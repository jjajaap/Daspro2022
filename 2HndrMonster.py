# NAMA : IZAZAVA PUTRI ASARI 
# NIM : 24060122120038

import ast
Exam = ast.literal_eval(input())

def IsList(r):
    return type(r) == list

def Konso(L,S):
    return [L]+S

def Hunter(e,G):
    if G == []:
        return G
    else:
        if IsList(G[0]):
            return Konso(Hunter(e,G[0]),Hunter(e,G[1:]))
        else:
            if G[0] % e == 0:
                return Hunter(e,G[1:])
            else:
                return Konso(G[0],Hunter(e,G[1:]))

e = int(input())
print(Hunter(e,Exam))