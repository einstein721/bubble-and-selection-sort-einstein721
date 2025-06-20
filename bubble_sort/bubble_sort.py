def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False  # Optimization: track if any swaps happened
        for j in range(0, n - 1 - i):
            if arr[j] > arr[j + 1]:
                # Swap if elements are in wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break  # Stop early if already sorted

