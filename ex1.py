# 1. It computes the fibonacci sequence
# 2. No it just completes the fibonacci sequence recursively
# 3. 2^n complexity

def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0 or n == 1:
        return n
    else:
        memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
        return memo[n]


# 5. 0(n) complexity
import timeit
import matplotlib.pyplot as plt

def func(n):
    if n == 0 or n == 1:
        return n
    else:
        return func(n-1) + func(n-2)

def func_memo(n, memo={}):
    if n == 0 or n == 1:
        return n
    
    if n not in memo:
        memo[n] = func_memo(n-1, memo) + func_memo(n-2, memo)
    
    return memo[n]

# Measure execution time for the original function
original_times = []
for i in range(36):
    time_taken = timeit.timeit(lambda: func(i), number=10)  # Number of repetitions can be adjusted
    original_times.append(time_taken)

# Measure execution time for the memoized function
memoized_times = []
for i in range(36):
    time_taken = timeit.timeit(lambda: func_memo(i), number=10)  # Number of repetitions can be adjusted
    memoized_times.append(time_taken)

# Plotting the results
plt.plot(range(36), original_times, label='Original Function')
plt.xlabel('Input (n)')
plt.ylabel('Execution Time (s)')
plt.legend()
plt.savefig('ex1.6.1.jpg')  # Save the plot for the original function

# If you want to create a separate plot for the memoized function, uncomment the lines below:
plt.figure()
plt.plot(range(36), memoized_times, label='Memoized Function')
plt.xlabel('Input (n)')
plt.ylabel('Execution Time (s)')
plt.legend()
plt.savefig('ex1.6.2.jpg')  # Save the plot for the memoized function

plt.show()