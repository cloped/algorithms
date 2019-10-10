import numpy as np

# Generating a random vector for ordering
# vector = list(np.random.randint(1,100, 10))
vector = [92, 8, 18, 5, 29, 9, 25, 80, 46, 58]

def heapify(array, index, v_size):
  largest = index
  left = 2 * index + 1
  right = 2 * index + 2

  if left < v_size and array[left] > array[index]:
    largest = left

  if right < v_size and array[right] > array[largest]:
    largest = right

  if largest != index:
    array[index], array[largest] = array[largest], array[index]
    heapify(array, largest, v_size)

def heapSort(arr):  
  v_size = len(arr)

  # Building max heap
  for index in range(int(len(arr) / 2) - 1, -1, -1):
    heapify(arr, index, v_size)

  for index in range(v_size - 1, 0, -1):
    arr[0], arr[index] = arr[index], arr[0]
    # Pass index as size to change the ordered parts, this step is the "exclusion from the tree"
    heapify(arr, 0, index)

  return arr

  # print(arr)

print(vector)
heapSort(vector)
print(vector)
