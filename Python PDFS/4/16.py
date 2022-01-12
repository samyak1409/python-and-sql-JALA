# 16. Write a function to get the difference of largest and smallest value.


def max_diff(arr: list) -> int:
    from i8 import min_n_max
    small, large = min_n_max(arr=arr)
    return large - small


print(max_diff(arr=[1, 2, 3, 4, 5]))  # 4
