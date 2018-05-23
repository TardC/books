#include <stdio.h>
#include <limits.h>

/* Divide by power of 2. Assume 0 <= k < w-1 */
int divide_power2(int x, int k)
{
    int is_neg = x & INT_MIN;
    (is_neg && (x = x + (1 << k) -1));
    return x >> k;
}

int main()
{
    int x = 0xFFFF1234;
    printf("%d\n", x);
    printf("%d %d\n", divide_power2(x, 2), x/4);

    return 0;
}
