#include "c_code.h"

void run_oi(void)
{
    int low;
    int high;

    printf("Please enter a value for the lower boundary: ");
    low = get_input();

    printf("Please enter a value for the upper boundary: ");
    high = get_input();

    printf("The amount of odd numbers between %d and %d is %d\n", low, high, get_odd_range(low, high));
    
    return;
}

int get_odd_range(int low, int high)
{
    int range;

    if (low % 2 == 1)
    {
        low = low - 1;
    }

    if (high % 2 == 1)
    {
        high = high + 1;
    }
    
    range = (high - low) / 2;

    return range;
}