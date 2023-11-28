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


############# my attempt did not work ###########################
############# how to do it for more strings at the same time ########

# calculate GC content for all of them and then find highest GC content
# prepare input

# load data
data = open("INI5.txt", "r")


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



# put loop into a function 
#def GCamount(DNA):
    #amount_GC = 0
#    for i in DNA:
#        if i == "G":
#            amount_GC += 1
#        elif i == "C":
#            amount_GC += 1
#        else:
#            continue
#    return amount_GC
    

#GCvalue = (GC/len(sequences) * 100)
#sequences.append(GCvalue)
#print(sequences)

# go over all keys and values in the squences dict

#amount_GC = GCamount()
# calculate percentage of GC in the DNA string    
# percent = GCamount *100 / len(sequences)
#print(percent)



############################# solution #######################

#fasta = open('rosalind_test.txt', 'r').read()

max_gc = 0.0

with open('rosalind_gc.txt') as f:
    content = f.readlines()
    for i, line in enumerate(content):
        if line.startswith('>'):
            id = line[1:]
            # reset sequence string
            seq = ''
        else:
            newseq = line.strip()
            seq = seq + newseq
            # print if last substring or if next substring starts with '>'
            if i==len(content)-1 or content[i+1].startswith('>'):
                gc = 100 * (seq.count('G') + seq.count('C')) / len(seq)
                if gc > max_gc:
                    max_gc = gc
                    max_id = id

print(max_id, end='')
print(max_gc)