#1
for i in range(3,13):
    print(i)

#2
limit = int(input("Input a number: "))
if limit > 0:
    for i in range(0,limit + 1):
        print(i)
else:
    print("Invalid input")

#3
limitOdd = int(input("Input a number: "))
if limitOdd > 0:
    for i in range(0,limitOdd + 1):
        if i % 2 != 0:
            print(i)

#4
import turtle
edges = int(input("Input number of edges: "))

for i in range(edges):
    turtle.forward(100)
    turtle.right(360/edges)

turtle.mainloop()