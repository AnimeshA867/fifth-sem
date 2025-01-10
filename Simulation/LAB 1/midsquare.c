#include <stdio.h>
#include <math.h>

int extractMiddle(int number, int digits)
{
    int totalDigits = (int)log10(number) + 1;    // Total number of digits in the squared number
    int dropDigits = (totalDigits - digits) / 2; // Number of digits to drop from the beginning and end

    int divisor = pow(10, dropDigits);
    int result = (number / divisor) % (int)pow(10, digits);

    return result;
}

void midSquareMethod(int seed, int numDigits, int numRandoms)
{
    int current = seed;

    for (int i = 0; i < numRandoms; i++)
    {
        int square = current * current;
        current = extractMiddle(square, numDigits);

        printf("Random Number %d: %d\n", i + 1, current);
    }
}

int main()
{
    int seed;       // Initial seed value
    int numDigits;  // Number of digits to extract (should be appropriate to the seed value)
    int numRandoms; // Number of random numbers to generate

    printf("Enter the seed value:");
    scanf("%d", &seed);
    printf("Enter the number of digits:");
    scanf("%d", &numDigits);
    printf("Enter the number of random numbers:");
    scanf("%d", &numRandoms);

    midSquareMethod(seed, numDigits, numRandoms);

    return 0;
}
