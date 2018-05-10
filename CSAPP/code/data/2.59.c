/* 
 * The expression is:
 * (x & 0xFF) | (y & ~0xFF)
 */
#include <stdio.h>
#include <assert.h>

int main()
{
    unsigned mask = 0xFF;
    unsigned x = 0x89ABCDEF;
    unsigned y = 0x76543210;

    unsigned res = (x & mask) | (y & ~mask);
    assert(res == 0x765432EF);

    return 0;
}
