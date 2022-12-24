import re

# File to read.
file_name = 'input.txt'
# Pattern for 'noop' instruction
noop_pattern = r'noop'
# Pattern for 'addx' instruction
addx_pattern = r'addx (-?\d+)'
# The first cycle numbers at which we want to test
test_cycle = 20
test_increment = 40
test_stop = 220 # last one to test.

def measure_signal_strength(c, x, ts):
    if c >= ts:
        signal_strenth = ts * x
        print('Signal strength at cycle %d: %d x %d = %d' % (ts, ts, x, signal_strenth))
        return (signal_strenth, ts+test_increment)
    return (0, ts)



X = 1
cycle = 0
sum_signal_stength = 0

with open(file_name, 'r') as f:
    for line in f:

        command = line.strip()
        if re.match(noop_pattern, command):
            cycle += 1
            (strength, test_cycle) = measure_signal_strength(cycle, X, test_cycle)
            sum_signal_stength += strength
            continue
        match = re.match(addx_pattern, command)
        if match:
            cycle += 2
            (strength, test_cycle) = measure_signal_strength(cycle, X, test_cycle)
            sum_signal_stength += strength
            val = int(match.group(1))
            X += val
        else:
            print('Unknown command: %s' % command)

        if cycle > test_stop:
            break

print('Sum of the signal strength at measurement points: %d' % sum_signal_stength )
