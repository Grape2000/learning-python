print("Exercise 14.11.23")

#while loop
i = 1
while i <= 10:
    print(i)
    i += 1 #why do I need this? -> it increments i (otherwise would run forever)


#print pattern with loop

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ") # end necessary to have output next to each other
    print("")


#sum of all numbers 1 to given number
#store sum of all numbers
s = 0 
n = int(input("Enter number"))
for i in range(1, n + 1):
    s += i
    print("Sum is: " , s)
