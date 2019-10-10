import numpy as np

# Generating a random vector for ordering
# vector = list(np.random.randint(1,100, 10))
vector = [4, 3, 8, 1, 2, 9, 6, 0, 7, 5]

def countingSort(arr, unit_marker):
  vector_size = len(arr)
  output = [0] * vector_size
  count = [0] * 10

  for element in arr:
    digit_count = (element // unit_marker) % 10
    count[digit_count] += 1

  pivot = 0

  # Acumulando para sabe aonde eu vou colocar no meu array de output
  for i in range(1,10): 
    count[i] += count[i-1]

  i = vector_size - 1
  while i >= 0: 
    element = arr[i]
    digit_count = (element // unit_marker) % 10
    output[count[digit_count] - 1] = arr[i]
    count[digit_count] -= 1
    i -= 1

  return output

def radixSort(arr):
  higher = None

  for element in arr:
    if higher == None or element > higher:
      higher = element
  
  unit_marker = 1
  while higher // unit_marker > 0:
    arr = countingSort(arr, unit_marker)
    unit_marker *= 10
  
  return arr

print(vector)
vector = radixSort(vector)
print(vector)
