length = int(input())
width = int(input())
height = int(input())
percent = float(input())

volume = length * width * height

volume_in_l = volume / 1000    # / 1л=1 дм3/

used_room = percent / 100    # 17% --> 0.17%

needed_liters = volume_in_l * (1 - used_room)
print(needed_liters)
