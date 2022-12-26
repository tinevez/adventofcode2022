#!/usr/bin/python3
import re
import inspect

#---------------------------------------------------------------
# CLASSES
#---------------------------------------------------------------

class Monkey():
    def __init__(self, 
            id,
            starting_objects, 
            operation,
            divisible_by,
            true_throw_to,
            false_throw_to):
        self.id                 = id
        self.objects            = starting_objects
        self.operation          = operation
        self.divisible_by       = divisible_by
        self.true_throw_to      = true_throw_to
        self.false_throw_to     = false_throw_to
        self.n_inspection       = 0
    
    def __str__(self):
        str = ('Monkey %d\n' % self.id)
        str += (' - objects: %s\n' % self.objects)
        str += (' - operation: %s\n' % inspect.getsource(self.operation).strip())
        str += (' - divisible by %d\n' % self.divisible_by)
        str += (' - if true throw to monkey #%d\n' % self.true_throw_to)
        str += (' - if false throw to monkey #%d\n' % self.false_throw_to)
        return str

class MonkeyCollection():
    def __init__(self, monkey_it):
        monkey_dict = {}
        for m in monkey_it:
            monkey_dict[m.id] = m
        self.monkey_dict = monkey_dict

    def __str__(self):
        str = ''
        for k in sorted(self.monkey_dict.keys()):
            m = self.monkey_dict[k]
            str += '%d -> %s' % (m.id, m)
        return str

    def print_object_list(self):
        str = ''
        for k in sorted(self.monkey_dict.keys()):
            m = self.monkey_dict[k]
            str += 'Monkey %d: %s\n' % (m.id, m.objects)
        return str

    def print_inspection(self):
        str = ''
        for k in sorted(self.monkey_dict.keys()):
            m = self.monkey_dict[k]
            str += 'Monkey %d inspected items %d times.\n' % (m.id, m.n_inspection)
        return str

    def monkey_business(self):
        ml = list(self.monkey_dict.values())
        sml = sorted(ml, key=lambda x: x.n_inspection, reverse=True)
        print(sml[0])
        print(sml[1])
        mb = 1
        for i in [0, 1]:
            m = sml[i]
            mb *= m.n_inspection
        return mb



    def turn_all(self):
        for id in sorted(self.monkey_dict.keys()):           
            self.turn(id)

    def turn(self, id):
        m = self.monkey_dict[id]
        print('Monkey %d:' % m.id)
        for i in range(len(m.objects)):
            obj = m.objects.pop(0)
            print('  Monkey inspects an item with a worry level of %d.' % obj)
            new_val = m.operation(obj)
            print('    Worry level is now %d.' % new_val)
            new_val = int(new_val / 3)
            print('    Monkey gets bored with item. Worry level is divided by 3 to %d.' % new_val)
            if new_val % m.divisible_by == 0:
                print('    Current worry level is divisible by %d.' % m.divisible_by)
                throw_to = m.true_throw_to
            else:
                print('    Current worry level is not divisible by %d.' % m.divisible_by)
                throw_to = m.false_throw_to
            print('    Item with worry level %d is thrown to monkey %d.' % (new_val, throw_to))
            target_monkey = self.monkey_dict[throw_to]
            target_monkey.objects.append(new_val)
            m.n_inspection += 1

#---------------------------------------------------------------
# READ FUNCTIONS
#---------------------------------------------------------------

pattern_monkey      = r'Monkey (\d+):'
pattern_starting    = r'\d+'
pattern_1_operation = r'([+*/-]) (\d+)$'
pattern_2_operation = r'([+*/-]) old$'
pattern_divisible   = r'\d+$'
pattern_true        = r'If true: throw to monkey (\d+)'
pattern_false       = r'If false: throw to monkey (\d+)'

def read_monkey(fo):
    
    # Monkey number.
    while True:
        line = fo.readline()
        if not line:
            return None
        match = re.match(pattern_monkey, line.strip())
        if match:
            break
    monkey_nbr = int(match.group(1))
    print('Reading monkey number: %d' % monkey_nbr)

    # Items.
    numbers = re.findall(pattern_starting, fo.readline().strip())
    starting_items = [ int(t) for t in numbers]
    # print(' . ', starting_items)

    # Operation.
    op_line = fo.readline().strip()
    match = re.search(pattern_1_operation, op_line)
    if match:
        op_str = match.group(1)
        op_val = int(match.group(2))
        # print(' . %s %d' % (op_str, op_val))
        if op_str == '+':
            operation = lambda x: x + op_val
        elif op_str == '-':
            operation = lambda x: x - op_val
        elif op_str == '*':
            operation = lambda x: x * op_val
        elif op_str == '/':
            operation = lambda x: x / op_val
        else:
            print('Unknown operation: %s %d' % (op_str, op_val))
    else:
        match = re.search(pattern_2_operation, op_line)
        if match:
            op_str = match.group(1)
            # print(' . %s old' % op_str)
            if op_str == '+':
                operation = lambda x: x + x
            elif op_str == '-':
                operation = lambda x: x - x
            elif op_str == '*':
                operation = lambda x: x * x
            elif op_str == '/':
                operation = lambda x: x / x
            else:
                print('Unknown operation: %s old' % op_str)
        else:
            print('Unknown operation type: %s' % op_line)

    
    # Test divisible
    match = re.search(pattern_divisible, fo.readline().strip())
    divisible = int(match.group())
    # print(' . divisible by %d' % divisible)

    # Throw to - true
    match = re.search(pattern_true, fo.readline().strip())
    throw_true = int(match.group(1))
    match = re.search(pattern_false, fo.readline().strip())
    throw_false = int(match.group(1))
    # print(' . true - throw to %s' % throw_true)
    # print(' . false - throw to %s' % throw_false)
    
    return Monkey(monkey_nbr, starting_items, operation, divisible, throw_true, throw_false)

def parse(file_path):
    monkeys = []
    with open(file_path, 'r') as fo:
        while True:
            monkey = read_monkey(fo)
            if monkey is None:
                return monkeys
            monkeys.append(monkey)

#---------------------------------------------------------------
# MAIN
#---------------------------------------------------------------

if __name__ == "__main__":
    # monkeys = MonkeyCollection(parse('input_test.txt'))
    monkeys = MonkeyCollection(parse('input.txt'))
    n_rounds = 20
    for i in range(n_rounds):
        monkeys.turn_all()
        print('\nAfter round %d:' % (i+1))
        print(monkeys.print_object_list())
    print(monkeys.print_inspection())
    print(monkeys.monkey_business())
    

