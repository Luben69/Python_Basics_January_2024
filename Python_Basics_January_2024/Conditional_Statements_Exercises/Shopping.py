budget = float(input())
peter_video_cards = int(input())
peter_processors = int(input())
peter_RAM = int(input())

total_video_cards = peter_video_cards * 250
processor_price = peter_processors * ((peter_video_cards * 250) * 0.35)
RAM_price = peter_RAM * ((peter_video_cards * 250) * 0.1)

total_price = total_video_cards + processor_price + RAM_price

if peter_video_cards > peter_processors:
    total_price = total_price - (total_price * 0.15)

if budget >= total_price:
    print(f"You have {budget - total_price:.2f} leva left!")
else:
    print(f"Not enough money! You need {total_price - budget:.2f} leva more!")