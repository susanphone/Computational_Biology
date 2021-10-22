# FM-Index - 3 Data Structures
    BW[]
    C[]
    occ(x, i)

* **Key Lemma 3.2**: The number of suffixes that are (lexicographically) $\leq_{lex} x S_{SA[i]}$ is $C[x] + occ(x,i)$

## Backwards-Search ($Q[1...m]$)
    st = 1j   ed = n   i = mj
    while st <= ed and i >= 1$ {
        x = Q[i]j;
        st = C[x] + occ(x, st-1) + 1;
        ed = C[x] + occ(x, ed);
    }
    if $st \leq ed$ report [st,ed];
    else report 'not found';
* **Time: $O(n)$**
    * Same time to search as the suffix tree
* From **st to ed** is where our pattern occurs

* Now we need to figure where the string is located
* BW[], C[], and occ(x,i) fit into **$O(n)$ space**
* To store all $O(n \log_2 n)$ space
* Only storing $n/\log n$ positions

### Suffix Array Sample
* **Idea**: only store some of SA entries - we can use *Lemma 3.2* to find other entries
* Use a dictionary data structure to store pairs $(i, SA[i])$ (key, value) where $\lceil \log_2(n)\rceil$ divides $SA[i]$, or $SA[i] = 1$

                        log(n)    2 log(n)    3 log(n)
             1 2 3 ...                                  n
        S: __a_b_c_______|______j1_____|___________|____$__
                                                  j2
        SA                                             1
        values

        j1 = can't find, so look for j-1 -> i'
        j2 = stored in dictionary
        dictionary:
            (1,n)
            (100 , log n)
            (i,j)
            (50 , 2 log n)
            (i', j-1)

        SA index:  ____________100_________50

        SA[i] = j

* Claim: $SA[i] = 1 + SA[C[x] + occ(x,i)]$ where $x = BW[i]$

        S: 1_____logn______2logn______3logn_____...___________n

* We store $(i, SA[i])$ if $j = 1$, or multiple of $\log(n)$
* We have $SA[i] = j$. Let $x = BW[i]$
* Then $S_{j-1} = x S_j$
    * We know what letter comes before j
* By **Lemma 3.2**, the number of suffixes $\leq_{lex} x S_j$ is $C[x] + occ(x,i)$ which equals $i$ prime **($\rightarrow i' = C[x] + occ(x,i)$)**

* $SA[i] = j-1 = SA[i] - 1$
    * $\rightarrow SA[i] = 1 + SA[i']$ 
    * $\rightarrow = 1 + SA[C[x] + occ(x,i)]$

## Compute Suffix Array (i)
    i' = i
    delta = 0
    while !SA hasKey(i') {
        x = BW[i'];
        i' = C[x] + occ(x,i');
        delta++;
    }
    return SA.getVal(i') + delta;
* Time: $O(\log n)$
* Pattern Matching Time: $O(m + occ \times \log^2(n))$

### Example:
    BW[i] of S| i | SA[i] | suffix        |BWT                            
    BW[1] = a | 1 |   7   | $             | a
    BW[2] = n | 2 |   6   | a $           | n
    BW[3] = n | 3 |   4   | a n a $       | n
    BW[4] = b | 4 |   2   | a n a n a $   | b
    BW[5] = $ | 5 |   1   | b a n a n a $ | $
    BW[6] = a | 6 |   5   | n a $         | a
    BW[7] = a | 7 |   3   | n a n a $     | a 

    Dictionary:
        (5,1)
        (3,4)

* Compute SA[5]
    * Dictionary has key so return
* Compute SA[4]
    * The dictionary does not has the key

            i'= 4
            x = b
            i' = C[4] + occ(1, i') => 5
            delta = 1
        * returns 1 + 1 = 2
    * SA[4] = 2
* Compute SA[7]
    * need to take two iterations

            i' = 7
            x = a
            i' = 1 + 3 => 4
            delta = 1

            i' = 4
            x = b
            i' => 5
            delta = 2

        *returns 1 + 2 => 3
    * SA[7] = 3