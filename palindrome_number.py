def palindrome_number(value):
    if (value == value[::-1]):
        return True
    else:
        return False

print(palindrome_number("12321"))