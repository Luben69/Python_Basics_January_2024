budget = int(input())
season = input()
fishers = int(input())
rent = 0

if season == "Spring":
    rent = 3000
elif season in ["Summer", "Autumn"]:
    rent = 4200
elif season == "Winter":
    rent = 2600

if fishers <= 6:
    rent *= 0.90
elif 7 <= fishers <= 11:
    rent *= 0.85
else:
    rent *= 0.75

if fishers % 2 == 0 and season != "Autumn":
    rent *= 0.95

difference = budget - rent

if difference >= 0:
    print(f"Yes! You have {difference:.2f} leva left.")
else:
    print(f"Not enough money! You need {abs(difference):.2f} leva.")
