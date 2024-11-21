needed_nylon = int(input())
needed_paint = int(input())
thinner = int(input())
hours_to_make = int(input())

nylon = 1.50
paint = 14.50
thinner_for_paint = 5
bags = 0.40

nylon_price = (needed_nylon + 2) * nylon
paint_price = (needed_paint + (needed_paint * 0.1)) * paint
thinner_price = thinner * thinner_for_paint

all_sum = nylon_price + paint_price + thinner_price + bags

sum_for_workers = (all_sum * 0.3) * hours_to_make

fr_end_sum = all_sum + sum_for_workers
print(fr_end_sum)
