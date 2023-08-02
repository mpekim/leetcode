print("Welcome to the palindrome_number.py file.")

def palindrome_number(value):
    if (value == value[::-1]):
        return True
    else:
        return False

print("Is the value 12321 a palindrome:" + palindrome_number("12321"))