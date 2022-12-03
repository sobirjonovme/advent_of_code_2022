
file_name = "day_1.txt"

elf_number = 1
i = 1

max_calories = 0
elf_calories = 0

elves_calories = [] # list of all elves'calories

# read file input line by line via for loop
with open(file_name, 'r') as file:
    for line in file:
        if line == '\n': # file'dan o'qiganimiz uchun, aks holda bo'sh string bn solishtirish kerak edi
            if max_calories < elf_calories:
                max_calories = elf_calories
                elf_number = i
            elves_calories.append(elf_calories) # list of all elves' calories
            
            elf_calories = 0
            i += 1 # just to know elf number
        else:
            elf_calories += int(line)

if max_calories < elf_calories:
    max_calories = elf_calories
    elf_number = i

elves_calories.append(elf_calories) # list of all elves'calories

print(f"elf number:   {elf_number}")
print(f"elf calories:   {max_calories}")
# print(elves_calories) # no need for problem
elves_calories.sort()

top_three_total = elves_calories[-1] + elves_calories[-2] + elves_calories[-3]
print(f"Top three total calories:   {top_three_total}")
