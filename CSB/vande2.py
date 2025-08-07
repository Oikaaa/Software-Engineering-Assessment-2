students = [1, 1, 0, 0]
sandwiches = [0, 1, 0, 1]

false_student = [1, 1, 1, 0, 0, 1]
false_sandwich = [1, 0, 0, 0, 1, 1]

def cafeteria_problem (students, sandwiches):
    i = 0
    for i in range(len(students)**len(sandwiches)):
        try:
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
            else:
                popped = students.pop(0)
                students.append(popped)
            i += 1
        except:
            break
    return len(students)

print(cafeteria_problem(students, sandwiches))