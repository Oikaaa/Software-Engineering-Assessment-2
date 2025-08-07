#--------------Phan 7-------------------

high_score = [56, 78, 67, 80, 29, 48]

print("High scores")
for i in range(len(high_score)):
    print(f"{i + 1}. {high_score[i]}")

new_score = int(input("Input new score: "))
high_score.append(new_score)
print("High scores")
for i in range(len(high_score)):
    print(f"{i + 1}. {high_score[i]}")

#--------------Phan 8-------------------

for i in range(len(high_score)):
    for j in range(len(high_score) - i -1):
        if high_score[j + 1] > high_score[j]:
            high_score[j], high_score[j + 1] = high_score[j+1], high_score[j]
print(high_score)

for i in range(0, 5):
    print(f"{i + 1}. {high_score[i]}")