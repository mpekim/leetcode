# include "c_code.h"

int get_input_int(void)
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

char get_input_char(void)
{
    char input;
    int num_of_conversions;

    num_of_conversions = scanf("%c", &input);
    clear_keyboard_buffer();

    while (num_of_conversions != 1)
    {
        printf("I'm sorry, I do not understand that input. Please try again.\n");
        num_of_conversions = scanf("%d", &input);
        clear_keyboard_buffer();
    }

    return input;
}

void present_choice_menu(void)
{
    printf("1. Odd Int\n");
    printf("2. Palindrome Number\n");
    printf("3. Two Sum\n");

    return;
}

Bool continue_program(void)
{
    char choice;

    printf("Do you want to continue? [y/n]: ");
    choice = get_input_char();

    switch(choice)
    {
        case 'n':
        case 'N':
            return FALSE;
            break;
        case 'y':
        case 'Y':
            return TRUE;
            break;
        default:
            print("I'm sorry, I do not understand that input.\n");
            printf("Resorting to default value (N).\n");
            return FALSE;
            break;
    }
}

void clear_keyboard_buffer(void)
{
    char c;
    do{
        scanf("%c", &c);
    } while (c != '\n');
    return;
}