"""
Scientific Calculator - Terminal Based
Author: Your Name
Description: A menu-driven scientific calculator built using Python's standard library.
"""

import math
from datetime import datetime


class ScientificCalculator:
    """Provides basic and scientific calculations in a terminal interface."""

    def __init__(self):
        self.angle_mode = "DEG"
        self.history = []

    def record(self, expression, result):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.history.append((timestamp, expression, result))

    def get_number(self, prompt="Enter a number: "):
        """Read a valid finite number from the user."""
        while True:
            raw = input(prompt).strip()
            try:
                value = float(raw)
                if not math.isfinite(value):
                    print("Please enter a finite number.")
                    continue
                return value
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

    def show_result(self, expression, result):
        print(f"\n{expression} = {result}\n")
        self.record(expression, result)

    def basic_operations(self):
        print("\n--- Basic Operations ---")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Modulus (%)")
        print("6. Power (x^y)")
        choice = input("Choose an operation: ").strip()

        if choice not in {"1", "2", "3", "4", "5", "6"}:
            print("Invalid operation.")
            return

        a = self.get_number("Enter the first number: ")
        b = self.get_number("Enter the second number: ")

        try:
            operations = {
                "1": (f"{a} + {b}", lambda: a + b),
                "2": (f"{a} - {b}", lambda: a - b),
                "3": (f"{a} * {b}", lambda: a * b),
                "4": (f"{a} / {b}", lambda: a / b),
                "5": (f"{a} % {b}", lambda: a % b),
                "6": (f"{a} ^ {b}", lambda: a ** b),
            }
            expression, operation = operations[choice]
            if choice == "4" and b == 0:
                raise ZeroDivisionError
            if choice == "5" and b == 0:
                raise ZeroDivisionError
            result = operation()
            if isinstance(result, complex):
                result = f"{result.real:.10g} + {result.imag:.10g}i"
            elif isinstance(result, float) and not math.isfinite(result):
                raise OverflowError
            self.show_result(expression, result)
        except ZeroDivisionError:
            print("Error: division or modulus by zero is undefined.")
        except (OverflowError, ValueError):
            print("Error: the operation is outside the supported numeric range.")

    def trigonometry(self):
        print(f"\n--- Trigonometry (current mode: {self.angle_mode}) ---")
        print("1. Sine")
        print("2. Cosine")
        print("3. Tangent")
        print("4. Inverse sine")
        print("5. Inverse cosine")
        print("6. Inverse tangent")
        choice = input("Choose a function: ").strip()
        if choice not in {"1", "2", "3", "4", "5", "6"}:
            print("Invalid function.")
            return

        x = self.get_number("Enter the value: ")
        try:
            if choice in {"1", "2", "3"}:
                angle = math.radians(x) if self.angle_mode == "DEG" else x
                funcs = {"1": math.sin, "2": math.cos, "3": math.tan}
                names = {"1": "sin", "2": "cos", "3": "tan"}
                result = funcs[choice](angle)
                expression = f"{names[choice]}({x} {'degrees' if self.angle_mode == 'DEG' else 'radians'})"
            else:
                funcs = {"4": math.asin, "5": math.acos, "6": math.atan}
                names = {"4": "asin", "5": "acos", "6": "atan"}
                angle = funcs[choice](x)
                result = math.degrees(angle) if self.angle_mode == "DEG" else angle
                expression = f"{names[choice]}({x})"
                expression += " in degrees" if self.angle_mode == "DEG" else " in radians"

            if not math.isfinite(result):
                raise ValueError
            self.show_result(expression, result)
        except ValueError:
            print("Error: this value is outside the valid domain for that function.")

    def logarithms_and_powers(self):
        print("\n--- Logarithms and Roots ---")
        print("1. Natural logarithm ln(x)")
        print("2. Base-10 logarithm log10(x)")
        print("3. Logarithm with a custom base")
        print("4. Square root")
        print("5. Cube root")
        choice = input("Choose an operation: ").strip()

        try:
            if choice == "1":
                x = self.get_number("Enter x (x > 0): ")
                result = math.log(x)
                expression = f"ln({x})"
            elif choice == "2":
                x = self.get_number("Enter x (x > 0): ")
                result = math.log10(x)
                expression = f"log10({x})"
            elif choice == "3":
                x = self.get_number("Enter x (x > 0): ")
                base = self.get_number("Enter the base (positive, not 1): ")
                if x <= 0 or base <= 0 or base == 1:
                    raise ValueError
                result = math.log(x, base)
                expression = f"log base {base} of {x}"
            elif choice == "4":
                x = self.get_number("Enter x (x >= 0): ")
                result = math.sqrt(x)
                expression = f"sqrt({x})"
            elif choice == "5":
                x = self.get_number("Enter x: ")
                result = math.copysign(abs(x) ** (1 / 3), x)
                expression = f"cuberoot({x})"
            else:
                print("Invalid operation.")
                return
            self.show_result(expression, result)
        except ValueError:
            print("Error: input is outside the valid domain for this operation.")
        except OverflowError:
            print("Error: the result is too large to calculate.")

    def other_functions(self):
        print("\n--- Other Scientific Functions ---")
        print("1. Factorial")
        print("2. Absolute value")
        print("3. Exponential e^x")
        print("4. Square (x^2)")
        print("5. Reciprocal (1/x)")
        print("6. Show constants (pi and e)")
        choice = input("Choose an operation: ").strip()

        try:
            if choice == "1":
                x = self.get_number("Enter a non-negative integer: ")
                if x < 0 or not x.is_integer():
                    print("Factorial requires a non-negative integer.")
                    return
                if x > 10000:
                    print("Input is too large for this calculator's factorial limit (10000).")
                    return
                result = math.factorial(int(x))
                expression = f"{int(x)}!"
            elif choice == "2":
                x = self.get_number("Enter x: ")
                result = abs(x)
                expression = f"abs({x})"
            elif choice == "3":
                x = self.get_number("Enter x: ")
                result = math.exp(x)
                expression = f"e^{x}"
            elif choice == "4":
                x = self.get_number("Enter x: ")
                result = x ** 2
                expression = f"{x}^2"
            elif choice == "5":
                x = self.get_number("Enter x (x != 0): ")
                if x == 0:
                    raise ZeroDivisionError
                result = 1 / x
                expression = f"1/{x}"
            elif choice == "6":
                print(f"pi = {math.pi}")
                print(f"e  = {math.e}")
                return
            else:
                print("Invalid operation.")
                return

            if isinstance(result, float) and not math.isfinite(result):
                raise OverflowError
            self.show_result(expression, result)
        except ZeroDivisionError:
            print("Error: reciprocal of zero is undefined.")
        except OverflowError:
            print("Error: the result is too large to calculate.")

    def toggle_angle_mode(self):
        self.angle_mode = "RAD" if self.angle_mode == "DEG" else "DEG"
        print(f"Angle mode changed to {self.angle_mode}.")

    def show_history(self):
        print("\n--- Calculation History ---")
        if not self.history:
            print("No calculations have been recorded yet.")
            return
        for index, (timestamp, expression, result) in enumerate(self.history, start=1):
            print(f"{index}. [{timestamp}] {expression} = {result}")

    def run(self):
        print("=" * 48)
        print("        SCIENTIFIC CALCULATOR")
        print("             Terminal Edition")
        print("=" * 48)

        while True:
            print(f"\nAngle mode: {self.angle_mode}")
            print("1. Basic arithmetic")
            print("2. Trigonometric functions")
            print("3. Logarithms and roots")
            print("4. Other scientific functions")
            print("5. Toggle degree/radian mode")
            print("6. View calculation history")
            print("7. Exit")

            choice = input("Select an option (1-7): ").strip()
            if choice == "1":
                self.basic_operations()
            elif choice == "2":
                self.trigonometry()
            elif choice == "3":
                self.logarithms_and_powers()
            elif choice == "4":
                self.other_functions()
            elif choice == "5":
                self.toggle_angle_mode()
            elif choice == "6":
                self.show_history()
            elif choice == "7":
                print("Thank you for using the Scientific Calculator. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a number from 1 to 7.")


def main():
    calculator = ScientificCalculator()
    try:
        calculator.run()
    except (KeyboardInterrupt, EOFError):
        print("\n\nCalculator closed. Goodbye!")


if __name__ == "__main__":
    main()
