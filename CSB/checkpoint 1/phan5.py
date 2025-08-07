import random

print("== FREAKING MATH CONSOLE ==")
print("Give correct answers to get scores.")
score = 0

for i in range(0, 100):
    Number_1 = random.randint(0, 25)
    Number_2 = random.randint(0, 25)
    randomOperator = random.randint(0, 3)
    randomAns = random.randint(0, 1)
    ans = ""
    rielAnswer = ""
    tf = True
        
    operators = ["+" , "-" , "*", "/"]

    selectedOp = operators[randomOperator]

    if selectedOp == "+":
        rielAnswer = Number_1 + Number_2
    elif selectedOp == "-":
        rielAnswer = Number_1 - Number_2
    elif selectedOp == "*":
        rielAnswer = Number_1 * Number_2
    else:
        rielAnswer = Number_1 / Number_2

    if randomAns == 0:
        ans = rielAnswer + random.randint(0, 10)
    else: 
        ans = rielAnswer

    print(f"{Number_1} {selectedOp} {Number_2} = {ans}")
    answer = input("1 for True, 0 for False: ")

    if ans == rielAnswer:
        tf = True
    else:
        tf = False

    if answer == "1" and tf == True:
        score = score + 1
    elif answer == "0" and tf == False:
        score = score + 1
    else:
        print("== GAME OVER ==")
        print("Your total score is: " + str(score))
        quit()