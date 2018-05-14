#include <stdio.h>

/*
 * Return 1 when x can be represented as an n-bit, 2's-complement
 * number; 0 otherwise
 * Assume 1 <= n <= w
 */
int fits_bits(int x, int n)
{
    /* note that x is represented as n-bit, 2's-complement number,
       the most significant bit is -2^(n-1), so when n=4, the maximun
       is 7, the min is -8.
       
       if x can be represented as n-bit, 2's-complement number,
       when x > 0, after x >>= (n-1), x = 0. That is 0x0000 if x is 16-bit;
       when x < 0, after x >>= (n-1), x = -1. That is 0xFFFF if x is 16-bit */
    x >>= (n-1);
    return !x || !~x;
}

int main()
{
    printf("%d %d\n", fits_bits(4, 3), fits_bits(4, 4));
    printf("%d %d\n", fits_bits(-3, 2), fits_bits(-3, 3));
    return 0;
}
