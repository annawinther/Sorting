# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    print('elements', elements)
    merged_arr = [0] * elements
    # TO-DO
    # A helper function that handles merging sorted pieces back together
    # 1 --> declare two variables starting at 0
    # 2 --> compare those valiarbles with the lenght of each array 
        # if its bigger or equal to thw length of the array we compare it to, append it to the merged_arr.
        # Then in the loop add one to the variable for each item in the loop
        # DO the same for both sides, 
    a, b = 0, 0 
    # while len(arrA) > a and len(arrB) < b:
    #         if arrA[a] < 2:
    #             print(arrA)
    #             print(arrB)
    #             merged_arr = arrA[a]
    #             a =+ 1
    #         else: 
    #             merged_arr = arrB[b]
    #             b =+ 1
    for i in range(0, elements):
            if a >= len(arrA):
                merged_arr[i] = arrB[b]
                b += 1
            elif b >= len(arrB):
                merged_arr[i] = arrA[a]
                a += 1
            elif arrA[a] < arrB[b]:
                merged_arr[i] = arrA[a]
                a += 1
            else:
                merged_arr[i] = arrB[b]
                b += 1
        
    # left_idx = 0
    # right_idx = 0
    # while len(arrA) > left_idx:
    #     if arrA[left_idx] < 2:
    #         print(arrA)
    #         print(arrB)
    #         merged_arr.append(arrA[left_idx])
    #         left_idx =+ 1
    #     else: 
    #         merged_arr.append(arrB[right_idx])
    #         right_idx =+ 1
    # for i in range(0, elements):
    #     if i < i +1:
    #         merged_arr[i]
        # if i == 0:
        #     return i
        # elif i < i + 1:
        #     merged_arr.append(i)
    # merged_arr += arrA[left_idx:]
    # merged_arr =+ arrB[right_idx:]

    return merged_arr

print(merge([1,2], [4, 5, 9]))

# TO-DO: implement the Merge Sort function below USING RECURSION
# A recursive function that handles dividing the array (or subarray) in half
def merge_sort( arr ):
    # TO-DO
    if len( arr ) > 2:
        return arr
    
    middle = len(arr) // 2
    arr_a = arr[:middle]
    arr_b = arr[middle:]

    return merge(merge_sort(arr_a), merge_sort(arr_b))


print(merge([1,4,6], [8,9,3,2]))


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
