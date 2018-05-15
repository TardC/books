/*
 * A: The size_t type is usually unsigned.
 *    When signed and unsigned numbers are calculated together, 
 *    signed number is first converted to unsigned number, and
 *    the result is also unsigned, so it always >= 0.
 */
#include <stdio.h>
#include <string.h>

void copy_int(int val, void *buf, int maxbytes)
{
    if (maxbytes >= (int) sizeof(val))
        memcpy(buf, (void *) &val, sizeof(val));
}

int main()
{
    int buf;

    copy_int(42, (void *) &buf, sizeof(int));
    printf("%d\n", buf);
    return  0;
}
