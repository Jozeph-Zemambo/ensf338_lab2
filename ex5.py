import random
import timeit

def binary(arr, n):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        mid_val = arr[mid]

        if mid_val == n:
            return mid
        elif mid_val < n:
            low = mid + 1
        else:
            high = mid - 1
    return "Not found"

def linear(arr, n):
    for i, num in enumerate(arr):
        if num == n:
            return i
    return "Not found"

def test(arr):
    binary_total = 0
    linear_total = 0
    for _ in range(1000):
        n = random.randint(1, len(arr))

        # Measure time for linear search
        linear_start = timeit.default_timer()
        for _ in range(100):
            linear(arr, n)
        linear_end = timeit.default_timer()

        # Measure time for binary search
        binary_start = timeit.default_timer()
        for _ in range(100):
            binary(arr, n)
        binary_end = timeit.default_timer()

        binary_total += (binary_end - binary_start)
        linear_total += (linear_end - linear_start)

    return {
        "b_avg": binary_total / 1000,
        "l_avg": linear_total / 1000
    }

arr1 = list(range(1, 1001))
arr2 = list(range(1, 2001))
arr4 = list(range(1, 4001))
arr8 = list(range(1, 8001))
arr16 = list(range(1, 16001))
arr32 = list(range(1, 32001))

print(test(arr1))
print(test(arr2))
print(test(arr4))
print(test(arr16))
print(test(arr32))

