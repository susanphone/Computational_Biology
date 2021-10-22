## Midterm 
    Q3 from exam
            a t a c g
        V    0 1 2 3 4 5
        ___|____________
        0| 0-1-2-3-4-5
        a 1|-1 2 1 0-1-2
        a 2|-2 1 1 3 2 1
        t 3|-3 0 3 2 2 1
        g 4|-4-1 2 2 1 4

    a | - | a | t | g |
    a | t | a | c | g |
    +2  -1  +2 -1  +2 = 4 

    Q4
    Suffix tree to find longest repeated substring
        1 2 3 4 5 6 7 8 9 10 11
    S = g a c t g a a c t  g  $

    S1 = g[10] a[5]c t g a a c t g $
    S2 = a [6]c t g a[7] a c t g $
    S3 = c t g[8] a a c t g $
    S4 = t g [9] a a c t g $
    S5 = g a a c t g $
    S6 = a a c t g $ 
    S7 = a c t g $ 
    S8 = c t g $
    S9 = t g $
    10 = g $
    11 = $

    Deepest internal node
    2 and 7 

    Q5
    Suffix Arrays
        1 2 3 4 5 6 7 8 9 10
    S = a c t t c c a t c $
    \sigma = {$ a, c, g, t }
    i | SA[i] | Suffix

    1 |  10   | $
    2 |   1   | a c t t c c a t c $
    3 |   7   | a t c $
    4 |   9   | c $
    5 |   6   | c a t c $
    6 |   5   | c c a t c $
    7 |   2   | c t t c c a t c $
    8 |   8   | t c $
    9 |   4   | t c c a t c $
    10|   3   | t t c c a t c $

    Nice simple data structure but have to store O(n log_2 n)
    Pattern Q = tc
    Binary search look at the midpoint and see if the letter is there L and R and find the midpoint, compare the midpoint, and since t is greater than c M become L and R stays the same. Choose a midpoint between 5 and 10 and we find the pattern at index 8. 
    Find all the occurences of the pattern, which is 8 and 4