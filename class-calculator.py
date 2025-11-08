class Calculator:
    def add(self, a, b):
        sum = a + b
        print(f"The sum is {sum}")

    def subtract(self, a, b):
        sub = a - b
        print(f"The subtraction equals to {sub}")

    def multiply(self, a, b):
        mult = a * b
        print(f"The answer is {mult}")

    def divide(self, a, b):
        if b == 0:
            print("Error: Cannot divide by zero.")
        else:
            quotient = a / b
            print(f"The quotient is {quotient}")


calculator = Calculator()

calculator.add(4, 2)
calculator.subtract(4, 2)
calculator.multiply(4, 2)
calculator.divide(4, 0)