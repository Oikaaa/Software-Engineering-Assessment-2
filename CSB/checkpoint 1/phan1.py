fname = input("First name: ")
lname = input("Last name: ")
print(f"Your full name is {fname} {lname}")

userInput = input("Your input: ").upper()
print(f"Capitalized: {userInput}")

numberInput = float(input("Input a number: "))
print(f"Squared input: {numberInput**2}")

import turtle
r = float(input("Input circle's radius: "))

turtle.circle(r)
turtle.mainloop()