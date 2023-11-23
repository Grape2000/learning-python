# Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms: k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.
# Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.

# k = AA
# m = Aa
# n = aa
# probability of any offspring being Ax (having one dominant Allel) -> Pr(offspring) = Ax 
# output is a decimal number between 0 and 1 probability)


# k/(k+m+n) * k/(k+m+n-1) * 1
# m/(k+m+n) * m/(k+m+n-1) * 0.75
# n/(k+m+n) * n/(k+m+n-1) * 0
# 

