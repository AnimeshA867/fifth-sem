#include <stdio.h>

double auto_correlation(double data[], int n, int lag)
{
    double mean = 0;
    for (int i = 0; i < n; i++)
    {
        mean += data[i];
    }
    mean /= n;

    double numerator = 0;
    double denominator = 0;
    for (int i = 0; i < n - lag; i++)
    {
        numerator += (data[i] - mean) * (data[i + lag] - mean);
    }
    for (int i = 0; i < n; i++)
    {
        denominator += (data[i] - mean) * (data[i] - mean);
    }

    return numerator / denominator;
}

int main()
{
    double data[] = {0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9};
    int n = sizeof(data) / sizeof(data[0]);
    int lag = 1;

    double result = auto_correlation(data, n, lag);
    printf("Auto-Correlation Result: %f\n", result);

    return 0;
}
