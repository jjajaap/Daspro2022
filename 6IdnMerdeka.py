# NAMA : IZAZAVA PUTRI ASARI 
# NIM : 24060122120038

import ast
Naruto = ast.literal_eval(input()) #list_of_list berisikan list of list

def NbElm(s):
    return len(s)
    # if s == []:
    #     return 0
    # else:
    #     return 1 + NbElm(s[1:])

def IsList(s):
    return type(s) == list

def IsAtom(s):
    if (IsList(s)):
        return len(s) == 1
    else:
        return True

def IsOneElmt(S):
    return NbElm(S)==1

def Max2(a,b):
    if a >= b:
        return a
    else:
        return b

def Max(s):
    if NbElm(s) == 1:
        if IsAtom(s[0]):
            return s[0]
        else:
            return Max(s[0])
    else:
        if IsAtom(s[0]):
            return Max2(s[0],Max(s[1:]))
        else:
            return Max2(Max(s[0]),Max(s[1:]))

def Konohagakure(n):
    if n == []:
        return 0
    else:
        return Max(n[0]) + Konohagakure(n[1:])

print(Konohagakure(Naruto) * 1000000)

