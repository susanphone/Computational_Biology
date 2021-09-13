# Assignment 1 Problem 2: Z-Algorithm
# CSCI 551: Advanced Computational Biology
# September 13, 2021

"""
This program takes in a single FASTA file to search and 
prompts the user for a query sequence and returns a list of full 
matches to the command line, along with their start index.
"""


def zAlgorithm(sequence, query):
    """
    Sequence is the string to be searched by.
    Query is the string searched for in the sequence.
    """
    # Construct the single string
    combinedString = query + "$" + sequence

    # Create empty list for matches and an empty list for all Z vlaues
    matchList = []
    zList = [-1]


    # Initiate the variables for the z-algorithm
    rightEdge = 0
    leftEdge = 0
    kPrime = 0
    beta = 0

    # Iterate over each letter in the combined string
    # K represents position in the string
    for k in range(1, len(combinedString)+1):
        tempZ = 0
        increment = 0

        # Case 1: If k is not in Z-box
        if k > rightEdge:
            
            # Match letters until mismatch found
            while ((len(combinedString) - 1 >= k + increment)
                    and (combinedString[increment] == combinedString[k + increment])):
                tempZ += 1
                increment += 1
            
            if tempZ > 0:
                rightEdge = k + tempZ - 1
                leftEdge = k
            zList.append(tempZ)
        
        
        # Case 2: In Z-box
        else:
            kPrime = k - leftEdge + 1
            beta = rightEdge - k + 1

            # If Match does not extend past Z-box end, record value
            if zList[kPrime] < beta:
                tempZ = zList[kPrime]

            # If matching extends past Z-box end, then move Z-box
            else:

                # Match letters past Z-box end until mismatch is found
                while ((len(combinedString) - 1 >= rightEdge + 1 + increment)
                       and (combinedString[beta + 1 + increment] == combinedString[rightEdge + 1 + increment])):
                    tempZ += 1
                    increment += 1
                tempZ = beta + increment - 1

                # Update Z-box edges
                rightEdge = increment - 1
                leftEdge = k
            zList.append(tempZ)

    # Use Z scores to compose list of indexes where perfect matches were found
    for zScore in range(len(zList) -1):
        if zList[zScore] == len(query):
            matchList.append(zScore - len(query))
    return matchList


def main():
    """handels the input, calls the z-algorithm, and prints the output"""
    # Handel the file opening of the FASTA file to be searched
    file = open(r"C:\Users\doodw\PycharmProjects\Zalgorithm\venv\input\testfasta.fasta", 'r')
    
    # Create an empty string to hold text sequence
    sequence = ""
    
    # Flag to ensure only one sequence is read from the Fasta file
    single_sequence_flag = False
    
    # Read in and concatenate sequence lines from Fasta file
    for line in file:
        if line.find('>') != -1:    # Ignores Header
            # Ignores multiple sequences in Fasta file
            if single_sequence_flag:
                break
            continue
        else:
            line = line.strip().lower()
            sequence += line

    # Prompt the user for query
    query = input("Please enter a DNA sequence to search for: ").strip().lower()

    # Call the z-algorithm
    output = zAlgorithm(sequence, query)

    # Print the output from the z-algorithm
    for index in output:
        print("A perfect match found at: " + str(index))

main()
