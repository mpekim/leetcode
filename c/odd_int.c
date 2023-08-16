# include <stdio.h>

void clear_keyboard_buffer(void);

int get_odd_range(int low, int high);

int main(int argc, char* argv[])
{
    int low;
    int high;

    printf("Please enter a value for the lower bound: ");
    low = scanf("%c", &low);

    clear_keyboard_buffer();

    printf("Please enter a value for the upper bound: ");
    high = scanf("%c", &high);

    clear_keyboard_buffer();

    printf("The amount of odd numbers between %d and %d is: %d\n", low, high, range);

    return 0;
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

void clear_keyboard_buffer(void)
{
    char c;
    do{
        scanf("%c", &c);
    } while (c != "\n");
}