#include <stdio.h>

unsigned srl(unsigned x, int k)
{
    /* Perform shift arithmetically */
    unsigned xsra = (int) x >> k;

    int w = sizeof(int) << 3;
    int mask = ~(-1 << (w-k));
    return xsra & mask;
}

int sra(int x, int k)
{
    /* Perform shift logically */
    int xsrl = (unsigned) x >> k;

    int w = sizeof(int) << 3;
    int mask = -1 << (w-k);
    if (x < 0)
        return xsrl | mask;
    return xsrl;
}

int main()
{
    unsigned test_num = 0x87654321;
    int test_num2 = (int) test_num;
    printf("%.8x %.8x\n", test_num >> 4, srl(test_num, 4));
    printf("%.8x %.8x\n", test_num2 >> 4, sra(test_num2, 4));
}
