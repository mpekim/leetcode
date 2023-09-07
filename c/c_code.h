#include <stdio.h>
#include <stdlib.h>

enum bool
{
    FALSE,
    TRUE
};

typedef enum bool Bool;

int get_input(void);

void clear_keyboard_buffer(void);
// Barebones functions used throughout all programs.

int get_odd_range(int low, int high);
// Declarations for odd_int.c

Bool check_palindrome(int number);
char* create_num_string(int number);
// Declarations for palindrome_number.c

int* get_two_sum(int* list, int sum);
// Declarations for two_sum.c