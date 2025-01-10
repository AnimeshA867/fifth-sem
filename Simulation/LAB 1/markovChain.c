#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define NUM_STATES 3
#define NUM_STEPS 10

// Function to get the next state based on transition probabilities
int getNextState(int currentState, double transitionMatrix[NUM_STATES][NUM_STATES])
{
    double randVal = (double)rand() / RAND_MAX;
    double cumulativeProb = 0.0;

    for (int nextState = 0; nextState < NUM_STATES; nextState++)
    {
        cumulativeProb += transitionMatrix[currentState][nextState];
        if (randVal < cumulativeProb)
        {
            return nextState;
        }
    }

    return NUM_STATES - 1; // In case of rounding errors
}

int main()
{
    srand(time(NULL));

    // Define the transition matrix
    double transitionMatrix[NUM_STATES][NUM_STATES] = {
        {0.1, 0.6, 0.3},
        {0.4, 0.4, 0.2},
        {0.7, 0.2, 0.1}};

    int currentState = 0; // Initial state

    printf("Initial State: %d\n", currentState);

    for (int step = 0; step < NUM_STEPS; step++)
    {
        currentState = getNextState(currentState, transitionMatrix);
        printf("Step %d: %d\n", step + 1, currentState);
    }

    return 0;
}
