# Multiple Sequence Alighment
* ${s_1, s_2, ..., s_k}$ collection of strings
* "distance"    $\delta(x,y)$ = distance between characters x and y
* "score" $\sigma(x,y)$= score between x and y

* A multiple alighment of S is a set of k equal length seuqences.

## Applications
* align domains of proteins
* align same genes/proteins from multiple species
* predicting protein structure
## Sum-of-Pair (SP) Score
* can we generalize to score more than two strings?
* SP-score $(a_1, ..., a_k) = \Sigma_{1 \leq i < j \leq k} \delta{a_i, a_j}$ where $a_i$ can be any character or space

        c a _ t 3
        c a a t 3
        _ a a t 2
        SOP = 8
* SP-score of S' $\Sigma_x$ SP-score( $S'_1[x], ..., S'_k[x]$)
## Dynamic Programming for aligning two sequences
* Similar to calcaulating optimal alginment
* rephrased as $V(i_1, i_2) =  \max....$
* This can be generalize to compare more than 2 strings

* Use a k-dimensial array instead of 2 dimensional array
* the score preceded plus the score of the final column
* recurrence relation: 2^k - 1 combinations

## Example

    S1      c a t
    S2      c a a t

    V(0,j) = -j

* if i1 is 0 then b1 has to be 0

* Base V(0,0,...0)
* Recurrence V(i_1, i_2,...i_k) = max ....

Inefficient in time and memory if you have 20 strings of length of 99
* Store V array
    * V is 20 dimensions, each dimension has 100 spaces (because we have to store the 0th index)
    * space needed is 100^20-> too big
    * $(n + 1)^k$
* Time 
    each position needs to compute each position
    * $(n+1)^k \times 2^k \times k^2$
* Isn't optimal with more than 4 strings

## Center Star Method
minimizes Sum-of-Pair distance

* Find a string $S_c$
* Align all other strings with respect to $S_c$

## Multiple Sequence Alignment (Continued)
        input: S1, S2,...,  Sk

        S' = Si plus some gaps
        |S'1| = |S'2| = ... = |S'k|

        SOP - score
        SOP - distance

* SOP - $dist(M) = \sum_{1 \leq i < j \leq k} dist_M(S'_i, S'_j)$ 
* distance $/delta(x,y) = ?$
    * $\delta(x,x) = 0$
    * $\delta(-,-) = 0$
* $\sum_{l=1}^n \delta(S'_i[l], S'_j[l])$
* Can switch the order of sums 
* Fact: $D_M$ satisfies the triangle-inequality
    * Suppose X, Y, Z are sequences in M
            
            M:  -----X------
                -----Y------
                -----Z------
    * $D_M(X,Y) \leq D_M(X,Z) + D_M(Z,Y)$
        * $D_M(X,Y) = \delta(X[l], Y[l])$
        * $D_M(X,Z) = \delta(X[l], Z[l])$
        * $D_M(Z,Y) = \delta(Z[l], Y[l])$
    * Assume $\delta$ has this property
        * $\delta(-,-) = 0$
        * $\delta(x,x) = 0$

