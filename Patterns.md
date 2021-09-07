### Problem: Find all occurrences of P in T
you have a very long string known as text (t)
a shorter string known as pattern (p)
    len(T) = n
    len(P) = m

# Exact Pattern Matching Problem
#### take the pattern and find of the occurrences of that pattern

                i
    text T:     a c t g a a ... g a t       length = n
                j
    pattern P:  g a a                       length = m

#### look for every occurrence of g and see if the next letter is in the pattern
### Worst Case Runtime: O(n times m)
* DNA is fixed, it cannot change. SO the text won't change
* The pattern is dynamic and can change
* Many variations of this problem
### Optimistic Goal: O(n+m) = O(n)
