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

int main()
{
    printf("%d\n", odd_ones(0x10101011));
    printf("%d\n", odd_ones(0x01010101));
    return 0;
}
