def min_index(arr, start, n):
    smallest = arr[start]     
    pos = start               
    for j in range(start + 1, n):  
        if arr[j] < smallest:     
            smallest = arr[j]
            pos = j
    return pos  

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):  
        pos = min_index(arr, i, n)  
        arr[i], arr[pos] = arr[pos], arr[i]  
