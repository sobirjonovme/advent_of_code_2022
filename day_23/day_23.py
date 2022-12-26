
input_file = 'day_23.txt'
test_file = 'test.txt'


def get_elves_positions(file_name):
    with open(file_name, 'r') as file:
        positions = []
        y = -1
        for line in file:
            x = 1
            for pos in line:
                if pos == '#':
                    positions.append([x, y])
                x += 1
            y -= 1
        return positions


def is_8_positions_empty(elves_positions, elf_pos):
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            new_pos = [elf_pos[0]+i, elf_pos[1]+j]
            if new_pos in elves_positions:
                return False
    return True


def is_direction_empty(elves_positions, elf_pos, direction):
    if direction == 'north':
        for i in range(-1, 2):
            new_pos = [elf_pos[0]+i, elf_pos[1]+1]
            if new_pos in elves_positions:
                return False
        return [elf_pos[0], elf_pos[1]+1]
    if direction == 'south':
        for i in range(-1, 2):
            new_pos = [elf_pos[0]+i, elf_pos[1]-1]
            if new_pos in elves_positions:
                return False
        return [elf_pos[0], elf_pos[1]-1]
    if direction == 'west':
        for i in range(-1, 2):
            new_pos = [elf_pos[0]-1, elf_pos[1]+i]
            if new_pos in elves_positions:
                return False
        return [elf_pos[0]-1, elf_pos[1]]
    if direction == 'east':
        for i in range(-1, 2):
            new_pos = [elf_pos[0]+1, elf_pos[1]+i]
            if new_pos in elves_positions:
                return False
        return [elf_pos[0]+1, elf_pos[1]]


def do_one_round(elves_positions, directions):
    elves_new_positions = []

    for elf_pos in elves_positions:
        if is_8_positions_empty(elves_positions, elf_pos):
            elves_new_positions.append(elf_pos)
            continue
        new_pos = elf_pos[::]
        for direct in directions:
            temp = is_direction_empty(elves_positions, elf_pos, direct)
            if temp is not False:
                new_pos = temp
                break
        elves_new_positions.append(new_pos[::])

    for i in range(len(elves_new_positions)):
        if elves_new_positions.count(elves_new_positions[i]) == 1:
            elves_positions[i] = elves_new_positions[i][::]

    return elves_positions


def get_empty_grounds_number(file_name):
    directions = ['north', 'south', 'west', 'east']
    elves_positions = get_elves_positions(file_name)

    for i in range(10):
        elves_positions = do_one_round(elves_positions, directions)
        directions.append(directions.pop(0))

    top, bottom = elves_positions[0][1], elves_positions[0][1]
    left, right = elves_positions[0][0], elves_positions[0][0]

    for pos in elves_positions:
        if pos[0] >= right:
            right = pos[0]
        if pos[0] <= left:
            left = pos[0]
        if pos[1] >= top:
            top = pos[1]
        if pos[1] <= bottom:
            bottom = pos[1]

    empty_grounds = (right-left+1)*(top-bottom+1) - len(elves_positions)

    return empty_grounds


def do_one_round_part_2(elves_positions, directions):
    elves_new_positions = []

    for elf_pos in elves_positions:
        if is_8_positions_empty(elves_positions, elf_pos):
            elves_new_positions.append(elf_pos)
            continue
        new_pos = elf_pos[::]

        for direct in directions:
            temp = is_direction_empty(elves_positions, elf_pos, direct)
            if temp is not False:
                new_pos = temp
                break
        elves_new_positions.append(new_pos[::])

    is_move = False
    for i in range(len(elves_new_positions)):
        if elves_new_positions.count(elves_new_positions[i]) == 1:
            if elves_new_positions[i] != elves_positions[i]:
                elves_positions[i] = elves_new_positions[i][::]
                is_move = True

    if is_move:
        return elves_positions

    return False


def find_no_movement_round_number(file_name):
    directions = ['north', 'south', 'west', 'east']
    elves_positions = get_elves_positions(file_name)

    i = 1
    while True:
        elves_positions = do_one_round_part_2(elves_positions, directions)

        if elves_positions is False:
            break

        directions.append(directions.pop(0))
        i += 1
        print(i)

    return i


if __name__ == '__main__':
    # # PART I
    # empty_grounds = get_empty_grounds_number(input_file)
    # # empty_grounds = get_empty_grounds_number(test_file)
    #
    # print(f"Empty grounds after 10th round: {empty_grounds}")
    #
    # PART II
    round_number = find_no_movement_round_number(input_file)
    # round_number = find_no_movement_round_number(test_file)

    print(f"No Change round number:   {round_number}")
