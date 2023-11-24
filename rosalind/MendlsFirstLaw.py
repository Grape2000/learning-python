# Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms: k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.
# Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.

# k = AA
# m = Aa
# n = aa
# probability of any offspring being Ax (having one dominant Allel) -> Pr(offspring) = Ax 
# output is a decimal number between 0 and 1 probability)

# all formulas for every possible pair of parents + the probability to have pr(Ax)
# first parent k
#kk = k/(k+m+n) * k-1/(k+m+n-1) * 1
#km = k/(k+m+n) * m/(k+m+n-1) * 1
#kn = k/(k+m+n) * n/(k+m+n-1) * 1
#first parent m
#mm = m/(k+m+n) * m-1/(k+m+n-1) * 0.75
#mn = m/(k+m+n) * n/(k+m+n-1) * 0.5
#mk = m/(k+m+n) * k/(k+m+n-1) * 1
#first parent n
#nn = n/(k+m+n) * n-1/(k+m+n-1) * 0
#nk = n/(k+m+n) * k/(k+m+n-1) * 1
#nm = n/(k+m+n) * m/(k+m+n-1) * 0.5

# number of individuals
k = 16
m = 28
n = 26

# calculate the probability
function = k/(k+m+n) * (k-1)/(k+m+n-1) * 1 +k/(k+m+n) * m/(k+m+n-1) * 1 + k/(k+m+n) * n/(k+m+n-1) * 1 + m/(k+m+n) * (m-1)/(k+m+n-1) * 0.75 + m/(k+m+n) * n/(k+m+n-1) * 0.5 + m/(k+m+n) * k/(k+m+n-1) * 1 + n/(k+m+n) * (n-1)/(k+m+n-1) * 0 + n/(k+m+n) * k/(k+m+n-1) * 1 + n/(k+m+n) * m/(k+m+n-1) * 0.5
print(function)