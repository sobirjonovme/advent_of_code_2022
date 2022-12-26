
# 0 for right  >
# 1 for down   v
# 2 for left   <
# 3 for up     ^

# 90 degrees turns
#        R   clockwise
#        L   counterclockwise

input_file = 'day_22.txt'
test_file = 'test.txt'


def get_input_data(file_name):
    board_map = [[]]
    path = []

    with open(file_name, 'r') as file:
        data = file.read()

    part_1, part_2 = data.split('\n\n')

    for point in part_1:
        if point == '\n':
            board_map.append([])
            continue
        board_map[-1].append(point)

    instruction = ''
    for letter in part_2:
        if letter in ['L', 'R']:
            if instruction:
                path.append(int(instruction))
            instruction = ''
            path.append(letter)
        else:
            instruction += letter
    if instruction:
        path.append(int(instruction))

    return board_map, path


def find_column_beginning(board_map, column):
    for i in range(len(board_map)):
        if (len(board_map[i])-1) >= column:
            column_beginning = i
            break
    return column_beginning


def find_column_end(board_map, column):
    for i in range(len(board_map)):
        if (len(board_map[i])-1) >= column:
            column_end = i
    return column_end


def forward_one_step(board_map, position, direction):
    y, x = position[0], position[1]

    # if direction is right >
    if direction == 0:
        # if position is at the end of line
        if x == len(board_map[y])-1:
            x_temp = 0
            while board_map[y][x_temp] == ' ':
                x_temp += 1
            if board_map[y][x_temp] == '#':
                # no change - no movement
                return [y, x]
            elif board_map[y][x_temp] == '.':
                return [y, x_temp]
        # if there is tiles after current position
        else:
            # if next tile is # (no way)
            if board_map[y][x+1] == '#':
                # no change - no movement
                return [y, x]
            elif board_map[y][x+1] == '.':
                # forward one step right >
                return [y, x+1]

    # if direction is downward v
    elif direction == 1:
        # if position is at the end of column
        if y == find_column_end(board_map, x) or board_map[y+1][x] == ' ':
            y_temp = find_column_beginning(board_map, x)
            while board_map[y_temp][x] == ' ':
                y_temp += 1
            if board_map[y_temp][x] == '#':
                # no change - no movement
                return [y, x]
            elif board_map[y_temp][x] == '.':
                return [y_temp, x]
        # if there is tiles downward from current position
        else:
            # if next tile is # (no way)
            if board_map[y+1][x] == '#':
                # no change - no movement
                return [y, x]
            elif board_map[y+1][x] == '.':
                # forward one step downward v
                return [y+1, x]

    # if direction is left <
    elif direction == 2:
        # if position is at the beginning of line
        if x == 0 or board_map[y][x-1] == ' ':
            # print('\n test \n')
            line_end = len(board_map[y])-1
            if board_map[y][line_end] == '#':
                # no change - no movement
                return [y, x]
            elif board_map[y][line_end] == '.':
                return [y, line_end]
        # if there is tiles before current position
        else:
            # if previous tile is # (no way)
            if board_map[y][x - 1] == '#':
                # no change - no movement
                return [y, x]
            elif board_map[y][x - 1] == '.':
                # forward one step left <
                return [y, x - 1]

    # if direction is up ^
    elif direction == 3:
        # if position is at the beginning of column
        if y == find_column_beginning(board_map, x) or board_map[y-1][x] == ' ':
            # print('\n test \n')
            column_end = find_column_end(board_map, x)
            while board_map[column_end][x] == ' ':
                column_end -= 1
            if board_map[column_end][x] == '#':
                # no change - no movement
                return [y, x]
            elif board_map[column_end][x] == '.':
                return [column_end, x]
        # if there is tiles upward from current position
        else:
            # if upward tile is # (no way)
            if board_map[y-1][x] == '#':
                # no change - no movement
                return [y, x]
            elif board_map[y-1][x] == '.':
                # forward one step upward ^
                return [y-1, x]


def do_instruction(board_map, instruction, position, direction):
    if instruction == 'L':
        new_direction = (direction-1) % 4
        return position, new_direction
    if instruction == 'R':
        new_direction = (direction+1) % 4
        return position, new_direction

    new_position = position
    for i in range(instruction):
        new_position = forward_one_step(board_map, new_position, direction)

    return new_position, direction


def find_final_password(file_name):
    board_map, path = get_input_data(file_name)
    x = 0
    while board_map[0][x] == ' ':
        x += 1
    position = [0, x]
    direction = 0

    for instruction in path:
        position, direction = do_instruction(board_map, instruction, position, direction)

    password = (position[0]+1)*1000 + (position[1]+1)*4 + direction

    return password


if __name__ == '__main__':
    # password = find_final_password(test_file)
    password = find_final_password(input_file)

    print(f"Final Password:   {password}")
