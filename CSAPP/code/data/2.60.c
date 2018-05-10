/* $begin replace_byte */
#include <stdio.h>

typedef unsigned char *byte_pointer;

unsigned replace_byte(unsigned x, int i, unsigned char b)
{
    unsigned tmp = x;
    byte_pointer start = (byte_pointer) &tmp;
    start[i] = b;

    return tmp;
}
/* $end replace_byte */

int main()
{
    printf("replace_byte(0x12345678, 2, 0xAB) --> 0x%X\n",
            replace_byte(0x12345678, 2, 0xAB));
    printf("replace_byte(0x12345678, 0, 0xAB) --> 0x%X\n",
            replace_byte(0x12345678, 0, 0xAB));
}
