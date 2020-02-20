# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    # elements = len( arrA ) + len( arrB )
    # print('elements', elements)
    # merged_arr = [0] * elements
    merged_arr = []
    # TO-DO
    # A helper function that handles merging sorted pieces back together
    a, b = 0, 0 
    while a < len(arrA) and b < len(arrB):
            if arrA[a] < arrB[b]:
                merged_arr.append(arrA[a])
                a += 1
            else: 
                merged_arr.append(arrB[b])
                b += 1
    merged_arr = merged_arr + arrA[a:] + arrB[b:]
    # for i in range(0, elements):
    #         if a >= len(arrA):
    #             merged_arr[i] = arrB[b]
    #             b += 1
    #         elif b >= len(arrB):
    #             merged_arr[i] = arrA[a]
    #             a += 1
    #         elif arrA[a] < arrB[b]:
    #             merged_arr[i] = arrA[a]
    #             a += 1
    #         else:
    #             merged_arr[i] = arrB[b]
    #             b += 1

    return merged_arr

# print(merge([1,2], [4, 5, 9]))

# TO-DO: implement the Merge Sort function below USING RECURSION
# A recursive function that handles dividing the array (or subarray) in half
def merge_sort( arr ):
    # TO-DO
    if len( arr ) < 2:
        return arr
    
    middle = len(arr) // 2
    arr_a = arr[:middle]
    arr_b = arr[middle:]

    return merge(merge_sort(arr_a), merge_sort(arr_b))


print(merge_sort([1,4,6, 8,9,3,2]))
# moving things to the right 

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
