#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void monte_carlo_dice(int games)
{
    int counts[6] = {0};

    for (int i = 0; i < games; i++)
    {
        int result = rand() % 6 + 1;
        counts[result - 1]++;
    }

    for (int i = 0; i < 6; i++)
    {
        printf("Face %d: %d times (%.2f%%)\n", i + 1, counts[i], (counts[i] / (double)games) * 100);
    }
}

int main()
{
    int games;

    printf("Enter the number of games to simulate: ");
    scanf("%d", &games);

    srand(time(NULL));

    monte_carlo_dice(games);

    return 0;
}
