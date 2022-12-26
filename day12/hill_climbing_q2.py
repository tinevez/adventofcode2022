#!python3
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def add_edge_maybe(G, s, t, img):
    if (t[0] < 0) or (t[1] < 0) or (t[0] >= img.shape[0]) or (t[1] >= img.shape[1]): 
        return
    diff = img[t] - img[s]
    if diff <= 1:
        G.add_edge(s, t)

if __name__ == "__main__":
    # file_path = 'input_test.txt'
    file_path = 'input.txt'
    index = -1
    arr = []
    with open(file_path, 'r') as f:
        for l in f:
            line = l.strip()
            width = len(line)
            for c in line:
                index += 1
                if c == 'S':
                    index_start = index
                    val = 0
                elif c == 'E':
                    index_finish = index
                    val = 25
                else:
                    val = ord(c)-ord('a')
                arr.append(val)
    img = np.array(arr, dtype=np.int64)
    img = np.reshape(img, [-1, width])
    sv = ( index_start // width, index_start % width )
    tv = ( index_finish // width, index_finish % width )

    G = nx.DiGraph()    
    for r in range(img.shape[0]):
        for c in range(img.shape[1]):
            add_edge_maybe(G, (r,c), (r-1,c), img) # North
            add_edge_maybe(G, (r,c), (r+1,c), img) # South
            add_edge_maybe(G, (r,c), (r,c-1), img) # West
            add_edge_maybe(G, (r,c), (r,c+1), img) # East

    min_path_length = 1_000_000_000
    for r in range(img.shape[0]):
        for c in range(img.shape[1]):
            if img[r][c] == 0:
                try:
                    spv = nx.shortest_path(G, (r,c), tv)
                    pl = len(spv)
                    if pl < min_path_length:
                        min_path_length = pl
                except nx.NetworkXNoPath:
                    pass

    print('Length of shortest path: %d' % (min_path_length-1))
