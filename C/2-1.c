#include <stdio.h>
#include <math.h>

int limit = 4000000;

int main()
{
    int sum = 0;
    int a = 1;
    int b = 1;
    int c = a+b;

    while (c < limit)
    {
        sum += c;
        a = b+c;
        b = c+a;
        c = a+b;
    }

    printf("Result: %i", sum);
    return 0;
}
