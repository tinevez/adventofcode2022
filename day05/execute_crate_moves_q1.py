import re

#----------------------------------
# Load starting crate arrangement.
#----------------------------------

# Find the number of stacks
stack_height = 0
with open('input.txt', 'r') as f:
    for line in f:
        if all(char.isdigit() or char.isspace() for char in line):
            tokens = line.strip().split()
            n_stacks = max( [ int(i.strip()) for i in tokens ])
            break
        stack_height += 1
print('Found %d stacks. Max height is %d' % (n_stacks, stack_height))

# Initialize the empty stacks.
stacks = []
for i in range(n_stacks):
    stacks.append([])

# Feed the stacks.
with open('input.txt', 'r') as f:
    for r in range(stack_height):
        line = f.readline()
        characters = re.findall(r"\[(.*?)\]| {3}", line)
        for c in range(n_stacks):
            if characters[c]:
                stacks[c].append(characters[c])

# Invert them (so that last char is on top).
for c in range(n_stacks):
    stacks[c].reverse()


#-----------------------------------------------------
# Perform crate re-arrangement according to give plan.
#-----------------------------------------------------

print('Before re-arrangement:')
for stack in stacks:
    print(stack)

with open('input.txt', 'r') as f:
    # Skip initial lines
    for r in range(stack_height+1):
        f.readline()
        continue
    for line in f:
        if not line.strip():
            continue
        numbers = re.findall(r'\d+', line.strip())
        amount      = int(numbers[0])
        from_stack  = int(numbers[1]) - 1
        to_stack    = int(numbers[2]) - 1
        
        for i in range(amount):
            val = stacks[from_stack].pop()
            stacks[to_stack].append(val)

print('After re-arrangement:')
for stack in stacks:
    print(stack)

