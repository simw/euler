#include <stdio.h>

int main()
{
    long i, total, imax;
    
    imax = 1000;
    total = 0;
    
    for (i=0; i<imax; i++) {
        if (i%3 == 0 || i%5 == 0) {
            total += i;
        }
    }
    
    printf("\n%li\n", total);
    
    return 0;
}
