# 17. Write a method to verify if the array contains two specified elements (12, 23).


from typing import Any


def func(arr: list, x1: Any, x2: Any) -> bool:
    return (x1 in arr) and (x2 in arr)


print(func(arr=[12, 21, 32, 23], x1=12, x2=23))  # True
