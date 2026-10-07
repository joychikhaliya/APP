import numpy as np
import random 

arr=np.array([1,2,3,4,5])
print(arr)
print(type(arr))



arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)


arr = np.array([1, 2, 3, 4])
print(arr[0])

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('2nd element on 1st row: ', arr[0, 1])


arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5])


arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[1, 1:4])


arr=np.array([1,2,3,4,5,6,7,8,9,10])
print(arr)
np.sum(arr)
print(type(arr))


heart_rates = np.random.randint(80, 151, size=10)

first_5_minutes = heart_rates[:5]

maximum = np.max(heart_rates)
minimum = np.min(heart_rates)
average = np.mean(heart_rates)

minutes_exceeded_120 = np.where(heart_rates > 120)[0] + 1

print("Heart rates:", heart_rates)
print("First 5 minutes:", first_5_minutes)
print("Maximum:", maximum)
print("Minimum:", minimum)
print("Average:", average)
print("Minutes exceeding 120 bpm:", minutes_exceeded_120)
