# Y-Algorithm
* Define: *Y_i* = max{|M'| : M' C M, and M' matches T at position *i*} 

    input:  text string T       =    a c t g a c a a c c ...
                        T: length = n
            multiset "pattern" M = { a, a, a, c, c, t, g, g}
                                       c t g g a c a a   
                               M : length = m      
    Y1 = 3
* actual M match <=> *Yi* = m
* order of letters does not matter, only the counts matter

Let Sigma = alphabet {a, c, t, g}
* #a(M) = number of a's in M

* let C_M = (#a(M), #c(M), #g(M), and #t(M))
        ^-counts for each letter
* characters in M left to match
    `
    Let C = C_M
        r = 0 (no characters have been matched yet)
    for l = 1 to n
        if l > r
            i = l
            while C[T[i]] > 0
                C[T[i]]--
                i++
            if i > l (found a (partial) match)
                r = i - 1
                Y_l = r - l + 1
            else
                Y_l = 0
        else (l <= r)
            C[T[l-1]]++
            i = r + 1
            while C[T[i]] > 0
                C[T[i]]--
                i++
            r = i - 1
            Y_l = r - l + 1
    `
### Example Y-Algorithm
    Yi: 1   0   3    
    T:  a   c   g   a   t   c   c   a   g
    M: {a   g   t}
    sum     {a  c   t   g}
    C_M =   (1, 0,  1,  1) <what letter are in the pattern

Goal: Compute *Y_i* = max {|M'|:M c M and M' matches(prefix) T[*i* ... n]}

    T  ______________________________________________________
      ^ 1   2   3   4   5   6   7   8   ...
    i=0    -------->*l*
    C = C_M <--"remaining characters to match"

    C = (1, 0, 1, 1) -> (0, 0, 1, 1)
    r = 0 -> r=1
    l = 1 -> l=2


    Yi: 1   0   
    T:  a   c   g   a   t   c   c   a   g
        1   2   3   4   5   6   7   8   9   
* Reset the C vector
    * C = C_M which takes |Sum| time OR go backwords in your match and add back the values 
        So C = (0, 0, 1, 1) -> (1, 0, 1, 1)

    C = (1, 0, 1, 1)
    r = 1
    l = 2 -> l = 3
    Yi: 1   0   
    T:  a   c   g   a   t   c   c   a   g
        1   2   3   4   5   6   7   8   9   


    C = (1, 0, 1, 1) -> (0, 0, 0, 0)
    r = 1 -> r=5
    l = 3
    Yi: 1   0   3
    T:  a   c  [g   a   t]  c   c   a   g
        1   2   3   4   5   6   7   8   9   


    C = (0, 0, 0, 0) -> (0, 0, 0, 1) -> (1, 0, 0, 1) -> (1, 0, 1, 1)
    r = 1 -> r=5
    l = 3 -> l=5 -> l=6
    Yi: 1   0   3   2   1
    T:  a   c   g  [a   t]  c   c   a   g
        1   2   3   4   5   6   7   8   9   


    C = (1, 0, 1, 1) -> (0, 0, 1, 1)
    r = 1 -> r=5
    l=6 -> l=7 -> l=8
    Yi: 1   0   3   2   1   0   0
    T:  a   c   g   a   t   c   c   a   g
        1   2   3   4   5   6   7   8   9  


    C = (0, 0, 1, 1)
    r=5 -> r=9
    l=8
    Yi: 1   0   3   2   1   0   0   2   
    T:  a   c   g   a   t   c   c  [a   g]
        1   2   3   4   5   6   7   8   9  


    C = (0, 0, 1, 1) -> (0, 0, 0, 1)
    r=9
    l=8 -> l=9
    Yi: 1   0   3   2   1   0   0   2   1
    T:  a   c   g   a   t   c   c   a [ g ]
        1   2   3   4   5   6   7   8   9  

### => O(m + |Sum| + n) time

* Inexact pattern matching vs exact pattern matching
* Knuth-Morris-Pratt (KMP) Pattern Matching Algorithm 
    * Could be a good presentation topic
