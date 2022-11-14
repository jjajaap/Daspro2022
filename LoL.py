def IsEmpty(S):
    return S==[]

def JmlElmtList(S):
    if isinstance(S, list):
        return len(S)
    else:
        return 1

def IsAtom(S):
    return not(IsEmpty(S)) and JmlElmtList(S) == 1

def IsList(S):
    return not(IsAtom(S))

def Konso(L,S):
    if IsEmpty(S):
        return [L]
    else:
        return [L]+S

def Konsi(L,S):
    if IsEmpty(S):
        return [L]
    else:
        return S+[L]

def FirstList(S):
    if not(IsEmpty(S)):
        return S[0]

def LastList(S):
    if not(IsEmpty(S)):
        return S[-1]

def HeadList(S):
    if not(IsEmpty(S)):
        return S[:-1]

def TailList(S):
    if not(IsEmpty(S)):
        return S[1:]

def IsOneElmt(S):
    return JmlElmtList(S)==1

def IsEqS(S1,S2):
    if IsEmpty(S1) and IsEmpty(S2):
        return True
    elif not IsEmpty(S1) and IsEmpty(S2):
        return False
    elif IsEmpty(S1) and not IsEmpty(S2):
        return False
    elif not IsEmpty(S1) and not IsEmpty(S2):
        if IsAtom(FirstList(S1)) and IsAtom(FirstList(S2)):
            return FirstList(S1) == FirstList(S2) and IsEqS(TailList(S1),TailList(S2))
        elif IsList(FirstList(S1)) and IsList(FirstList(S2)):
            return IsEqS(FirstList(S1), FirstList(S2)) and IsEqS(TailList(S1), TailList(S2))
        else:
            False

def IsMember(A,S):
    if IsEmpty(S):
        return False
    else:
        if IsAtom(FirstList(S)):
            return A == FirstList(S) or IsMember(A, TailList(S))
        else:
            return IsMember(A,FirstList(S)) or IsMember(A,TailList(S))

def IsMemberLoL(L,S):
    if IsEmpty(L) and IsEmpty(S):
        return True
    elif not(IsEmpty(L)) and IsEmpty(S):
        return False
    elif IsEmpty(L) and not(IsEmpty(S)):
        return False
    else:
        if (IsAtom(FirstList(S))):
            return IsMemberLoL(L,TailList(S))
        else:
            if IsEqS(L,FirstList(S)):
                return True
            else:
                return IsMemberLoL(L,TailList(S))

def Rember(a,S):
    if IsEmpty(S):
        return S
    elif IsList(FirstList(S)):
        return Konso(Rember(a,FirstList(S)),Rember(a,TailList(S)))
    else:
        if FirstList(S) == a:
            return Rember(a,TailList(S))
        else: 
            return Konso(FirstList(S),Rember(a,TailList(S)))

def Max2(a,b):
    if a>=b:
        return a
    else:
        return b

def Max(S):
    if IsOneElmt(S):
        if IsAtom(FirstList(S)):
            return FirstList(S)
        else:
             return Max(FirstList(S))
    else:
        if IsAtom(FirstList(S)): 
            return Max2(FirstList(S),Max(TailList(S)))
        else:
            return Max2(Max(FirstList(S)),Max(TailList(S)))