#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>

void *calloc2(size_t nmemb, size_t size)
{
    if (nmemb == 0 || size ==0)
        return NULL;

    size_t buf_size = nmemb * size;
    /* a good way to check overflow or not */
    if (nmemb == buf_size / size) {
        void *ptr = malloc(buf_size);
        memset(ptr, 0, buf_size);
        return ptr;
    }

    return NULL;
}

int main()
{
    void *p;
    p = calloc2(2, 4);
    printf("%d\n", p == NULL);
    free(p);

    p = calloc2(SIZE_MAX, 2);
    printf("%d\n", p == NULL);
    free(p);

    return 0;
}
