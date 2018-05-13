/*
 * A: If the value of the right operand is negative or is greater than or
      equal to the width of the promoted left operand, the behavior is
      undefined. Meanwhile, in Java, k = k mod w.
 */
#include <stdio.h>

int int_size_is_32()
{
    /* Set most significant bit (msb) of 32-bit machine */
    int set_msb = 1 << 31;
    /* Shift past msb of 32-bit word */
    int beyond_msb = set_msb << 1;

    /* set_msb is nonzero when word size >= 32
       beyond_msb is zero when word size <= 32 */
    return set_msb && !beyond_msb;
}

int int_size_is_32_for_16bit()
{
    int set_msb = 1 << 15 << 1 << 15;
    int beyond_msb = set_msb << 1;

    return set_msb && !beyond_msb;
}

int main()
{
    printf("%d %d\n", int_size_is_32(), int_size_is_32_for_16bit());
    return 0;
}
