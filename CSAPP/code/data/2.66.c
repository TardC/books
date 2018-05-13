#include <stdio.h>

/* 
 * Generate mask indicating leftmost 1 in x. Assume w=32. 
 * For example, 0xFF00 -> 0x8000, and 0x6600 -> 0x4000.
 * If x = 0, then return 0.
 */
int leftmost_one(unsigned x)
{
    /* first, generate a mask that all bits after leftmost one are one
       e.g. 0xFF00 -> 0xFFFF, and 0x6000 -> 0x7FFF
       If x = 0, get 0 */
    x |= x >> 1;
    x |= x >> 2;
    x |= x >> 4;
    x |= x >> 8;
    x |= x >> 16;

    /* then, do mask & (~mask >> 1), reserve leftmost bit one */
    return x & (~x >> 1);
}

int main()
{
    printf("0xFF00 -> %x\n", leftmost_one(0xFF00));
    printf("0x6000 -> %x\n", leftmost_one(0x6000));
    return 0;
}
