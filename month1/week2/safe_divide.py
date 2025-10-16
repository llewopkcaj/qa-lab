def safe_divide(a, b):
    try:
        a = float(a)
        b = float(b)
        return a / b
    except ZeroDivisionError as err:
        raise ValueError("Error: Division by zero is not allowed.") from err
    except (ValueError, TypeError, NameError) as err:
        raise ValueError("Error: Invalid input. Please enter numbers only.") from err
