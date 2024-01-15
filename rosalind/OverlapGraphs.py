### GRPH Overlap Graphs ####

# Given: A collection of DNA strings in FASTA format having total length at most 10 kbp.
# Return: The adjacency list corresponding to O3. You may return edges in any order.


# load data
rosalind_input = open("rosalind_grph.txt", "r")
fasta_list = rosalind_input.read()
fasta_list = fasta_list.split(">")
fasta_list = fasta_list[1:]

# make input into a dict
fasta_dict = {}

for i in fasta_list:
    i = i.split("\n")
    key = i[0]
    value = ""
    for j in i[1:]:
        value = value + j
    fasta_dict[key] = value

print(fasta_dict)


# compare strings
for fasta1, string1 in fasta_dict.items():
    for fasta2, string2 in fasta_dict.items():
        if string1 != string2:
            if string1[-3:] == string2[:3]: # take last 3 of string 1 and compare with first 3 of sring2
                print(fasta1, fasta2)