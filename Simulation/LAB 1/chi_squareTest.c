#include <stdio.h>
#include <math.h>

#define SIZE 5

double chiSquareTest(int observed[], int expected[], int size)
{
    double chiSquare = 0;
    for (int i = 0; i < size; i++)
    {
        chiSquare += pow(observed[i] - expected[i], 2) / expected[i];
    }
    return chiSquare;
}

int main()
{
    int observed[SIZE] = {10, 15, 20, 25, 30};
    int expected[SIZE] = {15, 15, 20, 25, 25};
    double chiSquare = chiSquareTest(observed, expected, SIZE);
    printf("Chi-Square Value: %lf\n", chiSquare);
    return 0;
}
