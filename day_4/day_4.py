
file_name = 'day_4.txt'
# file_name = 'test.txt.txt'  # test.txt input


def get_elves_assignments(line):

    elf_1, elf_2 = line.split(',')
    elf_2 = elf_2.split('\n')[0]  # for the reason that every line ends '\n' in file

    elf_1 = elf_1.split('-')
    elf_2 = elf_2.split('-')

    for i in range(2):
        elf_1[i] = int(elf_1[i])
        elf_2[i] = int(elf_2[i])
    
    return elf_1, elf_2


# Part I
def find_number_of_fully_contain_assignments(file_name):
    counter = 0

    with open(file_name, 'r') as file:
        for line in file:

            elf_1, elf_2 = get_elves_assignments(line)

            if elf_2[0] <= elf_1[0] and elf_1[1] <= elf_2[1]:
                counter += 1
            elif elf_1[0] <= elf_2[0] and elf_2[1] <= elf_1[1]:
                counter += 1
                
    return counter


# Part II
def find_overlaps_number(file_name):
    counter = 0

    with open(file_name, 'r') as file:
        for line in file:

            elf_1, elf_2 = get_elves_assignments(line)

            if elf_2[0] <= elf_1[1] and elf_1[0] <= elf_2[1]:
                counter += 1
            elif elf_1[0] <= elf_2[1] and elf_2[0] <= elf_1[1]:
                counter += 1

    return counter


if __name__ == '__main__':
    # Part I
    number = find_number_of_fully_contain_assignments(file_name)
    print(f"Part I \nNumber of assignment that fully contains each other:   {number}")
    
    # Part II
    overlaps_number = find_overlaps_number(file_name)
    print(f"\nPart II \nOverlaps number:   {overlaps_number}")
    