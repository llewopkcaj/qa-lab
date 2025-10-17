class Calculator:
    def add_(self, a: float, b: float) -> float:
        return a + b

    def sub_(self, a: float, b: float) -> float:
        return a - b

    def div_(self, a: float, b: float) -> float:
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b
