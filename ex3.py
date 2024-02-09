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

#SECTION 3
#3.1) A profiler creates a set of statistics that describes how often and for how long various parts of the program executed
#3.2) A profiler creates a profile with alot of statistics that can provide insight to where code can be optimized and more useful information. Benchmarking uses standardized tests to see how a program performs under certain workloads.
#3.4) Profiling the functions we get a table that contains different information. The first coloumn has ncalls which is the number of calls to the function, next is tottime which is time spent in function excluding time spent in sub or recursive functions. third collumn is percall which is tottime / ncalls. next is cumtime which is time spent in function as well as sub and recursive functions. next is the percall for cumtime / ncalls. finally is filename which is where the function is in the script. With all that in mind I can say that the execution time will be in the cumtime column.