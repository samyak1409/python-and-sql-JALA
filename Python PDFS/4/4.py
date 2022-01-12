# 4. Write a function to test if array contains a specific value.


from typing import Any


def contains(arr: list, x: Any) -> bool: return x in arr


print(contains(arr=[1, 2, 3, 4, 5], x=3))  # True
print(contains(arr=[1, 2, 3, 4, 5], x=-3))  # False
