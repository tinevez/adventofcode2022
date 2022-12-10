import numpy as np


# Input to play with.
# file_name = 'input_test.txt'
file_name = 'input.txt'


# Determine n_rows and n_cols
n_rows = 0
n_cols = 0
with open(file_name, 'r') as f:
    for l in f:
        n_rows += 1
    line = l.strip()
    n_cols = len(l)
print('Found a %d x %d forest.' % (n_rows, n_cols))

tree_heights = np.zeros([n_rows, n_cols], dtype=int)

with open(file_name, 'r') as f:
    row = 0
    for l in f:
        col = 0
        for c in l.strip():
            tree_heights[row][col] = int(c)
            col += 1
        row += 1

def process(ths, vis):
    num_rows, num_cols = ths.shape
    for row in range(num_rows):
        max_th = -1
        for col in range(num_cols):
            th = ths[row][col]
            if th > max_th:
                max_th = th
                vis[row][col] = True


visibility = np.zeros([n_rows, n_cols], dtype=bool)
# Transpose 3 times.
current_v = visibility
current_th = tree_heights
for i in range(4):
    process(current_th, current_v)
    current_th = np.rot90(current_th)
    current_v = np.rot90(current_v)


print(visibility)

print('There are %d visible trees.' % np.sum(visibility))