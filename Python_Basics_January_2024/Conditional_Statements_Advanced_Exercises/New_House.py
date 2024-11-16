flower_type = input()
flower_count = int(input())
budget = int(input())

prices = {
    "Roses": 5,
    "Dahlias": 3.80,
    "Tulips": 2.80,
    "Narcissus": 3,
    "Gladiolus": 2.50
}

base_price = prices[flower_type] * flower_count

if flower_type == "Roses" and flower_count > 80:
    base_price *= 0.90
elif flower_type == "Dahlias" and flower_count > 90:
    base_price *= 0.85
elif flower_type == "Tulips" and flower_count > 80:
    base_price *= 0.85
elif flower_type == "Narcissus" and flower_count < 120:
    base_price *= 1.15
elif flower_type == "Gladiolus" and flower_count < 80:
    base_price *= 1.20

difference = budget - base_price

if difference >= 0:
    print(f"Hey, you have a great garden with {flower_count} {flower_type} and {difference:.2f} leva left.")
else:
    print(f"Not enough money, you need {abs(difference):.2f} leva more.")
