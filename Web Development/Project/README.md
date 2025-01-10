# Calculator Application

This repository contains the code for a calculator application implemented in JavaScript. The calculator is designed to handle basic arithmetic operations along with advanced functions such as trigonometric, logarithmic, and factorial calculations.

## Features

- **Basic Arithmetic**: Addition, subtraction, multiplication, division.
- **Trigonometric Functions**: Sine, cosine, tangent with angle input in degrees.
- **Logarithmic Functions**: Logarithm base 10 (`log`) and natural logarithm (`ln`).
- **Factorial**: Calculation of the factorial of non-negative integers.
- **Square Root**: Calculation of the square root of a number.
- **Absolute Value**: Calculation of the absolute value of a number.
- **Error Handling**: The calculator checks for errors such as invalid input, unbalanced parentheses, and domain errors (e.g., factorial of a negative number).

## Functions

### `display1(val)`

- Handles the initial display of values in the input field (`expression1`).
- Checks if the current input requires multiplication (implicit multiplication handling).
- Calls `display2` and `display3` to handle updates to `expression1` and `expression2`.

### `display2(val)`

- Manages the updates to the `expression1` field, ensuring no invalid or conflicting inputs are entered.
- Handles clearing of the display when necessary.

### `display3(val)`

- Updates the internal expression string (`expression2`) which is used for computation.
- Similar to `display2`, it ensures proper input management and clears if necessary.

### `solve()`

- The core function for evaluating the expression.
- Handles special cases such as factorials, square roots, trigonometric functions, logarithms, and absolute value.
- Checks for errors and ensures proper handling of expressions with parentheses.
- Updates the `history` field with each calculated result.

### `checkBalancedParentheses(str)`

- A utility function that checks for balanced parentheses in the expression.
- Returns:
  - `0` if closing bracket is used before an opening bracket.
  - `1` if parentheses are not balanced.
  - `2` if parentheses are balanced.

## Error Handling

The calculator performs several checks to ensure valid input and expressions:

- **Factorial**: Only non-negative integers are allowed. If a factorial of a non-integer or negative number is attempted, an error is displayed.
- **Trigonometric Functions**: Checks for undefined cases, such as the tangent of 90°.
- **Logarithmic Functions**: Ensures the input is within the domain of the logarithm.
- **Balanced Parentheses**: Ensures all parentheses in the expression are balanced and valid.

## Usage

1. Enter values and operations using the calculator interface.
2. The calculator automatically handles implicit multiplication, such as between a number and a function.
3. Click the `=` button to evaluate the expression.
4. The result is displayed, and the calculation history is updated.
5. Errors are displayed if the input is invalid or the calculation cannot be performed.

## Known Issues

- The calculator currently uses `eval()` for expression evaluation, which may pose security risks if user input is not properly sanitized. Consider refactoring to use a safer method of evaluating expressions.
