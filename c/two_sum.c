#include "c_code.h"

void run_ts(void)
{
    print("Welcome to the Two Sum program.\n");
    int size;
    int sum;

    printf("Please enter a value for the size of the list: ");
    size = get_input();

    int* list = create_new_list(size);

    printf("Please enter a value for the sum to be found: ");
    sum = get_input();

    int solution[] = get_two_sum(list, sum, size);

    return;
}

int* create_int_list(int size)
{
    int* new_list;

    new_list = (int*)malloc(sizeof(int) * size);

    if (new_list == NULL)
    {
        printf("Error: unable to allocate memory for list. Ending program...\n");
        exit(1);
    }

    for (int i = 0; i < size; i++)
    {
        printf("Please enter a value for list item %d: ", (i + 1));
        new_list[i] = get_input();
    }

    return new_list;
}

int* get_two_sum(int* list, int sum, int size)
{
    int solution[] = {-1, -1};

   for (int i = 0; i < size; i++)
   {
        for (int j = i; j < size; j++)
        {
            if (list[i] + list[j] == sum)
            {
                printf("Solution found.\n");
                solution[0] = i;
                solution[1] = j;

                return solution;
            }
        }
   }
   printf("Error: solution not found.\n");

   return solution;
}