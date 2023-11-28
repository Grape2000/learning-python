# Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
# Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.

################# how to do it for one string ##################
# DNA strings
#Rosalind_0808 = "CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT"

# for every DNA string:
# count total length
#print(len(Rosalind_0808))

# if C or G count  -> GC_content
#amount_GC = []

#for i in Rosalind_0808:
#    if i == "G":
#        amount_GC += "G"
#    elif i == "C":
#        amount_GC += "C"
#    else:
#        continue   
#
#print(len(amount_GC))
# calculate percentage of GC in the DNA string    
#percent = len(amount_GC) * 100 / len(Rosalind_0808)
#print(percent)



# =================================================================== #



############# how to do it for more strings at the same time ########

# calculate GC content for all of them and then find highest GC content
# prepare input

# load data
data = open("INI5.txt", "r")


#make a dictionary
# sequences -> result(dictionary)
sequences = {}

for line in data:
    if line[0] == ">":
        key = line[1:-1]
        sequences[key]=""
    else: 
        sequences[key]+=line[:-1]
print(sequences)


### loop ### 
#amount_GC = []
amount_GC = 0
for i in sequences:
    if i == "G":
        amount_GC += 1
    elif i == "C":
        amount_GC += 1
    else:
        continue
print(amount_GC)


# put loop into a function 
def GCamount(DNA):
    #amount_GC = 0
    for i in DNA:
        if i == "G":
            amount_GC += 1
        elif i == "C":
            amount_GC += 1
        else:
            continue
    return amount_GC
    

#GCvalue = (GC/len(sequences) * 100)
#sequences.append(GCvalue)
#print(sequences)

###### works till here ######
# go over all keys and values in the squences dict

#amount_GC = GCamount()
# calculate percentage of GC in the DNA string    
# percent = GCamount *100 / len(sequences)
#print(percent)