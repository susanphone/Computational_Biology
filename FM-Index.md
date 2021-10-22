# FM-Index
### Storage
* Human genome: 
    * suffix tree 40Gb
    * suffix array 13Gb
    * FM Index 1.5Gb

## Burrows-Wheeler Transform (BWT)
* Originally used for data compression
* Def based on suffix array: $BW[i] = \{$
$\item S[SA[i] - 1]$ if $SA[i] \neq 1$\\ 
$ \item $S[n]$ if $SA[i] = 1$ 

            1 2 3 4 5 6 7
        S = b a n a n a $

        i | SA[i] | suffix

        1 |   7   | $
        2 |   6   | a $
        3 |   4   | a n a $
        4 |   2   | a n a n a $
        5 |   1   | b a n a n a $
        6 |   5   | n a $
        7 |   3   | n a n a $

* Only i and SA[i] is stored
* A permutation from 1 to n
* Use the number and definition to find out what the burrow-wheeler transformation is

        BW[i] of S| i | SA[i] | suffix        | remaining|BWT
                                    
        BW[1] = a | 1 |   7   | $             | b a n a n  a
        BW[2] = n | 2 |   6   | a $           |   b a n a  n
        BW[3] = n | 3 |   4   | a n a $       |       b a  n
        BW[4] = b | 4 |   2   | a n a n a $   |            b
        BW[5] = $ | 5 |   1   | b a n a n a $ |            $
        BW[6] = a | 6 |   5   | n a $         |     b a n  a
        BW[7] = a | 7 |   3   | n a n a $     |         b  a 
* Letter appear is runs use **Run-Length Encoding**
    * a 2n b $ 2a

## How to decode the BTW

* Draw a table that contains the last column, which is the BWT

        a
        n
        n
        b
        $
        a
        a

* BTW is a permutation of S. SA[i] is also a permutation. The preceding letters is a permutation of S. 
* **Observe, BW is a permutation of S**
* This means that sorting the letters is the first column of the table
        f   l
        $   a
        a   n
        a   n
        a   b
        b   $
        n   a
        n   a
* BW has to procede the letter, so now we know all pairs that occur in S
    * a $, n a, n a, b a, $ b(from rotation), a n, a n
    * these pairs need to show up in the first two columns in the table  

        f   2   l
        $   b   a
        a   $   n
        a   n   n
        a   n   b
        b   a   $
        n   a   a
        n   a   a
* Now we know the triples a$b, na$, nan, ban, $ba, ana, ana

        f   2   3   l
        $   b   a   a
        a   $   b   n
        a   n   a   n
        a   n   a   b
        b   a   n   $
        n   a   $   a
        n   a   n   a

* Now we know all quadruples a$ba, na$b, nana, bana, $ban, ana$, anan

        f   2   3   4   l
        $   b   a   n   a
        a   $   b   a   n
        a   n   a   $   n
        a   n   a   n   b
        b   a   n   a   $
        n   a   $   b   a
        n   a   n   a   a

* Now we know all quintuplets   

        f   2   3   4   5   l
        $   b   a   n   a   a
        a   $   b   a   n   n
        a   n   a   $   b   n
        a   n   a   n   a   b
        b   a   n   a   n   $
        n   a   $   b   a   a
        n   a   n   a   $   a

* Now we know the sextuplets

        f   2   3   4   5   6   l
        $   b   a   n   a   n   a
        a   $   b   a   n   a   n
        a   n   a   $   b   a   n
        a   n   a   n   a   $   b
        b   a   n   a   n   a   $
        n   a   $   b   a   n   a
        n   a   n   a   $   b   a

* Notice that the order has banana in every row
* Whatever string that ends in a $ is the original string s
* You will always have a special character at the end

## FM-Index (for a string S)
* Composed of 3 parts
        1. Burrows-Wheeler Transform of S: BW[]
        2. "count" array, $C[]$
                * C[(letter)] number of letters in S that lexicgraphically less than x
        3. A data structure that lets us compute occ(x,i) = number of x's in BW[1...i] in O(1) time

### Example:
        
        S = b a n a n a $
$\Sigma$ = {$, a, b, n}

        BW[i] = a n n b $ a a 
        _____| C 
          $  | 0
          a  | 1
          b  | 4
          n  | 5

        i | $  a  b  n

        1 | 0  1  0  0
        2 | 0  1  0  1
        3 | 0  1  0  2
        4 | 0  1  1  2
        5 | 1  1  1  2
        6 | 1  2  1  2
        7 | 1  3  1  2
* This stuff is only 1.5Gb instead of 13Gb

