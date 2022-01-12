# 13. Write a method to find the second largest number in an array.


def sec_large(arr: list) -> int:  # TC= O(n); SC= O(1)
    largest = sec_largest = float('-inf')
    for i in arr:
        if i > sec_largest:
            if i > largest:  # update largest and save old largest to sec_largest
                sec_largest = largest
                largest = i
            else:  # update second largest only
                sec_largest = i
    return sec_largest


print(sec_large(arr=[1, 20, 400]))  # 20
print(sec_large(arr=[1, 2, 0]))  # 1
