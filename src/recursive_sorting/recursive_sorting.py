# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    # A helper function that handles merging sorted pieces back together
   

    # left_idx = 0
    # right_idx = 0
    # while len(arrA) > left_idx and len(arrB) > right_idx:
    #     if arrA[left_idx] < arrB[right_idx]:
    #         merged_arr.append(arrA[left_idx])
    #         left_idx =+ 1
    #     else: 
    #         merged_arr.append(arrB[right_idx])
    #         right_idx =+ 1
    for i in range(elements):
        if i < i + 1:
            merged_arr.append(i)
    # merged_arr += arrA[left_idx:]
    # merged_arr =+ arrB[right_idx:]

    return merged_arr

print(merge([1,4,2], [5,7,6]))
# TO-DO: implement the Merge Sort function below USING RECURSION
#  A recursive function that handles dividing the array (or subarray) in half
def merge_sort( arr ):
    # TO-DO
    if len( arr ) > 1:
        pass

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
