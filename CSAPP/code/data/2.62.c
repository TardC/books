/* $begin int_shifts_are_arithmetic */
#include <stdio.h>

int int_shifts_are_arithmetic()
{
    int test_num = -1;
    int shift_val = sizeof(int) << 3;

   return !!(test_num >> shift_val);
}

int int_shifts_are_arithmetic2()
{
    int num = -1;
    return !(num ^ (num >> 1));
}
/* $end int_shifts_are_arithmetic */

int main()
{
    printf("%d\n", int_shifts_are_arithmetic());

    return 0;
}
