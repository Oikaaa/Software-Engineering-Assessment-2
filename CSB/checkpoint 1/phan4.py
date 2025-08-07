emailValid = []
passwordValid = []

print("== Registration ==")
username = input("Username: ")
password = input("Password: ")

def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)

if len(password) <= 8 or has_numbers(password) == False:
    print("Invalid password. Please input again")
    quit()

confirmPassword = input("Confirm password: ")
if confirmPassword != password:
    print("Passwords not match. Please input again.")
    quit()

email = input("Email: ")
for letter in email:
    if letter == "@" or letter == ".":
        emailValid.append(letter)
if len(emailValid) >= 2 and emailValid[0] == "@":
    print("Registered successfully.")
else:
    print("Invalid email. Please input again.")