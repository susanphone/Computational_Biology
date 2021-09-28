S = []
T = []
n = len(S)
m = len(T)


V = [n,m]

def delta(S, T):
    for i in S:
        dels = i
        for j in T:
            delt = j
    return dels, delt

for i in S:
    for j in T:
        if V == [0,0]:
            V = 0
        if V == [0,j]:
            V = V[0,j-1] + delta("char", T[j])
        if V == [i,0]:
            V = V[i-1, 0] + delta(S[i], "char")




