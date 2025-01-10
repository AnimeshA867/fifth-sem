#include <stdio.h>
#include <stdlib.h>

void poker_test(int numbers[], int n, int digits)
{
    int frequencies[10] = {0};

    for (int i = 0; i < n; i++)
    {
        int num = numbers[i];
        while (num > 0)
        {
            frequencies[num % 10]++;
            num /= 10;
        }
    }

    printf("Digit Frequencies:\n");
    for (int i = 0; i < 10; i++)
    {
        printf("%d: %d\n", i, frequencies[i]);
    }
}

int main()
{
    int numbers[] = {123, 234, 345, 456, 567, 678, 789, 890, 901};
    int n = sizeof(numbers) / sizeof(numbers[0]);

    poker_test(numbers, n, 3); // Three-digit
    poker_test(numbers, n, 4); // Four-digit (if applicable)

    return 0;
}
