#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void roll_dice(int rolls)
{
    int counts[6] = {0};

    for (int i = 0; i < rolls; i++)
    {
        int result = rand() % 6 + 1;
        counts[result - 1]++;
    }

    for (int i = 0; i < 6; i++)
    {
        printf("Face %d: %d times\n", i + 1, counts[i]);
    }
}

int main()
{
    int rolls;

    printf("Enter the number of dice rolls: ");
    scanf("%d", &rolls);

    srand(time(NULL));

    roll_dice(rolls);

    return 0;
}
