import math

class Calculator:
    def __init__(self):
        self.history = []

    def _log(self, operation, result):
        self.history.append(f"{operation} = {result}")

    def add(self, a, b):
        result = a + b
        self._log(f"{a} + {b}", result)
        return result

    def subtract(self, a, b):
        result = a - b
        self._log(f"{a} - {b}", result)
        return result

    def multiply(self, a, b):
        result = a * b
        self._log(f"{a} * {b}", result)
        return result

    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero"
        result = a / b
        self._log(f"{a} / {b}", result)
        return result

    def power(self, a, b):
        result = a ** b
        self._log(f"{a} ** {b}", result)
        return result

    def square_root(self, a):
        result = math.sqrt(a)
        self._log(f"√{a}", result)
        return result

    def get_history(self):
        return self.history
