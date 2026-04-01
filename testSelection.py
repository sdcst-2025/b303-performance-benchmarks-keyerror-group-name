from tdata100000 import data
import time

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
      
        # Assume the current position holds
        # the minimum element
        min_idx = i
        
        # Iterate through the unsorted portion
        # to find the actual minimum
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
              
                # Update min_idx if a smaller element is found
                min_idx = j
        
        # Move minimum element to its
        # correct position
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

d = data.copy()
start = time.time()    
sorted = selection_sort(d)
end = time.time()
elapsed = end - start
print(f"The sort of this data took {elapsed} seconds")