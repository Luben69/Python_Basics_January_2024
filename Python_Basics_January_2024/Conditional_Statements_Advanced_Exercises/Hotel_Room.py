month = input()
nights = int(input())

if month in ["May", "October"]:
    studio_price = 50
    apartment_price = 65
    if nights > 14:
        studio_discount = 0.30
    elif nights > 7:
        studio_discount = 0.05
    else:
        studio_discount = 0
elif month in ["June", "September"]:
    studio_price = 75.20
    apartment_price = 68.70
    if nights > 14:
        studio_discount = 0.20
    else:
        studio_discount = 0
else:
    studio_price = 76
    apartment_price = 77
    studio_discount = 0

studio_total = studio_price * nights * (1 - studio_discount)

if nights > 14:
    apartment_discount = 0.10
else:
    apartment_discount = 0

apartment_total = apartment_price * nights * (1 - apartment_discount)

print(f"Apartment: {apartment_total:.2f} lv.")
print(f"Studio: {studio_total:.2f} lv.")
