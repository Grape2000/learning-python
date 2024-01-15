#working with files
#Given: A file containing at most 1000 lines.
#Return: A file containing all the even-numbered lines from the original file. Assume 1-based numbering of lines.

# open file 
f = open("input.txt", "r")
# f.readline() to take a single line
# read even numbered lines
output = f.readlines()[1::2] 
# print(output)

# save output as file 

output_file = open("output.txt" , "w")

# write data

for i in output:

    output_file.write(str(i) + "/n")
    output_file.close()
print(output_file)




