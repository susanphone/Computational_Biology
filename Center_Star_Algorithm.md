# Center Star MSA Algorithm
1. Find/Compute $D(S_i, S_j)$ for all $i,j \in {1,...,k}$ <--- using Dynamic Programming
2. Find the "center sequence" $S_c$ that minimizes $\sum_{i=1}^k D(S_c, S_i)$
3. For each $S_i \neq S_c$, choose some optimal alignment between $S_c$ and $S_i$
4. Introduce spaces as needed into $S_c +$ previously algined sequences to match the spaces from step 3, for each $S_i$ in turn => produces an MSA $M$.

        M: ----Sc'----
           ----S1'----

           ----Sc'----
           ----S2'----

* Claim: Center Star provides a 2-approximation alg for MSA ( with SOP-dist)
* Proof: 
    * Let $M*$ be an optimal MSA
    * SOP-dist $(M*) = \sum_{1 \leq i < j \leq k} D_{M*}(S_i', S_j')$
    * $\geq \sum_{1 \leq i < j \leq k} D(S_i', S_j')$
    * $= 1/2 \sum_{1 \leq i < j \leq k} D(S_i', S_j')$
    * $= 1/2 \sum_{i=1}^k \sum_{j=1}^k D(S_i', S_j')$
    * $geq 1/2 \sum_{i=1}^k \sum_{j=1}^k D(S_c', S_j)$
        * $\sum_{j=1}^k D(S_i', S_j') = \sum_{j=1}^k D(S_c', S_j)$
    * = $1/2 \times k \sum_{j=1}^k D(S_c', S_j')$

* SOP-dist $(M*) \geq k/2 \sum_{j=1}^k D(S_c', S_j')$

## CS Alg => M (MSA)
* SOP-dist(M) = $\sum_{1 \leq i < j \leq k} D_M(S_i', S_j')$
    * $= 1/2 \sum_{i=1}^k \sum_{j=1}^k D_M(S_i', S_j')$
    * $\leq 1/2 \sum_{i=1}^k \sum_{j=1}^k [D_M(S_c', S_i') + D_M(S_c', S_j')]$ 
    * $=1/2 \sum_{i=1}^k \sum_{j=1}^k [D(S_c', S_i') + D(S_c', S_j')]$
    * $=1/2 \sum(\sum_i^k \sum_j^k D(S_c', S_i')) + 1/2 \sum_i^k \sum_j^k D(S_c', S_j')$
    * $= 1/2 k \sum_i D(S_c', S_i') + 1/2 k \sum_i D(S_c', S_i')$
    * $= k \sum_i D(S_c', S_i')$

* SOP-dist(M) $\leq k \sum_j D(S_c', S_j')$
* $k \sum_j^k D(S_c', S_j') \leq 2 \times$ SOP-dist(M*)
* $\leq 2 \times$ SOP-dist(M*)
* => 2 approximation for multiple alignment

## Running Time
* $O(k^2n^2)$
