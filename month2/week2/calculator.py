class Calculator:
    def add_(self, a, b):
        return a + b 
    def sub_(self, a ,b):
        return a - b
    def div_(self, a, b):  
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b

