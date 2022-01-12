# 18. Write a program to remove the duplicate elements and return the new array.


def unique(arr: list) -> list: return list(set(arr))


print(unique(arr=[1, 2, 3, 2, 1]))  # [1, 2, 3]
