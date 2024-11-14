dep_sum = float(input())
dep_months = int(input())
year_interest = float(input())

year_interest1 = year_interest / 100

final = dep_sum + dep_months * ((dep_sum * year_interest1) / 12)

print(final)