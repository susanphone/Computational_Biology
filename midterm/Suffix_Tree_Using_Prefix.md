## Longest Common Prefix (LCP)
              1 2 3 4 5 6 7 8 9 10 11
    input S = a c t g a c t g g  a  a
    length n

* LCP queries: LCP(i,j) = length of longest common prefix between $S[i...n]$ and $S[j...n]$

        Example: LCP(2,6)
        given position 2, if you look at the suffix of position 2 and 6, how many characters match
            Answer: LCP(2,6) = 3
* How can we build a data structure that allows us to build this structure quickly?
1. Start by build a suffix tree
    * input S = a c t g a c t g g a a $
    * leads to leaf node 2 and leaf node 6
2. Find the internal nodes
3. Find the depth of the node (**Lowest Common Ancestor(LCA)**)
    * depth of LCA = 3 = LCP(2,6)

### LCP Algorithm
Proprocessing Step:
1. Build suffix tree T
2. Find the depths of the internal nodes
3. Build 'nice' LCA data structure for our tree T
    * This will allow us to find LCA very fast, making query step $O(1)$ time

Query Step:
* LCP(i,j)
1. Find node $v = LCA(i,j)$ nodes
2. Report depth(v)

### LCA Theory
Query: get two nodes i and j and find the lowest common ancestor, which could be the root node
* Node is true if it can see both nodes
* Start at the nodes and walk upwards and only move the pointer that's at the greatest depth
* A complicated data structure that built for this:
    * We can compute LCA in $O(1)$ time
        * Targen came up with this
* Can support LCP queries

## Finding Palindromes in Strings
    input: a string S
    output: all maximal palindromes contained in S
* You can have even or odd length palindromes (maximal palindrome)
* We can use LCP queries to solve this problem fast
* Starting at location i, how many letters can we match in the reverse direction starting at i-1
1. Linear Time $O(n)$
    1. Make a generalized suffix tree for string $S$ and string $S^rev$ (reverse of S)
    2. Find the depths of internal nodes
    3. Add LCA data structure 
2. Linear $O(n)$
    * For $i = 1...n$, let $k = LCP(S_i, S^{rev}_{n-i+2})$
    * Report $S[(i-k)...(i+k-1)]$ even palindromes
3. Linear $O(n)$
    * For $i = 1...n$, let $k = LCP(S_i, S^{rev}_{n-i+1})$
        * if $k > 0$, Report $S[(i-k+1)...(i+k-1)]$ odd palindromes

* Not just the longest palindrome, but ALL palindromes in two strings
* Even palindrome, length of at least 0
* Odd palindrome, length of at least 1

