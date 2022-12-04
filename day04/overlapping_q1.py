
def split_by(line, char):
    tokens = line.split(char)
    return tokens[0].strip(), tokens[1].strip()

def get_assignments(line):
    return split_by(line, ',')
    
def get_minmax(line):    
    strmin, strmax = split_by(line, '-')
    return int(strmin), int(strmax)


fully_overlapping = 0
with open('input.txt', 'r') as f:
    for line in f:
        elf1, elf2 = get_assignments(line)
        amin1, amax1 = get_minmax(elf1)
        amin2, amax2 = get_minmax(elf2)
        # print('elf 1: %2d -> %2d      elf 2: %2d -> %2d' % (amin1, amax1, amin2, amax2) )

        # Elf 1 assgn contained in elf 2 assgn or the converse.s
        if (amin1 >= amin2 and amax1 <= amax2) or  (amin1 <= amin2 and amax1 >= amax2):
            fully_overlapping += 1

print('Number of fully overlapping assignments: %d' % fully_overlapping)
