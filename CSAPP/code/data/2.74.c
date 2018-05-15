#include <stdio.h>
#include <limits.h>

/* Determine whether arguments can be subtracted without overflow */
int tsub_ok(int x, int y)
{
    /* if x > 0, y < 0, x - y < 0, positive overflow
       if x < 0, y > 0, x - y > 0, negative overflow */
    int sum = x - y;
    /* when y = INT_MIN, x = 0, positive overflow too */
    int pos_over = x >= 0 && y < 0 && sum < 0;
    int neg_over = x < 0 && y > 0 && sum > 0;

    return !(pos_over || neg_over);
}

int main()
{
    printf("%d\n", tsub_ok(0, INT_MIN));
    printf("%d\n", tsub_ok(1, INT_MIN));
    printf("%d\n", tsub_ok(-1, INT_MIN));
    return 0;
}
