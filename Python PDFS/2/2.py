# 2. Write a method for increment and decrement operators (++, --).


# There are no '++' and '--' operators in Python.

def unary(num: int, op: str) -> int:
    match op:
        case '++':
            num += 1
        case '--':
            num -= 1
        case _:
            raise Exception('Unknown operation')
    return num


print(unary(num=21, op='++'))
print(unary(num=21, op='--'))
# print(unary(num=0, op=''))  # -> error
