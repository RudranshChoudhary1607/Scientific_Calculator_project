# Project Statement: Scientific Calculator

## 1. Project Title

**Scientific Calculator Using Python (Terminal-Based)**

## 2. Problem Statement

Students and other users frequently need to perform mathematical calculations involving arithmetic, trigonometry, logarithms, roots, powers, and factorials. Performing these calculations manually can take time and may lead to errors. A scientific calculator program can provide a convenient way to perform these operations accurately through a simple text-based interface.

The aim of this project is to develop a menu-driven scientific calculator using Python. The application will run in a terminal and will not require a graphical user interface or third-party libraries.

## 3. Objectives

The main objectives are:

1. To implement common arithmetic operations.
2. To provide scientific functions such as trigonometry, logarithms, roots, powers, and factorials.
3. To support degree and radian modes for trigonometric calculations.
4. To validate user input and handle common mathematical errors.
5. To maintain a record of calculations during the current session.
6. To demonstrate the use of Python functions, classes, loops, conditionals, exception handling, and the standard library.

## 4. Scope of the Project

The calculator supports the following operations:

- Addition, subtraction, multiplication, division, modulus, and exponentiation.
- Sine, cosine, tangent, and their inverse functions.
- Natural logarithm, base-10 logarithm, and logarithm with a custom base.
- Square root and cube root.
- Factorial, absolute value, exponential function, square, and reciprocal.
- Display of the constants π and *e*.
- Degree/radian mode selection.
- Session-based calculation history.

The application is intended for educational and general mathematical use. It is not designed for symbolic algebra, complex scientific workflows, or safety-critical calculations.

## 5. Proposed Methodology

The program uses a menu-driven approach:

1. Display the main menu.
2. Ask the user to select a category of operation.
3. Request the required numeric input.
4. Validate the input and check mathematical domain restrictions.
5. Perform the calculation using Python's built-in operators or the `math` module.
6. Display the result and record the calculation in session history.
7. Return to the main menu until the user chooses to exit.

The implementation is organized into a `ScientificCalculator` class to group related operations and maintain state such as angle mode and calculation history.

## 6. Tools and Technologies

- **Programming language:** Python
- **Standard library:** `math` and `datetime`
- **Interface:** Command-line / terminal
- **External dependencies:** None

## 7. Expected Outcome

The expected result is a working terminal-based scientific calculator that performs the supported operations, provides clear menu navigation, validates common input errors, and displays calculation history during the current session.

## 8. Constraints

- The application requires Python to be installed.
- Calculation history is not saved after the program closes.
- Floating-point arithmetic may produce small precision differences.
- Most functions operate on real numbers and follow the mathematical domains supported by Python's `math` module.
- The application does not include a graphical user interface.

## 9. Future Enhancements

Possible future improvements include persistent history, unit conversion, memory functions, automated tests, and a carefully validated expression parser.

## 10. Conclusion

This project demonstrates how Python can be used to create a practical scientific calculator without a GUI. It combines mathematical operations with structured programming, input validation, exception handling, and a simple interactive menu. It can serve as a foundation for further learning and development.
