print("Welcome to the odd_int.py file.")

def odd_int_count(low, high):
    if (low % 2 == 1):
        low = low - 1
    if (high % 2 == 1):
        high = high + 1

    range = (high - low) / 2
    return range

low = int(input("Please enter a lower bound value: "))
high = int(input("Please enter a upper bound value: "))

print("The range of odd numbers between " + str(low) + " and " + str(high) + " is: " + str(int(odd_int_count(low, high))))