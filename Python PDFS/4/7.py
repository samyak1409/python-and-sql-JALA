# 7. Write a function to insert an element at a specific position in the array.


from typing import Any


def insert(arr: list, x: Any, pos: int) -> None:
    arr.append(None)  # adding a placeholder
    for i in range(len(arr)-pos):  # shifting values to the right
        arr[-i-1] = arr[-i-2]
    arr[pos-1] = x  # inserting value


a = [1, 2, 3, 4]
insert(arr=a, x=5, pos=3)
print(a)  # [1, 2, 5, 3, 4]
