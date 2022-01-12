# 3. Write a program to find the index of an array element.


from typing import Any


def index(arr: list, x: Any) -> int:
    ans = 0
    for i in arr:
        if i == x:
            return ans
        ans += 1
    return -1  # element not found


print(index(arr=[1, 2, 3, 4, 5], x=3))  # 2
print(index(arr=[1, 2, 3, 4, 5], x=-3))  # -1
