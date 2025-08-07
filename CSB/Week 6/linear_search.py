import random
import time

arr = random.sample(range(100), 20)

print(arr)

num = int(input("Find me number: "))

def linear_search(array, number):
    for i in range(len(array)):
        if array[i] == number:
            return i
        
result = linear_search(arr, num)

print(f"{num} found at {result} of the array")