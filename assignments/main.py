def z_algorithm(sequence, query):
    """
    :argument sequence is the string to be searched by
    :argument query is the string searched for in the sequence
    :rtype: list
    :returns a list of the start indexes of full matches of query in sequence
    """
    # TODO fix the return list
    # Construct the single string
    combined_string = query + "$" + sequence
    # Create empty list for matches
    match_list = []
    # Create empty list for all Z values
    z_list = []
    # Initiate the variables for the z-algorithm
    r = 0
    l = 0
    k_prime = 0
    beta = 0
    for k in range(len(combined_string)):
        temp_z = 0
        increment = 0
        if k > r:
            while combined_string[increment] == combined_string[k + increment]:
                temp_z += 1
                increment += 1
            if temp_z > 0:
                r = k + temp_z - 1
                l = k
            z_list.append(temp_z)
        else:
            k_prime = k - l + 1
            beta = r - k + 1
            if z_list[k_prime] < beta:
                temp_z = z_list[k_prime]
            else:
                while combined_string[beta + 1 + increment] == combined_string[r + 1 + increment]:
                    temp_z += 1
                    increment += 1
                z_list[k] = temp_z
                z_list.append(temp_z)
                r = increment - 1
                l = k
    return z_list


def main():
    """handels the input, calls the z-algorithm, and prints the output"""
    # Handel the file opening and prompt the user for query
    file = open("/home/susan/school/Computational_Biology/assignments/testfasta.fasta", 'r')
    query = input("Please enter a DNA sequence to search for ").strip().lower()
    # Create an empty string to hold text sequence
    sequence = ""
    # Flag to ensure only one sequence is read from the Fasta
    single_sequence_flag = False
    # Read in and concatenate sequence lines from Fasta file
    for line in file:
        if line.find('>') != -1:    # Header ignored
            # Ignores multiple sequences in Fasta file
            if single_sequence_flag:
                break
            continue
        else:
            line = line.strip().lower()
            sequence += line
    # Call the z-algorithm
    output = z_algorithm(sequence, query)
    # Print the output form the z-algorithm
    for index in output:
        print("A perfect match found at: " + str(index))


# Call main
main()
