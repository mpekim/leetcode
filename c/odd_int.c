#include "c_code.h"

void run_oi(void)
{
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