# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    i = 0
    j = 0
    k = 0

    # traverse both array
    while i < len(arrA) and j < len(arrB):
        if arrA[i] < arrB[j]:
            merged_arr[k] = arrA[i]
            k += 1
            i += 1
        else:
            merged_arr[k] = arrB[j]
            k += 1
            j += 1
    while i < len(arrA):
        merged_arr[k] = arrA[i]
        k += 1
        i += 1
    while j < len(arrB):
        merged_arr[k] = arrB[j]
        k += 1
        j += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # Your code here
    if len(arr) <= 1:
        return arr
    # elif len(arr) > 1:
    mid = len(arr)//2 # Find the mid of the array
    left = arr[:mid] # Diving the array elements
    right = arr[mid:] # into 2 halves

    # recursicely sort each half
    left = merge_sort(left) # sorting the first half
    right = merge_sort(right) # sorting the second half

    arr = merge(left, right)


    return arr


# implement an in-place merge sort algorithm
# def merge_in_place(arr, start, mid, end):
#     # Your code here


#     return arr


def merge_sort_in_place(arr, l, r):
    # Your code here


    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
# def timsort(arr):
#     # Your code here

#     return arr