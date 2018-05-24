#include <stdio.h>
#include <limits.h>

int threefourths(int x)
{
    int is_neg = x & INT_MIN;
    int h = x & ~0x3;
    int l = x & 0x3;

    int hd4 = h >> 2;
    int hd4m3 = (hd4 << 1) + hd4;

    int lm3 = (l << 1) + l;
    int bias = (1 << 2) - 1;
    (is_neg && (lm3 += bias));
    int lm3d4 = lm3 >> 2;

    return hd4m3 + lm3d4;
}

int main()
{
    printf("%d %d\n", threefourths(8), 6);
    printf("%d %d\n", threefourths(10), 7);

    printf("%d %d\n", threefourths(-8), -6);
    printf("%d %d\n", threefourths(-10), -7);

    return 0;
}
