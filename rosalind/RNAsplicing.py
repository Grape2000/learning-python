# RNA Splicing

# given: DNA string & collection of substrings acting as introns as Fasta format
# return: protein string from transcribing & translating exons of DNA string


##### first try during class #####

# 1) translate DNA into RNa -> T = U
# 2) delete introns: find introns in gene + remove them

# definition to find introns
# def find_intron(gene, intron):
    # go through gene in steps of 1
    #for gene in sample:
    # look at an intron-sized window
    # check if window == intron
    #    for intron in sample:
    # if yes: return pos_start, intro_length + pos_start = pos_end
    #        pos_start = []
    #        pos_end = []
    #        if gene == intron:
    #            return pos_start
    #        if gene != intron:
    #            return pos_end

    
# def to remove intron
#def remove_intron(gene, pos_start, pos_end):
    # slicing


# sample
# sample = {"Rosalind_10":"ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG",
#          "Rosalind_12":"ATCGGTCGAA", "Rosalind_15":"ATCGGTCGAGCGTGT"}



# FASTA format input
# use defs on FASTA input
#### put fasta file into a dictionary

# prepare input
# load data
#data = open("RNAsplicing.txt", "r")

#make a dictionary -> this part works!
# sequences -> result(dictionary)
#sequences = {}

#for line in data:
#    if line[0] == ">":
#        key = line[1:-1]
#        sequences[key]=""
#    else: 
#        sequences[key]+=line[:-1]
#print(sequences)







#### working way ###
from pathlib import Path

working_directory = Path(__file__).absolute().parent
filename_path = working_directory / "rosalind_splc.txt"

DNA_Codons = {
    "GCT": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "TGT": "C", "TGC": "C",
    "GAT": "D", "GAC": "D",
    "GAA": "E", "GAG": "E",
    "TTT": "F", "TTC": "F",
    "GGT": "G", "GGC": "G", "GGA": "G", "GGG": "G",
    "CAT": "H", "CAC": "H",
    "ATA": "I", "ATT": "I", "ATC": "I",
    "AAA": "K", "AAG": "K",
    "TTA": "L", "TTG": "L", "CTT": "L", "CTC": "L", "CTA": "L", "CTG": "L",
    "ATG": "M",
    "AAT": "N", "AAC": "N",
    "CCT": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "CAA": "Q", "CAG": "Q",
    "CGT": "R", "CGC": "R", "CGA": "R", "CGG": "R", "AGA": "R", "AGG": "R",
    "TCT": "S", "TCC": "S", "TCA": "S", "TCG": "S", "AGT": "S", "AGC": "S",
    "ACT": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "GTT": "V", "GTC": "V", "GTA": "V", "GTG": "V",
    "TGG": "W",
    "TAT": "Y", "TAC": "Y",
    "TAA": "_", "TAG": "_", "TGA": "_"
}


# reading a file and returning a list of lines
def readFile(filePath):
    with open(filePath, 'r') as file:
        return [line.strip() for line in file.readlines()]
    
# making FASTA/List file data into a dictionary
def readFASTA(FASTAFile):
    FASTADict = {}
    for line in FASTAFile:
        if ">" in line:
            FASTALabel = line
            FASTADict[FASTALabel] = ""
        else:
            FASTADict[FASTALabel] += line
    return FASTADict


def translate_seq(seq, init_pos=0):
   result = [DNA_Codons[seq[pos:pos + 3]] for pos in range(init_pos, len(seq) -2, 3)]
   return result


full_sequence = ""
#this code goes through all the keys of the dictionary (all the ">XXXXXXXXXX"-style accession numbers)
#it compares the length of the corresponding value (a string with the sequence) and saves the longest one
#in the variable "full_sequence" since the introns must be shorter than the sequence they originate from.
for key in TESTData_dict:
    if len(TESTData_dict[key]) > len(full_sequence):
        full_sequence = TESTData_dict[key]

introns = []
#this bit of code goes through all the keys of the dictionary (all the ">XXXXXXXXXX"-style accession numbers)
#it then checks that it is different from the accession number of the full_sequence and saves the corresponding
#values, the intron sequences in a list named introns
for key in TESTData_dict:
    if key != TESTData[0]:
        introns.append(TESTData_dict[key])

#the following function itarates over the gene sequence nucleotide by nucleotide and compares
#stretches of nucleotides the length of a particular intron to that very intron. in the case of a match
#it saves the starting position. This works here as a single value, because every intron only appears once.
def find_intron(gene, intron):
    position = 0
    for i in range(len(gene)-len(intron)):
        if gene[i:i+len(intron)] == intron:
            position = i
    return position

#for every intron sequence in the list of introns these lines of code save the part before and after the intron as the new full_string
#thus deleting it from the string, this works here because we do not have an overlap of intron sequences
for intron in introns:
    start = find_intron(full_sequence, intron)
    full_sequence = full_sequence[0:start] + full_sequence[start+len(intron):]

#here we join the aminoacids translated from the intronfree full_sequence and leave out the last one, the "_" for the stop codon
print("".join(translate_seq(full_sequence))[:-1])