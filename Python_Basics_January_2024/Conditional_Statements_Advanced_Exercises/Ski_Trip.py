days = int(input())
room_type = input()
evaluation = input()
price_per_night = 0
discount = 0
nights = days - 1

if room_type == "room for one person":
    price_per_night = 18.00
    discount = 0
elif room_type == "apartment":
    price_per_night = 25.00
    if nights < 10:
        discount = 0.30
    elif 10 <= nights <= 15:
        discount = 0.35
    else:
        discount = 0.50
elif room_type == "president apartment":
    price_per_night = 35.00
    if nights < 10:
        discount = 0.10
    elif 10 <= nights <= 15:
        discount = 0.15
    else:
        discount = 0.20

total_price = price_per_night * nights

total_price -= total_price * discount

if evaluation == "positive":
    total_price += total_price * 0.25
elif evaluation == "negative":
    total_price -= total_price * 0.10

print(f"{total_price:.2f}")
