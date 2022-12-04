#!/usr/bin/python3
from itertools import islice

# Elf group size.
N = 3

# Number of groups 
ng = 0

sum_priorities = 0
with open('input.txt', 'r') as f:
    while True:
        
        # Read lines 3 by 3
        lines_gen = list(islice(f, N))
        if not lines_gen: # EOF
            break 

        ng += 1 
        group = []
        for line in lines_gen:
            content = line.strip()
            group.append(set(content))

        # Find common element.
        common_el = group[0]
        for i in range(1, N):
            common_el = common_el.intersection(group[i])

        if len(common_el) != 1:
            print('Problem with line %s' % group[0])
        
        # Get the score.
        for c in common_el:
            char_val = ord(c.lower()) - ord('a')
            if c == c.lower():
                char_val += 1
            else:
                char_val += 27

            sum_priorities += char_val
            print('%s -> %2d'% (c, char_val))

print('Found %d groups of %d elves.' % (ng, N))
print('Sum of priorities: %d' % sum_priorities)        
