import time
import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def measure_time(sort_func, arr):
    start_time = time.time()
    sort_func(arr)
    return time.time() - start_time

arr = [random.randint(1, 100000) for _ in range(9999)]

bubble_sort_time = measure_time(bubble_sort, arr.copy())
selection_sort_time = measure_time(selection_sort, arr.copy())
insertion_sort_time = measure_time(insertion_sort, arr.copy())
python_sorted_time = measure_time(sorted, arr.copy())

print("Bubble Sort Execution Time:", bubble_sort_time, "seconds")
print("Selection Sort Execution Time:", selection_sort_time, "seconds")
print("Insertion Sort Execution Time:", insertion_sort_time, "seconds")
print("Python's sorted() Function Execution Time:", python_sorted_time, "seconds")
