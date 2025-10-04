def safe_divide(a, b):
    try:
        a = float(a)
        b = float(b)
        return a / b
    except ZeroDivisionError:
        raise ValueError("Error: Division by zero is not allowed.")
    except (ValueError, TypeError, NameError):
        raise ValueError("Error: Invalid input. Please enter numbers only.")


