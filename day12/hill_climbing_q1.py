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
    print(img)
    print('Start vertex: [%d, %d]' % sv)
    print('End vertex:   [%d, %d]' % tv)

    G = nx.DiGraph()
    for r in range(img.shape[0]):
        for c in range(img.shape[1]):
            add_edge_maybe(G, (r,c), (r-1,c), img) # North
            add_edge_maybe(G, (r,c), (r+1,c), img) # South
            add_edge_maybe(G, (r,c), (r,c-1), img) # West
            add_edge_maybe(G, (r,c), (r,c+1), img) # East

    spv = nx.shortest_path(G, sv, tv)
    spe = []
    for i in range(len(spv)-1):
        spe.append((spv[i], spv[i+1]))
    print('Length of shortest path: %d' % (len(spv)-1))

    # Display
    pos = {point: point for point in G.nodes}
    # nx.draw(G, pos=pos)
    # nx.draw_networkx_nodes(G, pos=pos, nodelist=spv, node_color='r')
    nx.draw_networkx_edges(G, pos=pos, edgelist=spe, edge_color='r',width=1, node_size=1)
    plt.show()