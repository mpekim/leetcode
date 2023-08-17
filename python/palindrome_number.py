#print("Welcome to the palindrome_number.py file.")

def palindrome_number(value):
    if (value == value[::-1]):
        return True
    else:
        return False

def run_program():
    number_string = input("Please enter a number value: ")

    print("Is the value " + number_string + " a palindrome: " + str(palindrome_number(number_string)))
    print()

def continue_check():
    result = input("Would you like to continue? [y/n]: ")

    if (result == 'y' or result == 'Y'):
        return True
    elif (result == 'n' or result ==' N'):
        return False
    else:
        print("I'm sorry, I do not understand that input.")
        print("Resorting to default value (No).")
        print()

"""continue_program = True

while (continue_program == True):
    run_program()
    continue_program = continue_check()"""