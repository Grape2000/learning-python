#sum all odd numbers between a and b (including a and b)

a = 4656
b = 9652
result = 0

#for n in range(0, b-a+1):
    #print("iteration", a, "adding new number", a+n, "to result", result)
    #result = result + (a + n)
#print(result)


#second option
result = 0
for n in range(a, b+1):
    #is n odd? if yes->
    if n % 2 == 1: #% is the modular (Restfunktion)
        result= result + n
 
print(result)