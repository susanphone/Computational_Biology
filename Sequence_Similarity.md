# Sequence Similarity
* The distant between two strings

## Earliest Researches in Sequence Comparison
    see slides

## Why do we need to compare sequences?
* Given two DNAs, RNAs or proteins, high similarity -> similar function or 3d structure

### Applications of Sequence Comparison
* Inferring the biological function of gener
* Finding evolution distance between two species
* Helping genome assembly
* Finding common sequences in two genomes
* Finding repeats within a genome
* Many other applications

## Algorithms
* String Alignment Problem (**Global Alignment**)
* Local Alignment
* Semi-Global Alignment
* Gap penalty
* Scoring function

## String Edit
* Given two strings A and B, edit A and B with the minimum number of edit operations:  
    * Replace a letter
    * Insert
    * Delete
* Example: see slides
    A = interestingly
    B = bioinformatics
        Edit distance = 11 <- the spaces that are not in common
### String Edit Problem
Instead of minimizing the number of edge operations, we can associate a cost function to the operations and minimize the total cost. Such cost is called edit distance.
### String Alignment Problem
Instead of using string edit, people like to use string alignment
* we use *similarity function* instead of *cost function* to evaluate the goodness of the alignment.
* See alignment example in slides
    * Must me equal length (insertions and deletions)
    * Top string "_" is insertion
    * Bottom string "_" is deletion
    * The alignment has a similarity score of 7
* This is an **optimal alignment**
* String Alignment problem tries to find the alignment with the maximum similarity score
* Also known as **Global Alignment**

    Input: S, T stirngs
        d(A, C) = scoring function          d is delta
        (A, -)
        (-, G)
        S'  A  C  - G T
        T'  C  C  T G T
            -1 2 -1 2 2 score = 4
        Let |S|=n and |T|=m
    Output: best(maximum score) alignment of S and T given d

*Definition: An alignment of S and T is defined by two strings S' and T' such that S' = S(with gaps), and T' = T(with gaps), and |S'| = |T'|.
*The score of an alignment S', T' = Sum(len(S') i = 1) d(S'[i], T'[i])

    Typically, d(x,-) = d(-,x) = -1
           d(x,x) = 2
           d(x,y) =-1
           (x != y)

## Edit Distance Example
    
    Input: strings S, T
        S is length m
        T is length n

    Output: edit distance between S, T
    D(S,T) = edit distance between S and T
    d(x,x) = 0
    d(x,y) = 1
    d(-, x) = d(x, -) = 1

    S[1...i]
    T[1...j]
    D(i,j) = edit distance between S[1...i] and T[1...j]

    Base conditions:
        - D[0,0] = 0
        - D[0,j] = j
        - D[i,0] = i
    Recurrence Relation:
        D(i,j) = {
            D(i-1,j-1) + d(S[i], T[j])
            D(i,j-1) + 1
            D(i-1,j) + 1
        }
    NOTE: 1 is used for edit distance instead of d(_, T[j]) or d(S[i], _)

    Two Strings:
        S = CAT
        T = CCTT

            C   C   T   T
     D|_ 0___1___2___3___4
     0|  0   1   2   3   4                      
    C1|  1   0   1   2   3   
    A2|  2   1   1   2   3
    T3|  3   2   2   1 | 2 |
    Edit Distance: 2
### How to compute the alignments
    Go right to left and decide which path to take
    Possible Paths
        
            C_AT     CA_T    CAT_    _CAT
            CCTT     CCTT    CCTT    CCTT
            0110     0110    0101    1010



