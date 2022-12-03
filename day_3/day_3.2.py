
file_name = 'day_3.txt'
# file_name = 'test.txt'


letters = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26, 'A': 27, 'B': 28, 'C': 29, 'D': 30, 'E': 31, 'F': 32, 'G': 33, 'H': 34, 'I': 35, 'J': 36, 'K': 37, 'L': 38, 'M': 39, 'N': 40, 'O': 41, 'P': 42, 'Q': 43, 'R': 44, 'S': 45, 'T': 46, 'U': 47, 'V': 48, 'W': 49, 'X': 50, 'Y': 51, 'Z': 52}


def find_badge(line1, line2, line3):
    line1_dict = {}
    for i in line1:
        line1_dict[i] = True
    
    line2_dict = {}
    for i in line2:
        if line1_dict.get(i, False):
            line2_dict[i] = True
    
    for i in line3:
        if line2_dict.get(i, False):
            return i


total_priority = 0

with open(file_name, 'r') as file:
    counter = -1
    group = [str]*3

    for line in file:
        counter += 1
        group[counter] = line

        if counter == 2:
            letter = find_badge(group[0], group[1], group[2])
            total_priority += letters[letter]
            counter = -1


print(f"total priority:   {total_priority}")
