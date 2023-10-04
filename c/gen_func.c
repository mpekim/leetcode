# include "c_code.h"

int get_input(void)
{
    int input;
    int num_of_conversions;

    num_of_conversions = scanf("%d", &input);
    clear_keyboard_buffer();

    while (num_of_conversions != 1)
    {
        printf("I'm sorry, I do not understand that input. Please try again.\n");
        num_of_conversions = scanf("%d", &input);
        clear_keyboard_buffer();
    }

    return input;
}

void clear_keyboard_buffer(void)
{
    char c;
    do{
        scanf("%c", &c);
    } while (c != '\n');
    return;
}