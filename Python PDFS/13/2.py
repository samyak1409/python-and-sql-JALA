# 2. Write two methods with the same name but different number of parameters of different data type and call the methods.


# Python doesn't support Method Overloading :), though we can achieve the same by:

from typing import Any


def print_(*x: Any) -> None:
    print(*x)


print_(21)
print_('Samyak', 'Jain')
print_()
