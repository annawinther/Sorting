# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(i+1, len(arr) -1):
            if arr[smallest_index] > arr[j]:
                smallest_index = j
                # print(smallest_index)
        # TO-DO: swap
        temporary = arr[i]
        arr[i] = arr[smallest_index]
        arr[smallest_index] = temporary

    return arr
# print(selection_sort([5,2,1,9,0,4,6]))

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    for array in range(len(arr) - 1, 0, -1):
        for i in range(array):
            print(i)
            if arr[i] > arr[i+1]:
                temp = arr[i]
                print('k', temp)
                arr[i] = arr[i+1]
                print('l', arr[i])
                arr[i+1] = temp
                print('t', arr[i+1])

    return arr

print(bubble_sort([5,2,1,9,0,4,6]))

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr