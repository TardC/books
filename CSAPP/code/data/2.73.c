#include <stdio.h>
#include <limits.h>

/* Addition that saturates to TMin or TMax */
int saturating_add(int x, int y)
{
    int sum = x + y;
    int sig_mask = INT_MIN;
    /* if x > 0, y > 0, but sum < 0, it's a positive overflow
       if x < 0, y < 0, but sum >= 0, it's a negative overflow */
    int pos_over = !(x & sig_mask) && !(y & sig_mask) && (sum & sig_mask);
    int neg_over = (x & sig_mask) && (y & sig_mask) && !(sum & sig_mask);

    (pos_over && (sum = INT_MAX) || neg_over && (sum = INT_MIN));

    return sum;
}

int main()
{
    printf("%d %d\n", INT_MAX, saturating_add(INT_MAX, 1));
    printf("%d %d\n", INT_MIN, saturating_add(INT_MIN, -1));

    return 0;
}
