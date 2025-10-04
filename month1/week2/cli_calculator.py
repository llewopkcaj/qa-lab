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
        return a ** b
    elif x == "divide":
    # Require a second number and forbid division by zero
        if b is None:
            raise ValueError("Operation 'divide' requires two numbers.")
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b
    elif x == "sqrt":
        # Forbid square root of negative numbers
        if a < 0:
            raise ValueError("Cannot take square root of a negative number")
        return math.sqrt(a)  # make sure: import math at the top
    else:
        raise ValueError("Invalid operation")
    

def run_it():
    """Interactive CLI loop that prompts for an operation and numbers, prints the result; returns None."""

    while True:
        x = input("Enter operation (add, subtract, multiply, divide, power, sqrt, or q to turn off): ").strip().lower()  
        if x == "q":
            break
        try:            #Nesting inputs with calculate() inside the loop
            a = float(input("Enter first number: "))
            if x != "sqrt":
                b = float(input("Enter second number: "))
            else:
                b = None  
        except(ValueError, TypeError):          # Anticipating errors with user inputs
            print("Inputs must be numbers")
            continue
        try:            # Making sure the loop doesn't break within calculate ()
            result = calculate(x, a, b)
        except (ValueError, ZeroDivisionError) as e:
            print(f"Error: {e}")
            continue 
        if x == "sqrt":        # Reformats sqrt result (doesn't use b)
            print(f"sqrt({a:.2f}) is {result:.2f}")
        else:
            print(f"{a:.2f} {x} {b:.2f} is {result:.2f}")        
    
run_it()    



