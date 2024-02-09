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

i=0
def test(arr, i):
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
    barr[i] = binary_total / 1000
    larr[i] = linear_total / 1000
    i+=1
    return {
        
    }

barr = list(range(1, 7))
larr = list(range(1, 7))
i=0

list_size = [1000, 2000, 4000, 8000, 16000, 32000]

def linearz(x, a, b):
        return a * x + b

def logarithmic(x, a, b):
    return a * np.log(x) + b

popt_lin, pcov_lin = curve_fit(linearz, list_size, larr)
popt_bin, pcov_bin = curve_fit(logarithmic, list_size, barr)

# Plotting function
def plot_and_fit(list_sizes, times, popt, func, title):
    xnew = np.linspace(min(list_sizes), max(list_sizes), num=1000, endpoint=True)
    plt.plot(list_sizes, times, 'o', xnew, func(xnew, *popt), '-')
    plt.title(title)
    plt.savefig(title + '.png') 
    plt.show()


# Call the test function
test(list(range(1, 1001)),i)
test(list(range(1, 2001)),i)
test(list(range(1, 4001)),i)
test(list(range(1, 8001)),i)
test(list(range(1, 16001)),i)
test(list(range(1, 32001)),i)

plot_and_fit(list_size, barr, popt_bin, logarithmic, "Binary Graph")

plot_and_fit(list_size, larr, popt_lin, linearz,"Linear Graph")