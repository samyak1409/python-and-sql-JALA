# 12. Write a method to remove duplicate elements from an array.


def remove_dup(arr: list) -> None:

    from i10 import duplicates
    dup = duplicates(arr=arr)
    # print(dup)  # debugging

    for x in dup:  # loop over duplicate elements
        for i in range(len(arr)):  # loop to locate the duplicate
            if arr[-i-1] == x:  # duplicate found
                for j in range(i):  # shift elements to left
                    arr[-i-1+j] = arr[-i+j]
                arr.pop()  # delete the last garbage value
                break  # duplicate removed


a = [1, 2, 3, 2, 1]
remove_dup(a)
print(a)  # [1, 2, 3]
