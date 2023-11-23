# Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).
# Return: The protein string encoded by s

s = ["AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"]
# split up into triplets and save them into a list
# at every third position 

# 1) going over list end split at 3 position -> put it into list

triplets = []
i=0

for i in range(len(s)):
    #print(s[i:i+3])
    triplets.append(s[i:i+3])
    i+=3
print(triplets)
  


# 2) check which AA fits triplet

#i=0
#while i<9:
#    triplets.append(s[i:i+3])
#    i+=3