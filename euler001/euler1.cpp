#include <iostream>

int main()
{
    int total = 0;

    for (int i=0; i<1001; i++)
        if (i % 3 == 0 || i % 5 == 0)
            total += i;

    std::cout << total << std::endl;
}
