# 1. Write a function to add integer values of an array.


def sum_(arr: list) -> int:
    ans = 0
    for i in arr:
        ans += i
    return ans


print(sum_(arr=[1, 2, 3, 4, 5]))  # 15
