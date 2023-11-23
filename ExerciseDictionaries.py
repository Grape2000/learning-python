#studentNumbers = { 'Bioscience Technology': 16, 'Computational Biology': 12, 'Post-Genomic Biology': 20, 'Ecology and Environmental Management': 3, 'Maths in the Living Environment': 0 }

for x in studentNumbers:
    print(x) # only prints the keys

for course, st_numb in studentNumbers.items():
    print(course, st_numb) #prints both keys and values

###########################################

def find_within_range(list_of_numbers, lower=0, upper=10):
    output = []
    # find all numbera between lower and upper bound
    # no duplicate entries in the output
    for number in list_of_numbers:
        if lower <= number <= upper:
            if number not in output:
                output.append(number)
    return output


print(find_within_range([-2, 14, 9, 3.14]))              
print([9, 3.14])
print("======")
print(find_within_range([0, 5, 10, 15]))                
print([0, 5, 10])
print("======")
print(find_within_range([2.104, 10000, -435, 2.104]))    
print([2.104])
print("======")
print(find_within_range([1, 2, 3, 4], lower=2, upper=6)) 
print([2, 3, 4])
print("======")