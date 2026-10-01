import math


def calculate(a, operator, b):
    if operator == "+":
        return a + b
    if operator == "-":
        return a - b
    if operator == "*":
        return a * b
    if operator == "sqrt":
        return math.sqrt(a)
    raise ValueError("Unsupported operator")


if __name__ == "__main__":
    first = float(input("First number: "))
    operator = input("Operator (+, -, *, sqrt): ")
    second = 0 if operator == "sqrt" else float(input("Second number: "))
    print(calculate(first, operator, second))