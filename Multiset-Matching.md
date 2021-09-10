# Related Problem: Multiset Matching

    input:  text string T       =    a c t g a c a a c c ...
                        T: length = n
            multiset "pattern" M = { a, a, a, c, c, t, g, g}
                                       c t g g a c a a   
                               M : length = m        
    output: M occurs at position 2 in T, ...    

    naive alg: O(n * m)
