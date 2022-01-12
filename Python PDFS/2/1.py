# 1. Write a function for arithmetic operators (+,-,*,/).


def arithmetic(num1: float, op: str, num2: float) -> float:
    match op:
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '*':
            return num1 * num2
        case '/':
            return num1 / num2
        case '%':
            return num1 % num2
        case _:
            raise Exception('Unknown operation')


print(arithmetic(num1=14, op='+', num2=7))
print(arithmetic(num1=14, op='-', num2=7))
print(arithmetic(num1=14, op='*', num2=7))
print(arithmetic(num1=14, op='/', num2=7))
print(arithmetic(num1=14, op='%', num2=7))
# print(arithmetic(num1=14, op='', num2=7))  # Exception: Unknown operation
