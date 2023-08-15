print("Welcome to the odd_int.py file.")

def odd_int_count(low, high):
    if (low % 2 == 1):
        low = low - 1
    if (high % 2 == 1):
        high = high + 1

    range = (high - low) / 2
    return range

def continue_check():
    result = input("Would you like to continue? [y/n]: ")

    if (result == 'y' or result =='Y'):
        return True
    elif (result == 'n' or result == 'N'):
        return False
    else:
        print("I'm sorry, I do not understand that input.")
        print("Resorting to default value (No).")
        return False

def run_program():
    low = int(input("Please enter a lower bound value: "))
    high = int(input("Please enter a upper bound value: "))

    print("The range of odd numbers between " + str(low) + " and " + str(high) + " is: " + str(int(odd_int_count(low, high))))
    print()

continue_program = True

while (continue_program == True):
    run_program()
    continue_program = continue_check()
    print()