import timeit
import profile

def sub_function(n):
    #sub function that calculates the factorial of n
    if n == 0:
        return 1
    else:
        return n * sub_function(n-1)
    
def test_function():
    data = []
    for i in range(10):
        data.append(sub_function(i))
    return data

def third_function():
    #third function that calculates the square of the numbers from 0 to 999
    return [i**2 for i in range(100000000)]


print("Profiling test_function:")
profiler = profile.Profile()
profiler.runcall(test_function)
profiler.print_stats(sort='cumulative')

print("\nProfiling third_function:")
profiler = profile.Profile()
profiler.runcall(third_function)
profiler.print_stats(sort='cumulative')