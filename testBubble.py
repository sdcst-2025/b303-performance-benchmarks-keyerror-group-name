from tdata100000 import data
import time

def bubbleSort(arr):
    for k in range(len(arr)):
        for j in range(k,len(arr)):
            if arr[k] > arr[j]:
                temp = arr[k]
                arr[k] = arr[j]
                arr[j] = temp
    return arr

d = data.copy()
start = time.time()
sorted = bubbleSort(d)
end = time.time()
elapsed = end - start
print(f"The sort of this data took {elapsed} seconds")