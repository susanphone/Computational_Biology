# Four-Russians Algorithm Edit-Distance Speed-Up
* **Lemma**: In any edit distance table, the cost between adjacent cells differs by at most 1.
    * $|D[i,j] - D[i,j-1]| \leq 1$
    * $|D[i,j] - D[i-1,j]| \leq 1$

* Basic idea is to take a big table we are trying to fill out and divide it into some blocks. special row and columns. The size of the blocks will be size t by t, where the special rows and columns overlap and create a special square.
* Instead of solving cell by cell, we solve block by block
## Restricted Block Function
The function is going to take the special block and only look at the values of the first row and first column of the block, and map the values of the final row and final column of the block.

        ......                  .
        .                       .
        .           =>          .
        .                  ......
* Need to use dynamic programming ^ to know these blocks
* The whole string vertical is $S$ with substrings $s'$
* The whole horizontal string is $T$ with substrings $t'$
* => the special block is $S' \times T'$
* Now using the lemma, the values differ by at most 1
+ length is t by t:
            T'
        0  +1 +1 -1 0 ....
        +1
        0
    S'  -1
        -1
        0
        +1
* Consider every possible string 
* Number of entries of table to store this function:
    * $3^{2t} |\Sigma|^{2t}$

### Running time
* $3^{2t} |\Sigma|^{2t} \times t^2$
* => $O(n(\log(n)^2))$ 

* $t = \log_{2|\Sigma|}n / 2$

### Theorem:
Edit distance can be computed in $O(\frac{n^2}{\log(n)})$ time or $O(n^2/\log^2 n)$ time (*in unit-cost RAM model*)


