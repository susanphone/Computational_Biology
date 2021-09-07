# The Z-Algorithm
## Definition:
    Let S be a string. S = s_1 s_2 s_3 s_4 ... s_n
    For i > 0, define Z_i as the length of the longest prefix match of 
    S and S_i = s_i s_i+1 s_i+2 ... s_n <----(suffix of S)
    S[1...n] with S[i...n]

### Example:
         1   2   3   4   5   6   7   8   9   10  11  12  13
     S = a   b   c   a   b   d   a   b   c   a   c   a   b
    s_1= a   b   c   a   b   d   a   b   c   a   c   a   b
    Z_1 = 13        Z_6 = 0     Z_11 = 0
    Z_2 = 0         Z_7 = 4     Z_12 = 2
    Z_3 = 0         Z_8 = 0     Z_13 = 0
    Z_4 = 2         Z_9 = 0
    Z_5 = 0         Z_10= 1

### Assume we have a fast black box to compute Z values for any string.
    O(n)

## Can we use the Z-Algorithm for pattern matching?
### S = P $ T
* ($ means some new unused character)

    S: --------P-----$-----------------T-----------
       | length m    |    Z_i = m-^
#### Can a z value be greater than m?
    Yes, because of the $. $ never occurs in T

    For i>1, Z_i <= m
    if Z_i = m, then P occurs at i-(m+1) in T.

#### How do we do the Z-Algorithm?
## Z-Algorithm Details
    input : a string S = s_1 s_2 ...s_n
    output: Z_2, Z_3, ... , Z_n
        z box--v           can overlap
    S ---|_______|---|______|___|____|--------
      a b a b a b c
      1 2 3 4 5 6 7 8 9 10 
    
    Z_3 = 4
* use previous values to compute the next values

## Definition:
    For i > 1, let *r*_i be the rightmost endpoint of all Z-boxes that contain i, or 0 if no Z-boxes contain i.
    If *r*_i > 0, then let *l*_i be the left endpoint of one of the Z-boxes above.
* Of the z-boxes that contain i, which is the furthest to the right? and furthest to the left

-------------------|____|_____|_____|____|____|
                        ^       i        ^
                        *l*_i           *r*_i

### Z-Algorithm:
1. initialize l, r = 0
2. for k = 2 to n:
    * if k > r, then find Z_k by comparing S[k ... n] and S[1 .... n]
        * if Z_k > 0, then set r = k + Z_k - 1, set *l* = k
    * if k <= r, then let k' = k - l + 1
        * if Z_k' < |B|, then Z_k = Z_k' (*l*, *r* unchanged)
        * if Z_k' >= |B|, then compare S[|B| + 1, ... n] with S[*r*+1, ... n] until a mismatch occurs at position *q* >= *r* + 1
        Then set Z_k = *q* - k (= *q* - 1 - k + 1)
        *r* = q - 1 and *l* = k
        * If there are no mismatches, then *q* = n + 1

    |_________________________alpha________________|
    *l*                 k'                        *r*      *q*
    --------------------|_________beta_____________| _ _ _|
    (call the whole string alpha A and the string from k to *r* as beta B) 
    NOTE: the length of beta |B| = *r* - k + 1

### Prove the Algorthim runs in Linear Time
    Induction on the Z_k value

#### Running Time is O(n))
* iterations: n
* matches:  <= n since each match increases *r*
    * if there is a match then Z_k > 0, so update *l* and *r*
        * Z_k = *q* - k, *r* = *q* - 1, *l* = k
* mismatches: n since <= 1 per iteraion
- Therefore **O(n) time**


### Example of Z-Algorithm:
    S =  a a b b a b a a a
         1 2 3 4 5 6 7 8 9
    Z_i=   1 0 0 1 0 2 2 1 
* initial state
    * k = 2   *l* = 0 *r* = 0       k' = 2
* Z_2
    * k=3   *l*=2   *r*=2
* Z_5
    * k=5   *l*=5   *r*=5
* Z_7
    * k=7   *l*=7   *r*=8

* k'
    * k=8   *l*=7   *r*=8   k' = 2    |*B*| = 1
    * Compare S[|1| + 1, ... n] with S[8 + 1, ... n]
    * Therefore *q* = 10
    * Z_8 = 2
* Z_8
    * k=8   *l*=8   *r*=9
* Z_9
    * k=9
    * k' = 2
    * |*B*| = 1
    * *q* = 10
    * *l*=9     *r*=9

### Example of all matches
    S =  a a a a a a a a
         1 2 3 4 5 6 7 8
    Z_i=   7 6 5 4 3 2 1
* Z_2
    * k=2   *l*=2   *r*=8
        z-box from 2 to 8
    * k'=2    |*B*|=6   *q*=9
* Z_3
    * k=3   *l*=3     *r*=8
        z box from 3 to 8
    * k'=2    |*B*|=5   *q*=9
* Z_4
    * k=4   *l*=4   *r*=8

### How is this used for pattern matching?
* Pattern P   |P| = m
* Text T
* Therefor **S = P $ T**