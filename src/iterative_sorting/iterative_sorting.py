# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) -1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(i+1, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j
        # TO-DO: swap
        temp = arr[i]
        arr[i] = arr[smallest_index]
        arr[smallest_index] = temp

    return arr
print(selection_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    for i in range(len(arr)):
        # last i are already in place 
        for j in range(0, len(arr) - i - 1):
            # if the element is found greater than the next element, swap them
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                # without temp variabale:
                # arr[j], arr[j+1] = arr[j+1], arr[j]
    
    # for array in range(len(arr) - 1, 0, -1):
    #     for i in range(array):
    #         print(i)
    #         if arr[i] > arr[i+1]:
    #             temp = arr[i]
    #             print('k', temp)
    #             arr[i] = arr[i+1]
    #             print('l', arr[i])
    #             arr[i+1] = temp
    #             print('t', arr[i+1])

    return arr

print(bubble_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr