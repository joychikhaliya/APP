import numpy as np
import pandas as pd


bills = np.array([2500, 3200, 2800, 4100, 3650, 2900, 5000, 2400, 4300, 3100])

print("Electricity Bills:")
print(bills)
print(f"Mean Bill: ₹{np.mean(bills):.2f}")
print(f"Median Bill: ₹{np.median(bills):.2f}")
print(f"Maximum Bill: ₹{np.max(bills):.2f}")
print(f"Minimum Bill: ₹{np.min(bills):.2f}")

consumers = pd.DataFrame({
    'Consumer ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Consumer Name': ['Asha', 'Ravi', 'Nisha', 'Karan', 'Meera', 'Arun', 'Priya', 'Sanjay', 'Neha', 'Vikas'],
    'Bill Amount': bills
})

print("\nConsumers with bill > ₹3000:")
print(consumers[consumers['Bill Amount'] > 3000])
