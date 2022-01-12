# 2. Write a function to calculate the average value of an array of integers.


def avg_of(arr: list) -> float:
    return sum(arr)/len(arr)


print(avg_of(arr=[1, 2, 3, 4, 5]))  # 3.0
