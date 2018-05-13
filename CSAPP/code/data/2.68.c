#include <stdio.h>

/*
 * Mask with least significant n bits set to 1
 * Examples: n = 6 --> 0x3F, n = 17 --> 0x1FFFF
 * Assume 1 <= n <= w
 */
int lower_one_mask(int n)
{
    int w = sizeof(int) << 3;
    return ((unsigned) -1) >> (w-n);
}

int main()
{
    printf("6 --> 0x%X\n", lower_one_mask(6));
    printf("17 --> 0x%X\n", lower_one_mask(17));
    return 0;
}
