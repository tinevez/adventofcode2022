import re

# File to read.
file_name = 'input.txt'
# Pattern for 'noop' instruction
noop_pattern = r'noop'
# Pattern for 'addx' instruction
addx_pattern = r'addx (-?\d+)'
# What value should we add to the register at the end of each cycle.
values = []
# Sprite span
span = 1 # for a total size of 3 = 1 +/- 1
# The width of the 'screen'
width = 39

# Read all values to shift the register.
with open(file_name, 'r') as f:
    for line in f:

        command = line.strip()
        if re.match(noop_pattern, command):
            values.append(0)
            continue
        match = re.match(addx_pattern, command)
        if match:
            val = int(match.group(1))
            values.append(0)
            values.append(val)
        else:
            print('Unknown command: %s' % command)


X = 1
crt_pos = 0

line = []
for i in range(len(values)):
    if abs(crt_pos-X) <= span:
        line.append('#')
    else:
        line.append('.')

    val = values[i]
    X += val
    crt_pos += 1
    if crt_pos > width:
        print(''.join(line))
        line.clear()
        crt_pos = 0

print(''.join(line))
print('Done')