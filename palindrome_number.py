def palindrome_number(value):
    if (value == value[::-1]):
        return True
    else:
        return False

print("Welcome to the palindrome_number.py file.")
number_string = input("Please enter a number value: ")

print("Is the value 12321 a palindrome: " + str(palindrome_number(number_string)))
# Add an interface, to allow for continuous checking of values.