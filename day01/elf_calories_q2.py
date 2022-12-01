total_calories = []
current_elf_calories = 0

with open('input.txt') as f:
    for line in f:
        str = line.strip()
        if str:
            cal = int(str)
            current_elf_calories = current_elf_calories + cal
        else:
            total_calories.append(current_elf_calories)
            current_elf_calories = 0

# Doh! Don't forget the last line.
total_calories.append(current_elf_calories)
total_calories.sort(reverse=True)
sum_calories = total_calories[0] + total_calories[1] + total_calories[2]

print('The total amount calories carried by the top 3 elves is: %d' % sum_calories)
