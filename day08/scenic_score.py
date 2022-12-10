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

def vis_distance(th):
    vd = 0
    h0 = th[0]
    for t in th[1:]:
        vd += 1
        if t >= h0:
            break
    return vd

max_sc = -1
for r in range(n_rows):
    for c in range(n_cols):
        ths = []
        # to the East
        ths.append(tree_heights[r,c:])
        # to the West
        ths.append(tree_heights[r,c::-1])
        # to the North
        ths.append(tree_heights[r::-1,c])
        # to the South
        ths.append(tree_heights[r:,c])

        sc = 1
        for th in ths:
            vd = vis_distance(th)
            sc *= vd
        if sc > max_sc:
            max_sc = sc

print('Max scenic score: %d' % max_sc)