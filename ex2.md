# SECTION 2/1

1. **Interpolation Search Overview:**
   - Interpolation search is effective when dealing with uniformly distributed and sorted data.
   - It dynamically adjusts its search position based on the value of the key being searched, potentially resulting in faster searches compared to binary search.
   
2. **Potential Performance Issues:**
   - The performance of interpolation search can be negatively affected if the formula used to calculate the "mid point" is implemented incorrectly.
   - In the worst-case scenario, this can lead to a time complexity of O(n), diminishing the advantages of interpolation search.
   
3. **Modification to Interpolated Mid Point Calculation:**
   - Consideration should be given to modifying the calculation of the interpolated mid point to address potential performance issues.

# SECTION 2/2

1. **Use Cases for Linear Search:**
   - Linear search is suitable when the data being searched is not sorted.
   - It is particularly effective for small datasets where the overhead of sorting is not justified.
   
2. **When to Choose Linear Search:**
   - Opt for linear search when the dataset is very small and not sorted.
   
3. **Optimizations for Searching Algorithms:**
   - Various strategies can be employed to improve searching algorithms in specific use cases.
   - One approach is to switch to linear searching when dealing with a small dataset.
   - Pre-sorting the data before initiating the search process can also enhance the efficiency of searching algorithms.