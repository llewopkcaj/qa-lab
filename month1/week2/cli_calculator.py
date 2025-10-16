import math


def calculate(x, a, b=None):
    """Return the result of op `x` on `a` (and optional `b`); raises on invalid ops or math errors.
    Args: x(str), a(float), b(float|None). Returns: float."""

    if x == "add":
        return a + b
    elif x == "subtract":
        return a - b
    elif x == "multiply":
        return a * b
    elif x == "power":
        return a**b
    elif x == "divide":
        # Require a second number and forbid division by zero
        if b is None:
            raise ValueError("operation 'divide' requires two numbers")
        if b == 0:
            raise ZeroDivisionError("cannot divide by zero")
        return a / b
    elif x == "sqrt":
        # Forbid square root of negative numbers
        if a < 0:
            raise ValueError("cannot take square root of a negative number")
        return math.sqrt(a)  # make sure: import math at the top
    else:
        raise ValueError("invalid operation")


PERMITTED_OPS = (
    "add",
    "subtract",
    "multiply",
    "power",
    "divide",
    "sqrt",
)


def run_it():
    """Interactive CLI loop that prompts for an operation and numbers, prints the result; returns None."""
    while True:
        x = input(f"Enter operation({PERMITTED_OPS} or q to turn off):").strip().lower()
        if x == "q":
            print("Goodbye!")
            break
        if x not in PERMITTED_OPS:
            print("Error: invalid operation")
            continue

        try:  # Nesting inputs with calculate() inside the loop
            a = float(input("Enter first number: "))
            if x != "sqrt":
                b = float(input("Enter second number: "))
            else:
                b = None
        except ValueError:  # Anticipating errors with user inputs
            print("Error: inputs must be numbers")
            continue
        try:  # Making sure the loop doesn't break within calculate ()
            result = calculate(x, a, b)
        except (ValueError, ZeroDivisionError) as e:
            print(f"Error: {e}")
            continue
        if x == "sqrt":  # Reformats sqrt result (doesn't use b)
            print(f"Result: sqrt({a:.2f}) is {result:.2f}")
        else:
            print(f"Result: {a:.2f} {x} {b:.2f} is {result:.2f}")


if __name__ == "__main__":
    run_it()
