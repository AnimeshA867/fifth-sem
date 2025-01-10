#include <stdio.h>

int main()
{
    // Initial values
    double previousYearValue = 80;
    int numberOfYears = 5;
    double growthRates[] = {20, 25, 30, 35, 40};

    printf("Year\tConsumption\n");

    for (int year = 1; year <= numberOfYears; year++)
    {
        // Calculate values for current year
        double investment = 2 + 0.1 * previousYearValue;
        double totalValue = 45.45 + 2.27 * (investment + growthRates[year - 1]);
        double tax = 0.2 * totalValue;
        double consumption = 20 + 0.7 * (totalValue - tax);

        // Print the results
        printf("%d\t%.2f\n", year, consumption);

        // Update value for next year
        previousYearValue = totalValue;
    }

    return 0;
}