def two_sum(list, sum):
    for i in list:
        for j in list:
            if (i + j == sum):
                return [i, j]
    return "Sum not found"

def run_program():
    print("Welcome to the two_sum.py file.")

    list_size = int(input("Please enter a value for the size of the list: "))
    
    num_list = []

    for i in range(0, list_size):
        num_list.append(0)

    for i in range(0, list_size):
        num_list[i] = int(input("Please enter a value: "))

    sum = int(input("Please enter a value for the sum to be found: "))

    print("Determining if desired sum occurs within list...")

    print(two_sum(num_list, sum))
    print("")
    
def continue_check():
    result = input("Would you like to continue? [y/n]: ")

    if (result == 'y' or result == 'Y'):
        return True
    elif (result == 'n' or result =='N'):
        return False
    else:
        print("I'm sorry, I do not understand that output.")
        print("Resorting to default value (No)")
        return False

program_continue = True

while (program_continue == True):
    run_program()
    program_continue = continue_check()
    print("")