#include <stdio.h>

int main (void)
{
    long int n = 600851475143;
    int factor = 2;
    int lastFactor = 1;
    while (n > 1)
    {
        if (n % factor == 0)
        {
            lastFactor = factor;
            n = n / factor;
            while (n % factor == 0)
                n = n / factor;

        }
        factor++;
    }
    printf("%i", lastFactor);
}
