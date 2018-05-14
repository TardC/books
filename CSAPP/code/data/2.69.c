#include <stdio.h>

/*
 * Do rotating left shift. Assume 0 <= n < w
 * Examples when x = 0x12345678 and w = 32:
 *    n=4 -> 0x23456781, n=20 -> 0x67812345
 */
unsigned rotate_left(unsigned x, int n)
{
    unsigned w = sizeof(int) << 3;
    unsigned left_shift = x << n;
    /* pay attention when n == 0 */
    unsigned right_shift = x >> (w-n-1) >> 1;
    
    return left_shift | right_shift;
}

int main()
{
    unsigned test_num = 0x12345678;
    printf("n=4 -> 0x%X\n", rotate_left(test_num, 4));
    printf("n=20 -> 0x%X\n", rotate_left(test_num, 20));
    printf("n=0 -> 0x%X\n", rotate_left(test_num, 0));
    
    return 0;
}
