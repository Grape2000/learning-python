# load data
f = open("rosalind_ini5.txt", "r")
# read lines and put it into a string
data = f.readlines()
# loop string
i = 0
for line in data:
    if i % 2 == 1:
        print(line.strip())
    i = i + 1