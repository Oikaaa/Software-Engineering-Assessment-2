import random
import time

arr = random.sample(range(100), 20)
print(arr)

num = int(input("Find me number: "))

def binary_search(array, number):
    min = 0
    mid = round(len(arr)/2)
    max = len(arr) - 1

    print(array)

    while min <= max:
        mid = (min + max) // 2
        if number == array[mid]:
            return mid
        elif number > array[mid]:
            min = mid + 1
        else:
            max = mid - 1
    
    return -1
    
result = binary_search(sorted(arr), num)

if result == -1:
    print("Cant find the valid number in the array")
else:
    print(f"{num} found at {result} of the array")
