# Given: Two DNA strings s and t (each of length at most 1 kbp).
# Return: All locations of t as a substring of s.

# define variables
dna_sequence = "CTGATAGCGTGATAGCATGATAGCTGATAGCCTGATAGCCTTTAGACTGATAGCGCTGTGATGATAGCTGATAGCCCTGATAGCAGCCCCCTGATAGCATCTTGTTAGGAGTGTGTCTGATAGCGTGATAGCACTGATAGCTGATAGCTTACAACTTTCCCGTGATAGCACTGATAGCTCCTTGATAGCGATGATGATAGCTTGATAGCCGCTGATAGCTGATAGCTGATAGCTGTCATGATAGCGCTGATAGCCCTGATAGCATGATAGCTGATAGCTGATAGCCTGGCCTGATAGCTGATAGCAGGCGGCTGATAGCCGAGTGATAGCTTTTGCTTGATAGCAGGTTTGATAGCTGATAGCTGATAGCGGACAGTTGATAGCTGATAGCCTCTGATAGCTCCCTCCCGTAGTGATAGCTTGATAGCAATGGGTGATAGCTTATGATAGCTTGATAGCTGATAGCAGCATGATAGCGATGATAGCCATCTGATAGCAGGACGTGAGTCTGCTGATAGCAGTTTGATAGCACCATGATAGCTGATAGCTTGATAGCCATCTGATAGCTCGGTGTGATAGCGCTGATAGCATGATAGCTGATAGCGAATGATAGCTGATAGCTACATGTGATAGCTAACCCGAGTGATAGCATGATAGCTCTGATGATAGCATGATAGCTGATAGCGGTGATAGCGCATGATAGCGTGATAGCTGCATGATAGCTGATAGCTATGATAGCATGATAGCGAGTCTGTCTTCTGATAGCGTGATAGCTCATGATAGCATGATAGCATGATAGC"
substring = "TGATAGCTG"

# create an empty variable that - at the end of looping over the dna sequence - should contain the beginning positions of substring in dna_sequence
locations_of_substring_in_dna_sequence = []

# loop over every letter in dna_sequence, to do that: use indices (therefore, create a range with range-function) - only works like that, len would only return a number!
for index in range(len(dna_sequence)):
    # if substring fits to dna_sequence (make sure to use len(substringt) so that the code can be used for substrings of any length)...
    if dna_sequence[index:index+len(substring)] == substring:
        # ... append index number + 1 (to fit 1 - based numbering used in Rosalind) to locations_of_substring_in_dna_sequence variable
        locations_of_substring_in_dna_sequence.append(index+1)

# print result (I did it like this to match the way, the output is shown on Rosalind; exercises from the PYnative website used the end-parameter with print, that's how I got the idea!)
for item in locations_of_substring_in_dna_sequence:
    print(item, end = " ")