#include "c_code.h"

Bool check_palindrome(int number)
{
    // First, convert the number into a string.
    char* num_string;

    int number;

    num_string = create_num_string(number);

    printf("Please enter a value for the number to be checked: ");
    number = get_input_int();

    return FALSE;
}

char* create_num_string(int number)
{
    char* num_string;
    num_string = (char*)malloc(sizeof(char) * 9);

    if (num_string == NULL)
    {
        printf("Error: unable to allocate memory for number string. Ending program...\n");
        exit(1);
    }

    for (int i = 0; i < 9; i++)
    {
        num_string[i] = '0';
    }
    //  Set up the string to be "empty"
    // (only containing zeroes).

    return num_string;
}