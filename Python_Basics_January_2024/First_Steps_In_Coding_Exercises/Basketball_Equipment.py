tax_year = int(input())

sneakers = ((tax_year * 0.4) - tax_year) * -1
outfit = sneakers * 0.8
ball = outfit * 1/4
accessories = ball * 1/5

all_sum = tax_year + sneakers + outfit + ball + accessories
print(all_sum)