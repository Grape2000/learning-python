#Given: Positive integers n≤40 and k≤5
#Return: The total number of rabbit pairs that will be present after n months, if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).

## Number of rabbits is:
    # [1] new adult pairs (= number of last Gen, in pairs)
    # [2] new offspring pairs (= adults of 2 Gens before * k)
    # [3] adult pairs who are the parents of the new offpsrings

#   F1 = 1
#   F2 = 1
#   F3 = F2 + (F1*k)
#   F4 = F3 + (F2*k)
#   F5 = F4 + (F3*k)

# n = 5 ... number of generations, Fn
# k = 3 ... number of offspring pairs per pair

def rabbits(n, k):
    F1 = 1    #first generation with one pair, to young to have offspring
    F2 = 1    #second generation, one pair old enough to have babies
    Fn = 0    #calculating generation
    if n > 2:
        for number_of_Generations in range(n - 2):    #-2 = minus the first two generations
            Fn = (F1 * k) + F2    # ([3] * k) + [1] = [3] + [2] + [1]
            F1 = F2     #redefine last generation to generation before
            F2 = Fn    #redefine calculated generation to last generation
            
    #second and first generations are fixated
    elif n < 3:
        F2 = 1
    else:
        pass
        
    return F2
        
print(rabbits(30, 3))






def fib(n):
    if n > 1:
        return fib(n-1) + fib(n-2)
    else:
        return 1
    
#n = ["2","3","4","5","6","7","8","9","10"]   
#for i in range(len(n)):
#    print(fib(n))



