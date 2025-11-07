class Calculator:

    def add(self, a, b):

        return a + b

    def subtract(self, a, b):

        return a - b

    def multiply(self, a, b):

        return a * b

    def divide(self, a, b):

        if b == 0:
            raise ValueError("Cannot divide by zero")

        return a / b

    def is_even(self, number):

        return number % 2 == 0

    def factorial(self, n):

        if n < 0:
            raise ValueError("Factorial not defined for negative numbers")

        if n == 0:
            return 1

        result = 1

        for i in range(1, n + 1):
            result *= i

        return result