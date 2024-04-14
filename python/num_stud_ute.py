def unable_to_eat():
    students = [0,1,0,1]
    sandwiches = [1,0,1,1]
    # Basic format. Change to allow for user input.

    total = len(students)
    top = sandwiches[0]
    eat = 0

    while (students.count(top) > 0):
        if (students[0] == top):
            eat = eat + 1
            students.pop(0)
            sandwiches.pop(0)
        else:
            students.append(students.pop(0))
        
        if (len(sandwiches) > 0):
            top = sandwiches[0]

        else:
            break
    return int(total - eat)