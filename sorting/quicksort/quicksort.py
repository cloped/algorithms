import numpy as np

# Generating a random vector for ordering
# vector = list(np.random.randint(1,100, 10))
vector = [4, 3, 8, 1, 2, 9, 6, 0, 7, 5]

def callQuick(arr, first, last):
  if first >= last:
    return
  
  pivot = arr[last]

  markup = first - 1
  actual = first

  for index in range(first, last):
    if arr[index] < pivot:
      markup += 1
      arr[markup], arr[actual] = arr[actual], arr[markup] 

    actual += 1
  
  markup += 1
  arr[markup], arr[last] = arr[last], arr[markup] 

  callQuick(arr, first, markup - 1)
  callQuick(arr, markup + 1, last)

def quickSort(arr):
  callQuick(arr, 0, len(arr) - 1)
  return arr

print(vector)
quickSort(vector)
print(vector)

