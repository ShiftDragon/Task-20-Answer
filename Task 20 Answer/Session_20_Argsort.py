"Session 20 argsort() Code examples."

import numpy as np

# Part 1 - What argsort returns

print('\nWhat argsort returns')
arr = np.array([30, 10, 50, 20, 40])
indices = np.argsort(arr)
print('Indices:', indices)
print('Values:', arr[indices])

# Expected output:
# Indices: [1 3 0 4 2]
# Values: [10 20 30 40 50]

# Return value

print('\nReturn value')
arr = np.array([8, 3, 6])
indices = np.argsort(arr)
print('Indices:', indices)
print('Shape:', indices.shape)
print('Is integer:', np.issubdtype(indices.dtype, np.integer))

# Expected output:
# Indices: [1 2 0]
# Shape: (3,)
# Is integer: True

# Difference between sort and argsort

print('\nDifference between sort and argsort')
arr = np.array([8, 3, 6])
print('np.sort:', np.sort(arr))
print('np.argsort:', np.argsort(arr))
print('Original:', arr)
result = arr.sort()
print('After arr.sort:', arr)
print('Return from arr.sort:', result)

# Expected output:
# np.sort: [3 6 8]
# np.argsort: [1 2 0]
# Original: [8 3 6]
# After arr.sort: [3 6 8]
# Return from arr.sort: None

# Ascending and descending order

print('\nAscending and descending order')
arr = np.array([8, 3, 6])
ascending = np.argsort(arr)
descending = ascending[::-1]
print('Ascending indices:', ascending)
print('Ascending values:', arr[ascending])
print('Descending indices:', descending)
print('Descending values:', arr[descending])

# Expected output:
# Ascending indices: [1 2 0]
# Ascending values: [3 6 8]
# Descending indices: [0 2 1]
# Descending values: [8 6 3]

# Sorting along axes

print('\nSorting along axes')
arr = np.array([[9, 2, 7], [4, 8, 1]])
row_indices = np.argsort(arr, axis=1)
column_indices = np.argsort(arr, axis=0)
print('Row indices:\n', row_indices)
print('Sorted rows:\n', np.take_along_axis(arr, row_indices, axis=1))
print('Column indices:\n', column_indices)
print('Sorted columns:\n', np.take_along_axis(arr, column_indices, axis=0))

# Expected output:
# Row indices:
#  [[1 2 0]
#  [2 0 1]]
# Sorted rows:
#  [[2 7 9]
#  [1 4 8]]
# Column indices:
#  [[1 0 1]
#  [0 1 0]]
# Sorted columns:
#  [[4 2 1]
#  [9 8 7]]

# Part 2 - Working with argsort()
# Sort a one dimensional array

print('\nSort a one dimensional array')
arr = np.array([30, 10, 50, 20, 40])
indices = np.argsort(arr)
print(arr[indices])

# Expected output:
# [10 20 30 40 50]

# Sort in descending order

print('\nSort in descending order')
arr = np.array([30, 10, 50, 20, 40])
indices = np.argsort(arr)[::-1]
print(arr[indices])

# Expected output:
# [50 40 30 20 10]

# Sort each row

print('\nSort each row')
arr = np.array([[9, 2, 7], [4, 8, 1]])
indices = np.argsort(arr, axis=1)
result = np.take_along_axis(arr, indices, axis=1)
print('Indices:\n', indices)
print('Result:\n', result)

# Expected output:
# Indices:
#  [[1 2 0]
#  [2 0 1]]
# Result:
#  [[2 7 9]
#  [1 4 8]]

# Sort each column

print('\nSort each column')
arr = np.array([[9, 2, 7], [4, 8, 1]])
indices = np.argsort(arr, axis=0)
result = np.take_along_axis(arr, indices, axis=0)
print('Indices:\n', indices)
print('Result:\n', result)

# Expected output:
# Indices:
#  [[1 0 1]
#  [0 1 0]]
# Result:
#  [[4 2 1]
#  [9 8 7]]

# Rearrange using returned indices

print('\nRearrange using returned indices')
names = np.array(['A', 'B', 'C'])
values = np.array([30, 10, 20])
indices = np.argsort(values)
print('Indices:', indices)
print('Rearranged names:', names[indices])
print('Rearranged values:', values[indices])

# Expected output:
# Indices: [1 2 0]
# Rearranged names: ['B' 'C' 'A']
# Rearranged values: [10 20 30]

# Compare outputs

