#include <stdio.h>
#include <limits.h>

/* code from 2.78.c
   Divide by power of 2. Assume 0 <= k < w-1 */
int divide_power2(int x, int k)
{
    int is_neg = x & INT_MIN;
    (is_neg && (x = x + (1 << k) -1));
    return x >> k;
}

int mul3div4(int x)
{
    int mul3 = (x << 1) + x;
    return divide_power2(mul3, 2);
}

int main()
{
    int x = 0x12345678;
    printf("%d %d\n", mul3div4(x), x*3/4);

    return 0;
}
