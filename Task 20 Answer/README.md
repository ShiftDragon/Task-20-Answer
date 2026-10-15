# Session 20 NumPy Sorting Examples

This project explains NumPy sorting examples in `Session_20_Argsort.py`. It focuses on `argsort`, which returns the original positions of values in sorted order. These positions let you sort related information, such as student names and grades, together.

## Requirements

- Python 
- NumPy 

## How to run

1. Download `Session_20_Argsort.py` and place it in a folder.
2. Open a terminal in that folder.
3. Install NumPy:

   ```bash
   python -m pip install "numpy"
   ```

4. Run the file:

   ```bash
   python Session_20_Argsort.py
   ```

## What the file covers

| Part | Examples |
| --- | --- |
| Part 1: Understanding argsort | Returned indices, syntax, return type, differences from sort, ascending and descending order, and sorting along axes. |
| Part 2: Using argsort | Sorting a 1D array, descending order, sorting rows and columns, rearranging related arrays, and comparing outputs. |
| Part 3: Applications | Smallest and largest positions, top K values, ranking students and products, sorting one array using another, preserving record positions, and restoring original order. |
| Part 4: Multiple sorting keys | Sorting products by category and then by price using lexsort. |

## Example output

The first example uses:

```python
import numpy as np

arr = np.array([30, 10, 50, 20, 40])
indices = np.argsort(arr)
print('Indices:', indices)
print('Values:', arr[indices])
```

Its output is:

```text
Indices: [1 3 0 4 2]
Values: [10 20 30 40 50]
```

Index `1` contains `10`, the smallest value. Index `3` contains `20`, the next smallest value. Selecting `arr[indices]` returns all values in ascending order. NumPy indices start at zero.

## Key ideas

- `np.sort(arr)` returns sorted values in a new array.
- `np.argsort(arr)` returns the positions needed to put values in order.
- `arr[indices]` selects 1D values using those positions.
- `arr.sort()` changes the original array and returns `None`.
- For a 2D array, `axis=1` sorts across each row, while `axis=0` sorts down each column. The script uses `np.take_along_axis` to apply the returned indices along the matching axis.
- A stable sort keeps equal values in their original order.
- In `np.lexsort((prices, categories))`, the last key, `categories`, is the main sorting key. Prices determine the order within each category.

## How the student ranking works

The student example uses:

```python
indices = np.argsort(-grades, kind='stable')
```

The negative sign makes higher original grades come first: `-90` sorts before `-75`. It creates negative values for sorting while leaving the original grades unchanged. `kind='stable'` keeps students with the same grade in their original order.

For the example data, the result is:

```text
1 Mona 90
2 Sara 90
3 Omar 85
4 Ali 75
```

Mona stays before Sara because Mona appeared first in the original list. The printed numbers are positions in the sorted list. Students with equal grades still receive consecutive position numbers.