# Knuth-Morris Pratt Algorithm
Two strings as an imput and finds all occurences of the string in the text

* Don Knuth
    * Invented Tex, which is base of LaTex
    * TPK Algorithm

* James Morris
    * GUI operating system
    * lazy evaluation

* Vaughan Pratt
    * Sun Microsystems
    * median of medians
    * analysis of Shell sort

## Procedure
0. input two strings
1. preprocessing the query (S)
2. scan the text(T)
3. Shift the next match position in S by len(match) - S[current]
4. repeat step 2
    * We only look at a point an avg of two times
    * Never examine previous positions again
5. return the list

Case One: chack all possible start positions in T
Case Two: preprocessed array to check where we left off
    * Reduces redundency of checking every possible position

Examine all possible starting positions

## Time Complexity
1. O(m), for m length of S
2. O(n), for n length of T
3. O(1)

-> O(n+m) length of text and length of query

## Space
1. storing query O(m) for length of S
2. storing text O(n) for length of T
3. storing query again?? O(m) for length of S


-> O(2m + n)

Z-algorithm and KMP avoids redundant comparisons by storing information about where possible start positions could occur in the query string.

## Applications
* Pattern Matching
* Plagarism Detection
* Accelerated Spam Filtering
* Cyber Security - Intrusion Detection
* Machine Learning - extracting features for AI

## Enhancements/Combinations
* Hybrid KMP with other algorithms
    * MPI + KMP
        * adds parallelism
    * Fuzzy Pattern Matching
        * like google search
        * KMP efficiency while allowing ambiguity
        Uses
            * Disease Database
            * Close DNA Matches
