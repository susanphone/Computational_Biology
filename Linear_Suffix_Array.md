# Constructing Suffix Array in Linear Time
* Restrictions: time it takes to sort
## Suffix Type
* S-Type - smaller
    $suf(S,i)<suf(S, i+1)$
* L-Type - Larger
    $suf(S,i)>suf(S, i+1)$

## LMS Characters
Leftmost S-type
    l-type before s-type

## LMS Substring
* The starting and ending character are LMS characters and there is no other LMS character
* The sentinel ($) is an LMS
* If same value, s-type takes priority to l-type

## Saving Space- Pointer Array
Def 2.4: P1 is an array containing the pointers for all the LMS-substrings in S preserving their original positional order
## $S_1$
    
    2  iissi    2
    6  iissi    2
    10 iippii$  1
    16 $        0
S1 = 2 2 1 0
## Lemma: Reduction Rule
1/2 Reduction Ratio : |S1| is at most half of S

Proof: The first character in S must not be LMS and no any two consecutive characters in S are both LMS
* Worst case is alternating LMS characters
## Lemma: Order Preservation
The relatvie order of any two suffixes suf(S,i) and suf(S,j) in S1 is the same as that of suf(S, P1[i]) and suf(S,P1[j]) in S

## Inducing SA from SA1
* Buckets: Clusters of the same letters
* Right to Left

## Inducing Sorted Substrings
Find the end of each S-Type bucket, put all the LMS substrings in S into their S-type buckets in SA according to their first characters
* The will allow to correctly sort all non-size one LMS-prefixes and sentinel

## Complexity Analysis
$T(n) = T(\lfloor n/2 \rfloor) + O(n) = O(n)$

## Space Complexity
O(n log n) bits
