/*
 * A: !~x
 * B: !x
 * C: !~(x | ~0xFF)
 * D: !((x >> ((sizeof(int)-1) << 3)) & 0xff)
 */
#include <stdio.h>

int is_all_bit_one(int x)
{
    return !~x;
}

int is_all_bit_zero(int x)
{
    return !x;
}

/* $begin is_least_significant_byte_one */
int is_lsb_one(int x)
{
    return is_all_bit_one(x | ~0xFF);
}
/* $end is_least_significant_byte_one */

/* $begin is_most_significant_byte_zero */
int is_msb_zero(int x)
{
    return is_all_bit_zero((x >> ((sizeof(int)-1) << 3)) & 0xFF);
}
/* $end is_most_significat_byte_zero */

int main()
{
    int x = ~0x00;
    printf("%d\n", is_all_bit_one(x));
    x = 0x00;
    printf("%d\n", is_all_bit_zero(x));
    x = 0xFF;
    printf("%d\n", is_lsb_one(x));
    x = 0x00;
    printf("%d\n", is_msb_zero(x));

    return 0;
}
