# Suffix Trees
* "trie" -> retreival
* Key-values
* You have a set of key that are strings and you want to store these
* This can see if the string is stored or not
* Each edge of the tree reps one letter
* Tries are quick to search for strings
* End of string could still be part of the middle of another string
* make an array the length of the alphBET, that reps that array of children

* we are only using the suffixes, the ends of the strings

## A trie built on the suffixes of some string $S$ (over an alphabet $\Sigma$)
* $S$ = b a n a n a $\dollar$
    * use a dollar sign to indicated the end of the string
* out first suffix is the entire string

        banana $    1   [1:7]
* the rest of the suffix tree

        anana$
        nana$
        ana$ [2:4]
        na$ [3:4]
        a$ [2:2]
        $
        a $ 6 na $ 4 na $ 2
        na $ 5 na $ 3
        $
## Space Complexity
* $|S| = n$
    * there are n leaves in the tree
    * $n-1$ internal nodes
* at most $2n$ nodes
* at most $2n$ edges
* each string is of length $n$ and being stored explicitly
* $\lceil \log_2|\Sigma| \rceil$ bits/character
* edge strings up to length $n => n \lceil\log_2|\Sigma|\rceil$ bits
* worst case $=> O(n^2 \times \log_2|\Sigma|)$ bits needed
* banana goes from [1:7]
* best case $O(n^{|\Sigma|} \log_2 n)$ bits
* Are they 0 indexed? in practice yes
## What is this useful for?
### **Exact Pattern Matching Problem** - used Z-Algorithm before
    * P: pattern
        * length $m$
    * T: text
        * length $n$
    * Goal: find all occurences of P in T

            T = banana$
            P = ana
            2 and 4 start with ana
            => pattern occurs at position 2 and position 4
            P= ann
            there are no pattern occurences of ann

    1. build A suffix tree
    2. follow the pattern
    3. reach positions of pattern, or there is no match
    * Query time: $O(m+$occ) <-- number of occurences of the pattern
    * This algorithm will run fast for any query
#### How fast can you build the suffix tree?
* take ech suffix and add it to the tree
* Simple approach: $O(n^2)$ not that fast
* can get algorithm down to linear time
### Generalized Suffix Tree for Multiple Strings
* $S_1$ = banana $
* $S_2$ = apple #
* $S_3$ = nana &

        banana$ 1
        anana$ 2
        nana$ 3
        ana$ 4
        na$ 5
        a$ 6
        $ 7

        apple# 1
        pple# 2
        ple# 3
        le# 4
        e# 5
        # 6

        nana& 1
        ana& 2
        na& 3
        a& 4
        & 5
### Longest Common Substring
* calculate the length of every substring thats shared by at least two of these strings
* which internal nodes come from 2 different strings
* the set of every internal string is the union of the children set
* The nodes that matter are the nodes that have two different strings children
* Which of these nodes has the greatest depth?
    * a$ a& is the longest common substring
* Which of these nodes has the most in common for all three
    * a& a$ apple#

### Finding Palindromes
* given a string, what's the longest palindrome it contains


