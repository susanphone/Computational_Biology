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
* we use *similarity function* instead of *cost function* to evaluuate the goodness of the alignment.
* See alignment example in slides
    * Must me equal length (insertions and deletions)
    * Top string "_" is insertion
    * Bottom string "_" is deletion
    * The alignment has a similarity score of 7
* This is an **optimal alignment**
* String Alignment problem tries to find the alignment with the maximum similarity score
* Also known as **Global Alignment**

