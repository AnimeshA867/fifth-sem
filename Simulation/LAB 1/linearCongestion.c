#include <stdio.h>

void main()
{
    int x, a, c, m;
    printf("Enter the value of a:");
    scanf("%d", &a);
    printf("Enter the value of c:");
    scanf("%d", &c);
    printf("Enter the initial value of x:");
    scanf("%d", &x);
    printf("Enter the value of m:");
    scanf("%d", &m);
    printf("Starting with x= %d\n", x);
    for (int i = 0; i < 10; i++)
    {
        x = (a * x + c) % m;
        printf("%d\t", x);
    }
}