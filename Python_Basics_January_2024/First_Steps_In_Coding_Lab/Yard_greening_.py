kv_meters = float(input())
kv_meters_cena = kv_meters * 7.61
final_price_discount = kv_meters_cena * 0.18

all_final_price = kv_meters_cena - final_price_discount

print(f"The final price is {all_final_price} lv.")
print(f"The discount is {final_price_discount} lv.")