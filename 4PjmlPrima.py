# NAMA : IZAZAVA PUTRI ASARI 
# NIM : 24060122120038

import ast
AllMight = ast.literal_eval(input()) #list_of_list berisikan list of list

def IsList(m):
    return type(m) == list

def IsAtom(m):
    if (IsList(m)):
        return len(m) == 1
    else:
        return True

def IsPrima(n, i = 2):
    if (n < 2):
        return False
    if (n == 2):
        return True
    if (n % i == 0):
        return False
    if (i * i > n):
        return True
    return IsPrima(n, i + 1)

def Deku(d):
    if d == []:
        return 0
    else:
        if IsList(d[0]):
            return Deku(d[0]) + Deku(d[1:])
        else:
            if IsPrima(d[0]):
                return d[0] + Deku(d[1:])
            else:
                return Deku(d[1:])

print(Deku(AllMight))