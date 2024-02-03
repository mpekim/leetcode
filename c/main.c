# include "c_code.h"

int main(int argc, char* argv[])
{
    // Driver for all files.
    do{
        int choice;
        int num_of_conversions = 0;

        printf("Welcome to the Leetcode C-interface.\n");
        print("Please enter the program that you would like to run: ");
        present_choice_menu();
        choice = get_input();

    while(num_of_conversions != 1)
    {
        printf("I'm sorry, I do not understand that input. Please try again.");
        printf("Please enter the program that you would like to run: ");
        present_choice_menu();
        choice = get_input();
    }

        switch(choice)
        {
            case 1:
                run_oi();
                break;
            case 2:
                run_pn();
                break;
            case 3:
                run_ts();
                break;
            default:
                printf("I'm sorry, I don't understand that input.\n");
                break;
        }
    } while (continue_program() == TRUE);

    return 0;
}