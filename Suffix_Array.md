# Suffix Array
* requires $O(n \log n)$ bits
* Suffix trees are space inefficient, so we use a suffix array instead
* not as powerful as suffix array, but uses less space

        Human genome (3 billion base pairs)
        Suffix Tree: ~40 Gb
        Suffix Array: ~13 Gb
        
        FM-Index: 1.5 Gb
            based on suffix arrays

* Suffix array is sorted suffixes of n indices, which is why is take $O(n \log n)$
* Sorted in alphabetical order, by longest suffix


Def: A suffix array for a string $S$ of length $n$ is an array $SA$, such that $SA[i]$ = starting position of the $i$th suffix of $S$ in sorted order
* See page 73 for example
## Example:
        1 2 3 4 5 6 7
    S = b a n a n a $

Sorted suffixes:
    
    L   i | SA[i] | Suffix
        1 |   7   | $
        2 |   6   | a $
        3 |   4   | a n a $
        4 |   2   | a n a n a $
    M   5 |   1   | b a n a n a $
        6 |   5   | n a $
    R   7 |   3   | n a n a $

Each number takes $\lceil \log_2 n \rceil$ bits
* Storage needed: $O(n \log n)$ bits

        n <  2^64 => only need 1 long per index
                    => n long will suffice

### Exact Pattern Matching with Suffix Arrays
    Input: text T, pattern Q
    Idea: create a suffix array for T.
    Q = b a n
        This would mean only suffix 1 is a match
    Q = a n
        This would mean 2 and 4 are a match
* Start with the whole array and then look at the pattern letter by letter, and based on the next letter limit the range.

* Binary search can be used for this problem
    * current search range = [L,R]
    * Find the midpoint M = (L+R)/2, and change R to be M or L to M

### SA Binary Search
time: $\log n \times |Q|$
* $\min(lr)$ (*mlr*)
    * Idea: only need to look at Q past $mlr$

### SA Binary Search with LCP
keep track of little r and l values





