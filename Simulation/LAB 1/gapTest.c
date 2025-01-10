#include <stdio.h>
#include <stdlib.h>

void gap_test(int numbers[], int n, int low, int high)
{
    int gap = 0;
    int gaps[100] = {0}; // Assuming max 100 gaps

    for (int i = 0; i < n; i++)
    {
        if (numbers[i] >= low && numbers[i] <= high)
        {
            if (gap < 100)
            {
                gaps[gap]++;
            }
            gap = 0;
        }
        else
        {
            gap++;
        }
    }

    printf("Gap lengths:\n");
    for (int i = 0; i < 100; i++)
    {
        if (gaps[i] > 0)
        {
            printf("Length %d: %d\n", i, gaps[i]);
        }
    }
}

int main()
{
    int numbers[] = {1, 4, 5, 2, 6, 3, 4, 7, 1, 3, 5, 8, 2};
    int n = sizeof(numbers) / sizeof(numbers[0]);

    gap_test(numbers, n, 2, 5);

    return 0;
}
