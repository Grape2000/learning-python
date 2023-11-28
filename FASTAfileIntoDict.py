#### put fasta file into a dictionary

# prepare input
# load data
data = open("INI5.txt", "r")

#make a dictionary -> this part works!
# sequences -> result(dictionary)
sequences = {}

for line in data:
    if line[0] == ">":
        key = line[1:-1]
        sequences[key]=""
    else: 
        sequences[key]+=line[:-1]
print(sequences)
