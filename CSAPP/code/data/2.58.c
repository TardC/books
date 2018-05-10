/* $begin is_little_endian */
#include <stdio.h>
/* $end is_little_endian */
#include <assert.h>

/* $begin is_little_endian */
typedef unsigned char *byte_pointer;

int is_little_endian()
{
    int test_num = 0xFF;
    byte_pointer byte_start = (byte_pointer) &test_num;

    if (byte_start[0] == 0xFF)
        return 1;
    return 0;
}
/* $end is_little_endian */

int main()
{
    assert(is_little_endian());
    return 0;
}
