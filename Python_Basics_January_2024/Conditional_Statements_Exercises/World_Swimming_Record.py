world_record = float(input())
distance_meters = float(input())
time_to_swim_meter = float(input())

ivan_time_every_15 = (distance_meters // 15) * 12.5

total_time = distance_meters * time_to_swim_meter + ivan_time_every_15

if total_time < world_record:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    time_needed = total_time - world_record
    print(f"No, he failed! He was {time_needed:.2f} seconds slower.")