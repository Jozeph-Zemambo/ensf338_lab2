import random
import timeit
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit






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

arr1 = list(range(1, 101))
arr2 = list(range(1, 101))
arr4 = list(range(1, 101))
arr8 = list(range(1, 101))
arr16 = list(range(1, 101))
arr32 = list(range(1, 101))

test(list(range(1, 1001)))
test(list(range(1, 2001)))
test(list(range(1, 4001)))
test(list(range(1, 16001)))
test(list(range(1, 32001)))

def linear_fit(x, a, b):
    return a * x + b

def quadratic_fit(x, a, b, c):
    return a * x**2 + b * x + c

def plot_and_fit(arr_length, results):
    plt.figure(figsize=(8, 6))

  
    plt.scatter(range(1000), results, label="Data Points")

    
    popt, _ = curve_fit(linear_fit, range(1000), results)
    plt.plot(range(1000), linear_fit(np.array(range(1000)), *popt), 'r-', label="Linear Fit")

    

    plt.title(f"Array Length: {arr_length}")
    plt.xlabel("Test Case")
    plt.ylabel("Search Time (seconds)")
    plt.legend()
    plt.show()


arr_lengths = [1000, 2000, 4000, 8000, 16000, 32000]

for arr_length in arr_lengths:
    arr = list(range(1, arr_length + 1))
    results = test(arr)
    
    
    plot_and_fit(arr_length, results["binary_results"])

    
    plot_and_fit(arr_length, results["linear_results"])

