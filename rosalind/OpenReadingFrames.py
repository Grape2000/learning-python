# Given: A DNA string s of length at most 1 kbp in FASTA format.
# Return: Every distinct candidate protein string that can be translated from ORFs of s. Strings can be returned in any order.

# sample dataset
Rosalind_99 = "AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG"

# start codon = "ATG"
# stop codon = "TAG" , "TGA" , "TAA"

# steps to do:
# start reading at position  0 in steps of 3 -> if ATG start translating and stop at TAG or TGA or TAA
# start reading at position  1 in steps of 3 -> if ATG start translating and stop at TAG or TGA or TAA
# start reading at position  2 in steps of 3 -> if ATG start translating and stop at TAG or TGA or TAA
# start reading at position -1 in steps of 3 -> if ATG start translating RNA and stop at TAG or TGA or TAA
# start reading at position -2 in steps of 3 -> if ATG start translating RNA and stop at TAG or TGA or TAA
# start reading at position -3 in steps of 3 -> if ATG start translating RNA and stop at TAG or TGA or TAA

# then translate into Protein


# all possible ORFs (ATG ... *) on both strnads (forward + reversed) on all Rfs



# load data (FASTA)
dna = "AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG"

# first translate DNA string into RNA
first_string = ""
for x in dna:
    if x == "A":
        first_string += "A"
    elif x == "T":
        first_string += "U"
    elif x == "C":
        first_string += "C"
    elif x == "G":
        first_string += "G"
fwRNA = first_string
print(fwRNA)

second_string = ""
for x in dna:
    if x == "A":
        second_string += "U"
    elif x == "T":
        second_string += "A"
    elif x == "C":
        second_string += "G"
    elif x == "G":
        second_string += "C"
rvRNA = second_string[::-1]
print(rvRNA)


### make frames ####
frame1 = fwRNA[0:]
frame2 = fwRNA[1:]
frame3 = fwRNA[2:]
frame4 = rvRNA[0:]
frame5 = rvRNA[1:]
frame6 = rvRNA[2:]


# split into triplets and make a list for each ORF


# find all positions of Start (AUG) and all positions of Stop (UAG, UGA, UAA)
range(start, stop, step)

# make ORFs for all possible starts to stops



# triplets in Protein codieren
aminoacids = {
    'UUU': 'F', 'CUU': 'L', 'AUU': 'I', 
    'GUU': 'V', 'UUC': 'F', 'CUC': 'L', 
    'AUC': 'I', 'GUC': 'V', 'UUA': 'L', 
    'CUA': 'L', 'AUA': 'I', 'GUA': 'V', 
    'UUG': 'L', 'CUG': 'L', 'AUG': 'M', 
    'GUG': 'V', 'UCU': 'S', 'CCU': 'P', 
    'ACU': 'T', 'GCU': 'A', 'UCC': 'S', 
    'CCC': 'P', 'ACC': 'T', 'GCC': 'A', 
    'UCA': 'S', 'CCA': 'P', 'ACA': 'T', 
    'GCA': 'A', 'UCG': 'S', 'CCG': 'P', 
    'ACG': 'T', 'GCG': 'A', 'UAU': 'Y', 
    'CAU': 'H', 'AAU': 'N', 'GAU': 'D', 
    'UAC': 'Y', 'CAC': 'H', 'AAC': 'N', 
    'GAC': 'D', 'UAA': 'Stop', 'CAA': 'Q', 
    'AAA': 'K', 'GAA': 'E', 'UAG': 'Stop', 
    'CAG': 'Q', 'AAG': 'K', 'GAG': 'E', 
    'UGU': 'C', 'CGU': 'R', 'AGU': 'S', 
    'GGU': 'G', 'UGC': 'C', 'CGC': 'R', 
    'AGC': 'S', 'GGC': 'G', 'UGA': 'Stop', 
    'CGA': 'R', 'AGA': 'R', 'GGA': 'G', 
    'UGG': 'W', 'CGG': 'R', 'AGG': 'R', 
    'GGG': 'G'}








######## ???? #######


#protein = ""
#stop = ["UAG","UGA","UAA"]
#print(stop)

#for i in range(len(fwRNA)//3):
#    codon = fwRNA[i:i+3]
#    if codon == "AUG":
#        protein = ""
#        f=fwRNA[i:]
#        start = 0     
    #translate to aminoacid
#    protein += aminoacids[codon]
#print(protein)



