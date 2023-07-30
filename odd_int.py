print("Welcome to the oddInt.py file.")

def odd_int_count(low, high):
    if (low % 2 ==0):
        low = low - 1
    if (high % 2 == 0):
        high = high + 1

    range = (high - low) / 2
    return range

low = int(input("Please enter a lower bound value: "))
high = int(input("Please enter a upper bound value: "))

print("The range of odd numbers between " + low + " and " + high + " is: " + odd_int_count(low, high))