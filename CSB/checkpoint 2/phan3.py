arr = [5, 1, 8, 92, -1, 30]
total = 0
total2 = 0

num = int(input("Input a number: "))

for i in range(len(arr)):
    if num == arr[i]:
        print(f"Number found at position {arr.index(num)}")
        break
    elif len(arr) - 1 == i:
        print("Number not found")

for i in arr:
    total = total + i
print(f"Sum of numbers in list: {total}")

print("------------------")

userInput = input("Input the list of numbers\nSpace every new number\n0 to stop, every number after 0 will not be count:\n").split(" ")

for i in userInput:
    if i == "0":
        break
    else:
        total2 = total2 + int(i)
print(f"Sum of numbers in your list: {total2}")