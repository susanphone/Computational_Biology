# Alignments
## Problem of Speed
* Let $d$ be the total number of inserts and deletes
    * $0 \leq d \leq n+m$
* If $d$ is smaller than $n+m$, can we get a better algorithm? Yes!

#### You only need to compute the values based on the total number of insertions and deletions allowed in the problem
### $O(dn)$ time

## Local Alignment
* Given two long DNAs, both of them contain the same gene or closely related gene.
    * Can we identify the gene?
* Local Alignment Problem:
    
        Given two string $S[1...n]$ and $T[1...m]$,
        amoung all substrings of $S$ and $T$,
        find the substings $A$ of $S$ and $B$ of $T$ whose global alignment has the highest score.
### Brute Force Solution
**See slides**
* Global alignment computed in $O(nm)$
* time complexity is $O(n^3m^3)$
* Can we do better?

### Dynamic Programming for Local Alignment Problem
Define $V(i,j)$ be the maximum score of the global alignment of A and B over
* all suffixes of A of $S[1...i]$
* all suffixes of B of $T[1...j]$
* NOTE: 
    * all suffixes of $S[1...i]$ = all substrings in $S$ end at $i$
    * {all suffixes of $S[$1...i]|i=1,2,...n$} = all substrings of $S$
* Then, score of local alignment is 
    * $\max_{i,j} V(i,j)$

### Smith-Waterman ALgorithm
* Basis: $V(i,0) = V(0,j) = 0$
* Recursion of $i > 0$ and $j > 0$ :
* $ V(i,j) = max
    \begin{cases}
        V(i-1,j-1) + \delta(S[i],T[j]) & \\
        V(i-1,j) + \delta(S[i], -)  &\\
        V(i, j-1) + \delta(-,T[j])
    \end{cases}$
## Problem on Space
* Note that the dynamic programming requires a lot of space $O(mn)$
* When we compare two very long string, space can be limited
* Thus, if we did not backtrack, space complexity = $O(\min(n,m))$
* The table can tell us the final score, but we cannot determine why that is the final score.
* The trick is we know two rows and store the arrows, but we don't want to store the arrows in every cell. So...
    * use divide and conquer by splitting the matrix into two by way on the two rows we know. So we can remove two regions, one to the upper right and one to the lower left.
    * refine the path recursively until we get all locations of the path.
* Every time we divide and conquer, we reduce the matrix by half, until the path is complete
1. first scan is $mn$
2. second scan is $1/2 mn$
3. $(1/2)^2 mn$

=> $mn (1 + 1/2 + 1/2^2 +....)$

=> $2mn$

### Can we recover the alignment given $O(m+n)$? 
Yes, through recursion!

### Space analysis
* space goes down to $m+n$

## Semi-Global Alignment
* Ignores some end spaces
* exmaple: ignoring beginning and ending spaces of the second sequence
### How to compute semi-global alignment?
* can be computed using the dynamic programming for global alignment with some small changes

        Spaces in the beginning S -> Initialize first row with zeros
        Spaces in the ending S -> Look for maximim in last row
        Spaces in the beginning T -> Initialize fir column with zeros
        Spaces in the ending T -> Look for maximum in the last column
        
## Gaps
* a gap in an alignment is a maximal substring of contiguous spaces in either sequence of the alignment
### General gap penalty
* there is a function that depends on the length of the gap
* Time complexity = $O(n^2m + mn^2)$
* The penalty for the gap is divided into two parts
* A convex gap penalty function g(q) is a non=negative increasing function
    * $O(nm \log(mn))$


* A matrix for a protein is much longer than a matrix for DNA

