# Needle-Wunsch Algorithm
* consider two string S[1...n] and T[1...m]
* Definition: Let V(i,j) be the score of the optimal alignment between S[1...i] and T[1...j]
* Note V[0,j] V[i,0] means align empty string to S[1...i] and T[1...j] to empty string
* Observe **V[n,m]** = optimal score of aligning S and T
* d is delta
* Basis
    V[0,0] = 0
    V[0,j] = V[0, j-1] + d(_, T[j])
        Insert j times
    V[i,0] = V[i-1, 0] + d(S[i], _)


* We have this table *V*
    *V[i,j]* = optimal score for aligning
* Base conditions:
                T
        V|__0___1___2_____...____m_
        0|  0  -1  -2   -3  -4..-m                 
        1| -1
    S   2| -2
        .| -3
        .| -4
        .| ..
        n| -n

S   _   a
T   a   _
V(0,1) insert letter   
    d(_, a)
* Suppose we have an optimal alignment of S[1...i] and T[1...j]:
    S[1...i]'   A C ... A
    T[1...j]'   A T ... C
                    ^-%
    What can occur in the final alignment(column)?
    1. S[i] against T[j]
        % optimal alignment S[1...i-1] and T[1...j-1]
    2. '-' versus T[j]
        optimal alignment S[1...i] and T[1...j-1]
    3. S[i] versus '-'
        optimal alignment S[1...i-1] and T[1...j]
* In each of the cases, the alignment to the left of the final column must also be optimal
* Note: one of these cases must be correct, namely the case that yields the greatest/highest score. So, this leads us to a **recurrence relation**:
    V[i,j] = max{
        case 1: V[i-1. j-1] + d(S[i], T[j])
        case 2: V[i, j-1] + d(-, T[j])
        case 3: V[i-1, j] + d(S[i], -)
    }
* Recurrence lets us fill in the pattern for a grid of cells
           j-1     j
    i-1 |_______|_________
      i |       | can compute
    
* Recurrence: For i>0, j>0
    see slides for equation
* In the alignment, the last pair must either be a mis/match, delete, or insert
* Square values, if you know three you can figure out the fourth
* First row arrows need to be case 3, first column needs to be case 2
### Example:
    S = C A T
    T = T A A T
               T   A   A   T
        V| 0 | 1 | 2 | 3 | 4
        0| 0 | -1| -2| -3|-4
    C   1| -1| -1| -2| -3|-4
    A   2| -2| -2| 1 | 0 |-1
    T   3| -3| 0 | 0 | 0 | 2

    CASE 1 ADD -1 \
    CASE 2 ADD -2 |
    CASE 3 ADD -2 <-
* We know the optimal score = 2. Now we want to reconstruct the alignment
    T,T = 2 -> 0    then A,A = 0 -> -2   then C,A =-2 -> -1    then C,T =-1 -> 0

* Optimal Alginment:
     C  -  A  T 
     T  A  A  T   
    -1 -1  2  2
* What is the running time? **O(nm)**
    Time: 
    Space/Memory: O(nm)
