#!/usr/bin/python3

sum_priorities = 0
with open('input.txt') as f:
    for line in f:
        content = line.strip()
        n = len(content)
        compartment_1 = set(content[:n//2])
        compartment_2 = set(content[n//2:])
        common_items = compartment_1.intersection(compartment_2)
        for c in common_items:
            # Get the score.
            char_val = ord(c.lower()) - ord('a')
            if c == c.lower():
                char_val += 1
            else:
                char_val += 27
            sum_priorities += char_val

print('Sum of priorities: %d' % sum_priorities)        
