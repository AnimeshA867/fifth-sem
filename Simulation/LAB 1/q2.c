#include <stdio.h>
#include <stdlib.h>
#include <time.h>

double monte_carlo_circumference(int points)
{
    int inside_circle = 0;

    for (int i = 0; i < points; i++)
    {
        double x = (double)rand() / RAND_MAX;
        double y = (double)rand() / RAND_MAX;

        if (x * x + y * y <= 1)
        {
            inside_circle++;
        }
    }

    double pi_estimate = (inside_circle / (double)points) * 4;
    return pi_estimate * 2; // Circumference of unit circle = 2 * pi
}

int main()
{
    int points;

    printf("Enter the number of random points to generate: ");
    scanf("%d", &points);

    srand(time(NULL));

    double circumference = monte_carlo_circumference(points);
    printf("Estimated Circumference: %f\n", circumference);

    return 0;
}