print('\nCompare outputs')
arr = np.array([30, 10, 50, 20, 40])
indices = np.argsort(arr)
print('sort:', np.sort(arr))
print('argsort:', indices)
print('arr[indices]:', arr[indices])

# Expected output:
# sort: [10 20 30 40 50]
# argsort: [1 3 0 4 2]
# arr[indices]: [10 20 30 40 50]

# Part 3 - Applications of argsort()
# Find the smallest and largest indices

print('\nFind the smallest and largest indices')
arr = np.array([30, 10, 50, 20, 40])
indices = np.argsort(arr)
print('Smallest index:', indices[0])
print('Smallest value:', arr[indices[0]])
print('Largest index:', indices[-1])
print('Largest value:', arr[indices[-1]])

# Expected output:
# Smallest index: 1
# Smallest value: 10
# Largest index: 2
# Largest value: 50

# Find the top K largest elements

print('\nFind the top K largest elements')
arr = np.array([30, 10, 50, 20, 40])
k = 3
indices = np.argsort(arr)[::-1][:k]
print('Indices:', indices)
print('Largest values:', arr[indices])

# Expected output:
# Indices: [2 4 0]
# Largest values: [50 40 30]

# Find the top K smallest elements

print('\nFind the top K smallest elements')
arr = np.array([30, 10, 50, 20, 40])
k = 3
indices = np.argsort(arr)[:k]
print('Indices:', indices)
print('Smallest values:', arr[indices])

# Expected output:
# Indices: [1 3 0]
# Smallest values: [10 20 30]

# Rank students by grades

print('\nRank students by grades')
students = np.array(['Ali', 'Mona', 'Omar', 'Sara'])
grades = np.array([75, 90, 85, 90], dtype=float)
indices = np.argsort(-grades, kind='stable')
for rank, index in enumerate(indices, start=1):
    print(rank, students[index], int(grades[index]))
    
# Expected output:
# 1 Mona 90
# 2 Sara 90
# 3 Omar 85
# 4 Ali 75

# Rank products by prices

print('\nRank products by prices')
products = np.array(['Mouse', 'Keyboard', 'Monitor'])
prices = np.array([350, 800, 5000])
indices = np.argsort(prices)
for rank, index in enumerate(indices, start=1):
    print(rank, products[index], prices[index])
    
# Expected output:
# 1 Mouse 350
# 2 Keyboard 800
# 3 Monitor 5000

# Sort one array based on another

print('\nSort one array based on another')
names = np.array(['Ali', 'Mona', 'Omar'])
ages = np.array([22, 19, 21])
indices = np.argsort(ages)
print('Names:', names[indices])
print('Ages:', ages[indices])

# Expected output:
# Names: ['Mona' 'Omar' 'Ali']
# Ages: [19 21 22]


# Sort records and preserve original indices

print('\nSort records and preserve original indices')
records = np.array([['Ali', '75'], ['Mona', '90'], ['Omar', '85']])
grades = records[:, 1].astype(float)
indices = np.argsort(grades)
for original_index in indices:
    print('Original row:', original_index, 'Record:', records[original_index])
    
# Expected output:
# Original row: 0 Record: ['Ali' '75']
# Original row: 2 Record: ['Omar' '85']
# Original row: 1 Record: ['Mona' '90']

# Retrieve original positions of sorted values

print('\nRetrieve original positions of sorted values')
arr = np.array([40, 10, 40, 20])
indices = np.argsort(arr, kind='stable')
sorted_values = arr[indices]
for i in range(len(arr)):
    print('Value:', sorted_values[i], 'Original index:', indices[i])
# The inverse permutation restores the initial order.
inverse = np.argsort(indices)
print('Restored:', sorted_values[inverse])

# Expected output:
# Value: 10 Original index: 1
# Value: 20 Original index: 3
# Value: 40 Original index: 0
# Value: 40 Original index: 2
# Restored: [40 10 40 20]

# Part 4 - Sort using multiple keys
# lexsort returns positions using several keys. The last key is the main key. Problem:
# sort products by category, then by price within each category. Category is therefore the
# last key below.
# Expected output:
# Indices: [2 1 3 0]
# A 10
# A 30
# B 15
# B 20
print('\nSort using multiple keys')
categories = np.array(['B', 'A', 'A', 'B'])
prices = np.array([20, 30, 10, 15])
indices = np.lexsort((prices, categories))
print('Indices:', indices)
for index in indices:
    print(categories[index], prices[index])

