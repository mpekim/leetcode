#ifndef C_CODE_H_
#define C_CODE_H_

#include <stdio.h>
#include <stdlib.h>

enum bool
{
    FALSE,
    TRUE
};

typedef enum bool Bool;

int get_input_int(void);
char get_input_char(void);
void present_choice_menu(void);
Bool continue_program(void);
void clear_keyboard_buffer(void);
// Barebones functions used throughout all programs.

void run_oi(void);
int get_odd_range(int low, int high);
// Declarations for odd_int.c

void run_pn(void);
Bool check_palindrome(int number);
char* create_num_string(int number);
// Declarations for palindrome_number.c

void run_ts(void);
int* create_int_list(void);
int* get_two_sum(int* list, int sum, int size);
// Declarations for two_sum.c

// Declarations for num_stud_ute.c

#endif // C_CODE_H_