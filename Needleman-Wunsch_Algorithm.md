# Needle-Wunsch Algorithm
* consider two string S[1...n] and T[1...m]
Define V(i,j) be the score of the optimal alignment between S[1...i] and T[1...j]
* d is delta
* Basis
    V(0,0) = 0
    V(0,j) = V(0, j-1) + d(_, T[j])
        Insert j times
    V(i,0) = V(i-1, 0) + d(S[i], _)


* We have this table *V*
    *V[i,j]* = optimal score for aligning

    V|__0___1___2_____...____m_
    0|  0  -1  -2   -3  -4..-m                 
    1| -1
    2| -2
    .| -3
    .| -4
    .| ..
    n| -n

S   _   a
T   a   _
V(0,1) insert letter   
    d(_, a)

* Recurrence: For i>0, j>0
    see slides for equation
* In the alignment, the last pair must either be a mis/match, delete, or insert
* Square values, if you know three you can fingure out the fourth