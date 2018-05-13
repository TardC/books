/* some useful links:
   https://zhuanlan.zhihu.com/p/25746093
   https://stackoverflow.com/questions/9133279/bitparity-finding-odd-number-of-bits-in-an-integer */
#include <stdio.h>

int odd_ones(unsigned x)
{
    x ^= x >> 16;
    x ^= x >> 8;
    x ^= x >> 4;
    x ^= x >> 2;
    x ^= x >> 1;
    x &= 0x1;
    return x;
}

int odd_ones2(unsigned x)
{
    /* $begin count bits of 1 */
    x = (x & 0x55555555) + ((x >> 1) & 0x55555555);
    x = (x & 0x33333333) + ((x >> 2) & 0x33333333);
    x = (x & 0x0f0f0f0f) + ((x >> 4) & 0x0f0f0f0f);
    x = (x & 0x00ff00ff) + ((x >> 8) & 0x00ff00ff);
    x = (x & 0x0000ffff) + ((x >> 16) & 0x0000ffff);
    /* $end count bits of 1 */

    /* if number of 1 is odd, the lsb is 1, otherwise 0 */
    x &= 0x1;
    return x;
}

int main()
{
    printf("%d\n", odd_ones(0x10101011));
    printf("%d\n", odd_ones(0x01010101));
    printf("%d\n", odd_ones2(0x10101011));
    printf("%d\n", odd_ones2(0x01010101));
    return 0;
}
