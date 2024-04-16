import odd_int as oi
import palindrome_number as pn
import two_sum as ts
import num_stud_ute as nsu

program_continue = True

while (program_continue == True):

    print("Welcome to the main module of Python Leetcode.")
    print("1. Odd Int")
    print("2. Palindrome Number")
    print("3. Two Sum")

    menu_choice = int(input("Please enter a choice of program to run: "))
    
    if (menu_choice == 1):
        oi.run_program()
    elif (menu_choice == 2):
        pn.run_program()
    elif (menu_choice == 3):
        ts.run_program()
    else:
        print("I'm sorry, I do not understand that input. Ending program.")
        program_continue = False
    
    program_continue = pn.continue_check()