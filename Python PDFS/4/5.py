# 5. Write a function to remove a specific element from an array.


from typing import Any


def remove(arr: list, x: Any) -> None:
    for i in range(len(arr)):  # loop to locate the element to remove
        if arr[i] == x:  # element to remove found
            for j in range(i, len(arr)-1):  # shifting elements to left
                arr[j] = arr[j+1]
            arr.pop()  # delete the last garbage value
            break  # element removed


a = [1, 2, 3]
remove(arr=a, x=2)
print(a)  # [1, 3]
