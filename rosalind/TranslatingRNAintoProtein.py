# Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).
# Return: The protein string encoded by s


# split up into triplets and save them into a list
# at every third position 

# 1) going over list end split at 3 position -> put it into list

rna = ("AUGAGAUUAAUUUCGGCGCACACCUGCGCGGCGUAUAACCCCACACACCCAUCUUUCGUCUAUGUAAGAGGGGCCGCUUCCACAACUCCAGGUUCGGCCGUGUCAGUGACCCACCAGACUAUGGGGAAUAAGGGUCAGCUGGGCCUGAUUGCUUCGUAUCCUGAACGCGCACUAUGCGGUGCACCUGGUUGCGUGCGUAGAGUACUAAGGACACGCGGAAACCGCUCACAGAAGUGCGGCCUUUCCCAACAGCUGUGGUACGGCCCUGUUGUAUUGGAGAAGCCAAUACACGCGCUACUCAGCCCCUGGGAAAUCGCUCGUCCAAGUGUGCCUGUUGUGUUUGUGAGCUACUUCGGUCCCAUCAAACACGAUCGCGACCAACCUUACGGACUGCCCUGUGGAGCACGACGCGAGCCUCGGAAUUCAUAUCUCCAAUCCCCGGACCAAAUGGUUACGCAUACCUUCUUGACAUGCUGUGCGGUCGUUCUCCUAACCAACUCUGCUGGGAUCACCCGCACUAAUCCUGUGUGCUCAAUGUCCCGUAUCGAUAUACCGUACCUCAAUUGCCAUCCUGCUGGCUAUAGGAAGCCAGUCCGGAAAACGGAGGACCAGUUAUCAUCAGUAUCCUGUGCACAAGGAGGUGCACGAUCGCAGAACAGACAGGAAGUCGGCCGAUCUUUCAGUGAUUUAGUAAAAAUGUGGUCCACUAUUUUGACACUUGUUACCAGAGGUUCGUGGGUAUGUCUCAAAAUGGGGCGCUCCUCAGGCUCGCCAGUUGCUCGCCCGAGCAAUCAACGUUCCGCGCAUGGGCAGCAUCCCGUCCUUCGACGUCUGAGAUUUCCGACUAGAUCUGUUCGAAAAACGACUGAACACGAGGACGGCUCGCCCAUGACAAACGGGACUGGUUUCAAGCCAUGUUUUUUCUUGAACCGCUCUCGAGCUUUAUGCUGCAUGCGGACAUACAGUCGUUUGCGAGCGGUGUUUUAUGAGAUGAUUUGCGGAGCAUGUCUAUCGCAAUGCGCGAGGAAAUCGGAGCCCGGAGGGCACAUGGGCGAAAUCCAUGCUGGACUGAUGCCGCCUAACCCCCACCUUGGGCUUACCGAACGAGCGUCAAGGCCACUAUCCCAUUGCGCUGGGACGGCCCGUCCACUUGGAGAGCUACGUGCAGCGCCUAGUGUGUUGCCGAUCGAUGUAUACGCUCUAAACAUAUACCGUACGGCGGGCCCCAAGACCUGGCGCUCAGUACUGCGGUCGCGGACGCGCCUCAGUGCUCCCCAAUCGUUGACUUAUCCUUCAUGCUCCGCACAGCGGCGAACCCUAAACGCAGUCUCACAUGUUAUGCAAACACCAGAGCGUACCACCUUCGUGACUAAUCGGACUACGAGCUAUAUUUCUGUGCUGUACCAUGUGACUAGGCAUUGGAAAAAGUUAUUUUUAGCGGAUCACCAUGGGAGUGGGGCAUCGCCAAGUUACCAGUGUCAUUUGAAUGAACGGUUCAGUUGUCUCAAUUACGACCUACAGGCCAGUUACUACCAAGACCUAGGCUGUCUACGCCCGUUUUUGACAUGGCCCAUUGAAUCCCACAGAGGCCCCCAGUUGUCAGAUAAUAUCGCAACACAGGGCACGGCUUCAUUAACUCUAGGUCCUUCCGACGGAAGUCGUAUAGGAGUCCCCCCCAGCCCCCGGCAUCUUCUCACAUCUCUCCCACUGGGGCGUGAAUCUUCUAAGCGCUCGCCCUGUUGGCGCGCCAACGUUUGUGAGGCCACUGUGGAGCUACGAAUAAUCCGUAACUCAGAAAGUACACCAUUCACCAGUACAUACGCCUGCACGAGGAUACCCCUAAUUGCGGCCCGUGAGUUCGCUAAUUCGGGGUUCCCGAUUCGAUCUAACAUGGUCAGCGGGCAUCUUUCUACCCUGGGAAUAAGGGUGCAGAACUUAGCGCCUGUGGCUUCCGUCAUAGUCAGCAUCGAUCAUGGCUUCCGCGUGAGGCCUGCGUUCUCCAGGGACCCUGUAAGCAGUCCCGAUUGUUACUGCAGUCGUUGUUCUAGUCAGACGGUCGCGUGUAUAGUAGUCAGCGGACCUCUACUCACAAGUAAAAUUGACUCUCGACAGAAAUUUUCAGAUCGAACUGCCACUGAGAUAGGAGCUUACUGUGGUCGAUCCGGAAUCCACCGUCGGACGCGCCGAAAACACUGGACUGCAACAUUCGGGAUAUACCUUGCCAGCAUAAUGGGUGCCGUUCAUUGCUCCGUGUGCGCUACUGGCAGAGCUAAUUGCUUGGUGCAGAUUUACCCAUCGCUCGGAAAACUCCGCGAUGACGCCGCUGGGGAAGUAUUUCUGCCUUUAAUCGAGUCCUCCAUUUCAAGCCCAGGUGAGGCGUCAGAUAAAAAGCCAGUUAUCGCUGCGCUGCUGCACUCGGCUGACAAUUCCCACGAUCCUAUAUUAUUCCUCGUCUGCCCAUUACAUUUUUUCAUCACAGGACCGUCUAUGCUAGCAGCGUCAUGUCGAGAAUUAUGCCGAUAUCUUAGACCAGGUAAUCCGACAGUUCGGAGUGGACGAAGGGGGGUACGCCAACGUUUGGACACUAAUGGGGUGGAAUUAGAAGGUCGUUGGCCCACUAUUAAAUUAGGAUAUCGUCAGGGGUUCAGCUCUAGCCCCAUAAGCGCGUACAUCGGAUGUACGCGUGACGGAGGGAACACCCAGGUCGGGAGCCUCGAUUCUGAUGUCAUAAUCGAUCGCUGCGCGCUGCCAGUACGCUCUGGGUUUAACCCGGACCGGUACCGCAUACGCGGUAGGCACAGUGGGCGUAGCGUACACCGCCUUCUGGCCAGUAUGCAGCUGGAACGACGCGGAGACGGUCCUGUCGCCCAAAUCCCAGUGUCAACUAUACUCGAGCUAAAGCGAGCCCUUUAUCUAGACUCUUUUAUGAGUCAACAGGCCGUGCGCGAAGGCUGUACGCAAACCCCGGGCGGCGUCAUUAUGCUAGGAGCUGCCCUCGCCUCUCAGCAUACGUCCGAUAAGAAAUACGUGGCAUUAUCGGAAAAGAAUUCCGUACGGGUCCCAGCGGGUCCUGAUGCAUUGACGACGGGAUACAGUCCCCGGGCUAUACGCCAGCUUCGGUCUCGAGUCCGGUUAGGUAAUAAGUCAACCUUGGUCAGGUUCGUAACUUCGCAGCGGACACGCGUCGUGUGUCGGACGCCCUCUGCCAUACCGCCUGCGGAAUCGCUAGGCACACUCCGGUUCAGAGUAGAUCUGGGGCGGGCGCGGGCCUGUCUAUCCGAAGGUCGGAGGAUAUCGACUCUGGGAAUUGCGGCCGUGUAUGGGUGCUCUCCUAGCAGGCGUGAGAGCUUGAUGAAGAGCGCUAAUCCUGUGCUUGGGUGGGAGAGUAUUAUCGAUUCGAGCUAUCCCGAACUCACACGACUGGCCCUACGACCUGUCUCUUCUUGGGAUCGAUAUUGCAGUUUACUUAGCACGGCUUGUUUUUUCCAUAACAUUUCCUCUUUAGACGUGGCCCUCGUUCAGACCAGUGACCGUAUGCUGAGGCGCUUAUUCAUUCGUUGCGAUCUGGAUAGAGUAGAAGCACUGGAGUUAACGAGAAUAACAGCAACACAGUCGCUUGGACGUACUUCCAACUCCGUGGAAGCCCUCACGAGUAAGCCCUUCUUUCGGUGCUACGCUAUACCCUACUGUAAUUAUGGAGUCCUAGAUGUACGUAUAGUAAUAACUGUGGAAAGGGUCAGAGCAGAGGAGGAGGUAACGUCAGCCCUCCGAGUUGAGUCAUACCCGCAUCGGGGAAGAAGAACUGAUUCCGUCACACCUGCUCCCACUCAUACACUAGCCGUCGAAUGCCAGUCCGAUGGGUACCCCCGCAAGCACCUGCGUAGUCGCAAUAAAUUAUUGCUUAUGCCUCCUCAAGAACCCCGUAAAGCUACUGCUGAGCGCCGGCAACUUGGAAGUCUCGAUUAUGUCUGCGGCUCCAGUCUGGAGCGCAAAGUUCACAGAAUUAGGGGACCGAUCUACCACCAACUUUUUAUCUCCGGUCAAAUCGACAGUCGGCCGAUCGACUUUGAAAAAUGCUGGAACCGACUAUUUCGAGUAUUCUCGUUCAGCGCAAGUGGGUCACGGAUAAAUCUGCGGUCCUCCCGAAGUGUAUCGUGCCAAUGUACGCACCUCGGACCCCCCUAUAACACUGCUUCCCAGGUUAGGACGCUAAAUUACCGUAUAACUCGCUCCCAUAAUACUUGUCUGGGACUCGACGUCCAUAUGGCCCAUACGAGACAGUCUCGCUUGCCGGCCGCGACCUUCACUAUCUUGCUAGUUCCCAGGGUGCCGGGUCUGCUCCCGCGUAAUUUAUUUUGGGGUGCAGAGCUGUGCUCGGUCCGGCUUGCAGGCCUAGAUGAUCCCGUAACUCCCAGUCGCCGGAAGCCGCUGUGGCAGCCUCUAGCUGAAAGCGCAGCAAUAACAAAAUGUCGUCCUUGCCUCAGAGCGUCGACAUUCUGGCAAGAAUCCAGUCCAUCGAGCCCACGUUCAAGGCAAGACAAAUGGCAUAGAAGUAGUCCGGUAGAAGUGGAAAUUGGUCACGGGGAAUUGAAUCCUAAUUGUUUUCUAUGGGCUUUUGUAGGUCGCUCCUUAGCCGCCACGCCUGCAGGCGUACGUUGCAAAGAUAAUAUACAGACGGCGCCUCACGGAUUAGUGCAUGGCGAGACAUCUAUCACGCCCUGCUUUAUAAGGACUCGAAUAGCCCGACCCAUUGCGCUCCGUACCGAGAAAGGGAACCUAAGAACCUGGUACGUUGUGUGUAUCGGAGUCCAAGAUUGCACCAGACACAACAUUUAUUUCGUGACGUCCACACCAGUUAAUAGAUGUGCCCCUGCAAGUACUCAUAUAUUGGGUGCGCCGCAGUCGGCGCCCCACCGCGCCCACGCCCACUGCGCAAUAUGCAGGGCACCUCGGGUCUGGUCUAAUGGCCAUGUUAUGGCCUCAGGCCGCGUUUGCUCUGCGCUGCAUUGGACCGUAAGGGCACCUUGUACUAUACUGUCUACCUCCAUUAGCCGUCAGAGGGACGUAUCGACGGUUCUACUCUCGGCGCGGGUUUUGGCCGGCAAUUCAAGGAGUUCAGAUCUCGAUGUGCAUGAAAAACAUCGGACGUGGUUCUACAAAUGGGGCAAAAAAGUUCUGUUGAGCCUAUUGAUCAGUUCGAGGCGGUUUUUCCGGGGUCAGCGCUCGGUUCACCUGACGGCCCGCCUUGCCCUCAGUAAAGGCGUACCUUAUAGGUACGACUCUGUCCGAGACGCCGUAUUCAUGGCUAUGAUGGUACGGACGCGAAGUGGGUACCGUGCAAGGAUCAUACCUCGUAUAAGUGCCACUAACACUGCGAGACAUGCAGUGCCUCCCACAGUCUCAAGUGGAGGGUCGUGGUGCCUUGCAUCCAAUUACCACUACACACUUAAGCCUCCGAAAGAUUCUCCGCCAGUGAGAUUAACCAUGCGACACCUCAACGGCCGGUGGGUAUCGCCAUCAGUCCUAAUCUUUCCAGGAAAUUCGAACUUUAGACACAUCAGCGGAGAGAUAAACUUUUUACCCGGUAAUUUGGGGCUAAAAACAUUUACAAACGUGCUGCAAAAACCACCACUGCACCAUUGUCCGCACGAUAGUCAAUCCACGCCACGGUUUCAUGUGCGUCAUCACUGUCAAUCAUUUGGGAUAGCGCUCACCCAUCCUCAUUUCCAGAGACCUUCCUCCACGGGUGGUCCUCUAUUGAGGGACAAUCAAGGAGCUCUCGCGUGUAUUAGCACACACCCUCGUACCGUUAAUAUGCAGUCGUGCCGCUCAACAAUUGCAGCUAACGCCAGCGGUCUCUCAAUCCAUCUGAUUUCCCCUCCAGCGCGGGUCGUAACGUGUAGGGCGUCUAAGGCGUGGUGCGCGCAUCAAAAUGACGGAACCGGGACAAACACGAUUGCACCGCGUAUUGCCGAGUGUAGCCGACAGCUUAUGAACAUACGUCCAAAUGCGCGCCUUUUCACUUUUCUUCAUGCUAGGUGGAUAGCUACUUUGCCGGAUUGCCCCCUACGAAUGGUGGGCGGGCCCCCAGUACGAUCAGUUAGGAGGCCUUGCGUAGCCAAUAGCACGGACAGAGUCAACGGCCCUGAUAGCCACGUUUUGGUCCUUCCGAUCCUUUGGCCCCUCCAACUUCCUUUUGCGCCUCGCGGAUCCACAAUGGGAAGCAACACCGUGGCCGAGAUUACAGGCUGCACCCACCACGCGGAUCUGUACGGGGCACAGAGUCAUGUUCAACCCGUUGGGCUGGAAUGUCGACGUGAUGCUUGCAAAUUAAGCACUCAAAAUGGAGCGGAUACGCAUGUGCAUAGGUCACUGGACGCUGCGGUUGUAGUGAGUGUGCUUAUUGGUGAAGCCUCGUCUUUUCGCGCGUCCAUCAAGUCCUUACGGGAAACGCUGGUCGGUGAACUUUCCGCCCGAUUCUGCCCUGUGGCGUUGGUCAUCCCACCGCUCAUCCCGGCGUCGCGCGCGACGCACCGUCGAACCCGCUUUCUUGUGUUACUACCAGACCUUAUGGCAGAGUGCACUGUCUGUAGCCGCGCUAUCAGUGGGAUUGAGUGGAGCUAUCCGAAGAACAUGGUGACGGACUCCUCGUCGUGUUGUCGGGUUUAUUUCCGCGACGUGAUUCCCCUCCGUCCAGAGCGAAGCGUUGCGUGUAGAGCGGGCUCGGGCGUUAACAAAAAGAAAGACAGUAGAAUCUUUCUUGAGUGGUCUUGCACAGGAGUCGUGGUUACUCCAAGGGGCCACCCGUUACCAAGGGGAUGCUUCAUUGGCGAGCAUAGAGUGAAUAGCCGGCCUUCUACGUGGAGCCGUCGAGCCACCUCACCUUUUAGGGCAGUGAUGGCUCCGAGUACCUUAAUGACUGGAGUUUGCAGGUGUCUGUAUCGGAAAAUACCUAAUAGGCUCUCCAACUUUUUACACCCUUCUCUUCGUCAACCAUCAGAUCUCCGCGUUGUGCUUUCAGGACAACCGGAUAAGAGAAAGGCUGGAGAGUAUCCCCACCCUGACACAAAAAGCCAUACCAACGCGAGGUGGAGAGGCGUGAGGCCAAAUUCACUGGGAAGAUUACGGCAGUGUGUGGAAUUCUCCUUACUCGAAGGAAAGCCGCAUUACGAAGCAUACGGUGUAUUCAACUAUAAUCGGCAGUACUUCGCGCUGACGAAACAUCGCUCGGGCUCUACAUGUCGCCGUUACAGCUCUGGGUGCGGGGGCCACGGCCGAUGGCAAGCUCAAAGCAGGAUUCAUAGACUCUUAUUUCGUCCGGGGCAGACAAUUAUCACCAACGGUCAUCACUCAACAUCGCUACGCGACACGGAGUGCGUUAUAGAAGCAGAAACUCGAAGGGCUUAUUACAGUUGCGAGGGGACCCGUUUUGGCCCUAAAACGCCUAAGCACCGCUACUCGUUUGUCUCCACUGGCCAGAACCUAGAAGCCUCCGGCCCGAAAAUGAACCUUCACGCUGCAGCGGCUCGAGUUGACACGUGGAGGCAACGUCCUCCCUAUUCGCACGAUGCGGUGGAUUCUCACUCAGCCGUGCUCAUGCGCGGGAUUAUACAGUGGGUUUGGAAUAAGGAAGUACGCCUCCUGCUUGAGGAAGCUGAAACCAGCGAAGCGUCACCGGGCAUAGGAGUGAGGGUUAUAAGGUCUAGGCAAUUCUCCUAUUUGCUUCGUAACCGCGAGAGGCUGUGGGUGAAGCGGAAACAGCGAUCGAACCUUCGUAUGAUGGGUAGCCCGCCAAAUGAGCAUUCCUGGGCUUGGGAUUCAAGAGCCGGAGGAGGCAUUAUGUAUUUUCGGAUAGAGUCUGACGGGCACGCUCUGCCCCGAGAUGCUGACAAAAUAUCAUGUAUCGCCCAACGGCUUGUCUUCGCAUUACUUAGCUCUGGAAUUGAUCAACGACGGGGAUGGGAAGAGAUACAUGUGCCUUGCGAAACGGGCUGUCGAAAGCGACGCUGGGCGAUGUUAAUACCCCCCGGUAAUAGUCUAGGACGUAUGGAGUUGCGUGCUGUUGAGUGUGUCAGACGUAUCAGGACCUCAAUUUGCCCACAACAAGGUAGCACGAGUCAGAUCAGACAGGUUCAGUACGGAUCCUUCACAUUUAUGGAAAGUGUCGCUCCAGGGACGGGGAGAUCGUUCAGGGCUCCCAAGGCUUAUCUUGGGGCUCGGCGGCCUGGACGUCCAGACGCAACGCUCGGCUGUCUCGAUGUAGCUUUCCAGUUUACGGUGGCCUCCAGAAAUCCGAAAUCUACUGGUGUGAAGCGUAGGGUGUCACAAAUUGACUUACAUGUGCGAGACAGGCUCACUGAUCAUUGGGAGGUGGAGUCCGCCUUUCCGCAAGCCGAUGCACUACGUGCUCUUUUAUUUCGACGUUGGCGGUUGAUCGGAGAGUACCGAGGCGGACCAUUGAGGCACGGUAUCCCUGAGCAAUUCGACUCUAUCGCGGUUUUCUAUGAUAUAAUACGAGGUCUGGACCUCGCAGGCUCCUCCGCUGUGUUGGUCCGGUUCAUCGCCUCCAGAAUCCUAAGAGCCGAACCGAUCGGACAAUUCAAGCCGGGGACUCCUCUGCUGGUGUAUCAGCGCCUUCCAUUAAGCUGCCUGCCGAGUAAUAACUGUCCCUUGGGACCCAUCGAGCCACACUGUCUCAUCACCCACCUAGGAAGUUCGUCAAGUUGUAUUGUAGCGCAGUGUGGGCGGGGCCUAACUAGUAUCCAAGUGGGGGGCUACGAAAGGACUGGGCUGUGUAACCUUAGGUUUGCGACUGUUAGUACGACAGCCUUAGAGUGCCUUUCGACUGCGCCCAGAUUGGCUGGUAUUAUAGUAUGGAAAUCUUAUGAGUCGGCCCAGGUUCACGUUCCAUGGGAAAGCGGUUGGCGCUCCAAGGUCAAGCAAUGCACAAGGCAAAUAUUCCCAUCGAGUACAAGGGACCACCAAACCCGAGCUGACAUGACACAGAGUUAA")
triplets = []


for i in range(len(rna)):
    if i == 0:
        triplets.append(rna[i:i+3])
    elif i % 3 == 0:
        triplets.append(rna[i:i+3])
print(triplets)

# aminoacids for triplets
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


# 2) check which AA fits triplet

protein = ""

for i in triplets:
    if aminoacids[i] != "Stop":
        protein = protein + aminoacids[i]
    else:
        break

print(protein)