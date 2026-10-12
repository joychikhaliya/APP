import numpy as np
import pandas as pd


room_rents = np.array([2500, 4200, 3100, 5500, 4800, 3900, 6000, 2900, 4500, 3500])

print("--- Room Rents Array ---")
print(room_rents)
print()

mean_rent = np.mean(room_rents)
median_rent = np.median(room_rents)
max_rent = np.max(room_rents)
min_rent = np.min(room_rents)

print("--- Rent Statistics ---")
print(f"Mean Rent: ₹{mean_rent:.2f}")
print(f"Median Rent: ₹{median_rent:.2f}")
print(f"Maximum Rent: ₹{max_rent}")
print(f"Minimum Rent: ₹{min_rent}")
print()

data = {
    'Room_Number': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Rent': room_rents
}
df = pd.DataFrame(data)

print("--- Full Hotel Room DataFrame ---")
print(df)
print()

high_rent_rooms = df[df['Rent'] > 4000]

print("--- Rooms with Rent Greater than ₹4000 ---")
print(high_rent_rooms)
