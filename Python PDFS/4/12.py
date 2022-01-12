# 12. Write a method to remove duplicate elements from an array.


def remove_dup(arr: list) -> None:
    from i10 import duplicates
    dup = duplicates(arr=arr)
    # print(dup)  # debugging


a = [1, 2, 3, 2, 1]
remove_dup(a)
print(a)  # [1, 2, 3]
