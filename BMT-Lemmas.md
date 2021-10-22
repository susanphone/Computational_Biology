# Properties:
## Let $S_i = S[i...n]$ (suffix that starts at $i$ in $S$)

## Lemma 3.2: The number of suffixes that are (lexicographically) $\leq_{lex} x S_{SA[i]}$ equals $C[x] + occ(x,i)$
* Proof:
        * Number of suffixes that start with a letter <$_{lex}x is C[x]$
        * Number of suffixes of the form x $S_j$ that $\leq_{lex} x S_{SA[i]}$ is $occ(x,i)$
                * $S_j$ has to occur before SA[i]

                                i = 4
                                x = a
                                a a n a n a $
                                C[a] = 1
                                occ(a,4) = 1
                                = 2

                                i = 7
                                x = b
                                b n a n a $
                                C[b] = 4
                                occ(b,7) =1
                                = 5
 * Definition: Given a query string Q, let $range(Q,S) = [st,ed]$, where st-1 = number of suffixes $<_{lex} Q$ and ed = number of suffixes $\leq_{lex} Q$
        * if Q= ana -> st=3 and ed=4
        * if Q =a -> st=2 and ed=4

* Gives us a way to find the ranges
## Lemma 3.3: Suppose $Q \in S$, and $range(Q,S) = [st,ed]$. Then, $range(xQ, S) = [st',ed']$ where $st' = C[x] + occ(x,st-1) + 1$ and $ed' = C[x] + occ(x,ed)$
* The new range of the new pattern
* If Q=ana, view that pattern as an empty string->add a->add n->add a (1 to n).  <----
* If Q = empty string, range = [1,n]
* How to do pattern matching with an FM Index
* Proof:
        * st' - 1 = number of suffixes that are $<_{lex} xQ
                * Either start with a smaller letter or have the form $x S_j$ where $S_j <_{lex} Q$
                        * C[x] or <=> $S_j \leq S_{SA[st-1]}$ ----> $occ(x,st-1)$
        * ed' =  number of suffixes that are $\leq_{lex} xQ
                * Either start with a smaller letter or have the form $x S_j$ where $S_j \leq_{lex} Q$
                        * C[x] or <=> $S_j \leq S_{SA[ed]}$ ----> $occ(x,ed)$

* Examples:

                initial range(emptyString, S) = [1,7] ([st,ed])
                Q = a n a
                <------
                range(a,S)
                        st' = C[a] + occ(a,0) + 1
                                = 1 + 0 + 1
                                = 2
                        starts at position 2

                        ed' = C[a] + occ(a,7)
                                = 1 + 3 
                                = 4
                        ends at position 4
                => range(a) = [2,4]

                range(na,S)
                        st' = C[n] + occ(n,1) + 1
                                = 5 + 0 + 1
                                = 6
                        ed' = C[n] + occ(n,4)
                                = 5 + 2
                                = 7
                => range(na) = [6,7]
                range(ana, S)
                        st' = [3,4]