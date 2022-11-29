# NAMA : IZAZAVA PUTRI ASARI 
# NIM : 24060122120038

import ast
permen = ast.literal_eval(input()) #list_of_list berisikan list of list

def IsList(s):
    return type(s) == list

def IsAtom(s):
    if (IsList(s)):
        return len(s) == 1
    else:
        return True

def Total(p):
    if p == []:
        return 0
    else:
        if IsList(p[0]):
            return Total(p[0]) + Total(p[1:])
        if IsAtom(p[0]):
            return p[0] + Total(p[1:])

def Diskon(w):
    if w == []:
        return 0
    else:
        if IsList(w[0]):
            if Total(w[0]) % 2 == 0:
                return Total(w[0]) * 2000 + Diskon(w[1:])
            else:
                return Total(w[0]) * 1000 + Diskon(w[1:])
        else:
            if w[0] % 2 == 0:
                return w[0] * 4000 + Diskon(w[1:])
            else:
                return w[0] * 3000 + Diskon(w[1:])
                
print(Diskon(permen))