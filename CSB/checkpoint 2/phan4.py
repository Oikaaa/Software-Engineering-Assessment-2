arr = [5,1,8,92,7,30]
even = []
even2 = []

for i in arr:
    if i%2 == 0:
        even.append(i)

print(even)

userInput = input("Input the list of numbers\nSpace every new number\n0 to stop, every number after 0 will not be count:\n").split(" ")

for i in userInput:
    if i == "0":
        break
    elif int(i)%2 == 0:
        even2.append(i)
print(even2)