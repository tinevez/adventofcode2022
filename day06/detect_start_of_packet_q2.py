import collections

msg_size = 14

buffer = collections.deque(maxlen=msg_size)
i = 0
with open('input.txt', 'r') as f:
    while True:
         
        # Read from file
        c = f.read(1)
        if not c:
            break

        i += 1
        buffer.append(c)
        if len(buffer) >= msg_size:
            if len(set(buffer)) == len(buffer):
                print('First start-of-packet marker: %d' % i)
                break
