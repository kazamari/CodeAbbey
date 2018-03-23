def combinations(L,length): #L is list [A,A+1, ... ,B]
    length_L = len(L)
    L_new=[]
    for start in range(0,length_L):
        if length > 1:
            unit_self = retrieve_unit_self(L, start, length)
            L_new.append(unit_self)
        if start + length <= length_L:
            unit = retrieve_unit(L, start, length)
            L_new.append(unit)
    return L_new


def retrieve_unit_self(L,start,length):
    unit=[]
    for index in range(0,length):
        unit.append(L[start])
    return unit


def retrieve_unit(L,start,length):
    unit=[]
    for index in range(0,length):
        unit.append(L[index+start])
    return unit

print(combinations('0 1 1 2 3 3 3 4'.split(), 3))