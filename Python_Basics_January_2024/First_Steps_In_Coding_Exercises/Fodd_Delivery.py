chicken_menu = 10.35
fish_menu = 12.40
vegan_menu = 8.15

numb_chicken_menus = int(input())
numb_fish_menus = int(input())
numb_vegan_menus = int(input())

price_chicken_menu = numb_chicken_menus * chicken_menu
price_fish_menu = numb_fish_menus * fish_menu
price_vegan_menu = numb_vegan_menus * vegan_menu

all_menus_price = price_chicken_menu + price_fish_menu + price_vegan_menu

desert = all_menus_price * 0.2

price_with_desert = all_menus_price + desert

sum_with_delivery = price_with_desert + 2.50


print(sum_with_delivery)