/*
 * A: This function can't extract a negative number byte from word
 */
#include <stdio.h>

/* Declaration of data type where 4 bytes are packed
   into an unsigned */
typedef unsigned packed_t;

/* Extract byte from word. Return as signed integer */
int xbyte(packed_t word, int bytenum)
{
    int size = sizeof(packed_t);
    /* after shift left word of shift_left_val, the byte
       that bytenum specified will be most siginificant byte */
    int shift_left_val = (size-1-bytenum) << 3;
    /* then shift right word of shift_right_val, the byte
       that bytenum specified will be least siginificant byte.
       using arithemetic shift, word is we want */
    int shift_right_val = (size-1) << 3;

    return (int) word << shift_left_val >> shift_right_val;
}

int main()
{
    printf("%d\n", xbyte(0xFFFFFFFF, 0));
    return 0;
}
