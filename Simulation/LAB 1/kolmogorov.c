#include <stdio.h>

void swap(double *a, double *b)
{
    double temp = *a;
    *a = *b;
    *b = temp;
}

void bubble_sort(double arr[], int n)
{
    for (int i = 0; i < n - 1; i++)
    {
        for (int j = 0; j < n - i - 1; j++)
        {
            if (arr[j] > arr[j + 1])
            {
                swap(&arr[j], &arr[j + 1]);
            }
        }
    }
}

double ks_test(double data[], int n)
{
    bubble_sort(data, n);
    double d_max = 0;
    for (int i = 0; i < n; i++)
    {
        double d1 = (i + 1) / (double)n - data[i];
        double d2 = data[i] - i / (double)n;
        if (d1 > d_max)
            d_max = d1;
        if (d2 > d_max)
            d_max = d2;
    }
    return d_max;
}

int main()
{
    double data[] = {0.1, 0.3, 0.2, 0.5, 0.4};
    int n = sizeof(data) / sizeof(data[0]);
    double d = ks_test(data, n);
    printf("Kolmogorov-Smirnov D statistic: %f\n", d);
    return 0;
}
