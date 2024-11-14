pencils_numbs = int(input())
markers_numbs = int(input())
liters_numbs = int(input())
discount = int(input())

price_pencils = 5.80 * pencils_numbs
price_markers = 7.20 * markers_numbs
price_liters = 1.20 * liters_numbs

percent_discount = discount / 100   # 0.25
all_price = price_pencils + price_markers + price_liters

fr_all_price = all_price - (all_price * percent_discount)
print(fr_all_price)
