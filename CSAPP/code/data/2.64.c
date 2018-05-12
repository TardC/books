#include <stdio.h>

/* Return 1 when any odd bit of x equals 1; 0 otherwise.
   Assume w=32 */
int any_odd_one(unsigned x)
{
    unsigned mask = 0xAAAAAAAA;
    return !((mask & x) ^ mask);
}

int main()
{
    unsigned test_num1 = 0xFFFFFFFF;
    unsigned test_num2 = 0x00000000;

    printf("%d %d\n", any_odd_one(test_num1), any_odd_one(test_num2));
}
