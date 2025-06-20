def find_min_index(arr, start):
    min_idx = start
    for i in range(start + 1, len(arr)):
        if arr[i] < arr[min_idx]:
            min_idx = i
    return min_idx

def selection_sort(arr):
    for i in range(len(arr)):
        min_index = find_min_index(arr, i)
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
