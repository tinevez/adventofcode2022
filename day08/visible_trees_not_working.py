import numpy as np
from file_read_backwards import FileReadBackwards

'''
Solution that tries very hard not to read the full file in memory.
Otherwise I would have loaded the data as an image, and apply
4 rotations with one method.

This does not work and overestimates the number of tree. I do 
not know why. 

DOH! YES IT WORKS! I simply did not have the right input...
'''

def process_line(line, v):
    max_val = -1
    col = 0
    for c in line:
        val = int(c)
        if val > max_val:
            v[col] = True
            max_val = val
        col += 1

def process_cols(line, v, max_val_cols):
    col = 0
    for c in line:
        val = int(c)
        if val > max_val_cols[col]:
            v[col] = True
            max_val_cols[col] = val
        col +=1 

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

# Visibility 2D array.
visibles = np.zeros((n_rows, n_cols), dtype=bool)

# Top to bottom, left to right and right to left.
max_val_cols = np.ones([n_cols], dtype=int) * -1
with open(file_name, 'r') as f:
    r = 0
    for l in f:
        line = l.strip()
        visible_row = visibles[r]
        process_line(line, visible_row)
        process_line(line[::-1], visible_row[::-1])
        process_cols(line, visible_row, max_val_cols)
        r += 1

# Bottom to top.
max_val_cols = np.ones([n_cols], dtype=int) * -1
with FileReadBackwards(file_name) as f:
    r = n_rows
    for l in f:
        line = l.strip()
        r -= 1
        visible_row = visibles[r]
        process_cols(line, visible_row, max_val_cols)

print('There are %d visible trees.' % np.sum(visibles))