#1
numInput = float(input("Input a number: "))
if numInput > 13:
    print("This number is larger than 13")
else:
    print("This number is equal or not larger than 13")

#2
evenInput = int(input("Input a number: "))
if evenInput % 2 == 0:
    print("This number is even")
else:
    print("This number is not even")

#3
month = int(input("Input a month: "))

if month > 0 and month < 13:
    if month == 2:
        print("This month has 28 or 29 days if in leap years")
    else:
        if month < 8 and month % 2 != 0:
            print("This month has 31 days")
        elif month >= 8 and month % 2 == 0:
            print("This month has 31 days")
        else:
            print("This month has 30 days")
else:
    print("Invalid month")