# 1. Write two methods with the same name but different number of parameters of same type and call the methods.


# Python doesn't support Method Overloading :) [PS- are these questions directly copied from Java or something?],
# though we can achieve the same by:


def func(*num: int) -> int:
    """Multiply."""
    from functools import reduce
    from operator import mul
    return reduce(mul, num)


print(func(10))
print(func(10, 20, 30))
# print(func())  # Error
