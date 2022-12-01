max_calories = -1
elf_with_max_calories = -1
elf_index = 0
current_elf_calories = 0

with open('input.txt') as f:
    for line in f:
        str = line.strip()
        if str:
            cal = int(str)
            current_elf_calories = current_elf_calories + cal
        else:
            if current_elf_calories > max_calories:
                max_calories = current_elf_calories
                elf_with_max_calories = elf_index
            # Increment and reset.
            elf_index = elf_index + 1
            current_elf_calories = 0

# Doh! Don't forget the last line!
if current_elf_calories > max_calories:
    max_calories = current_elf_calories
    elf_with_max_calories = elf_index

print('The elf with the most calories was the elf #%d, with a total amounf of calories %d' % (elf_with_max_calories, max_calories))
            