
# 0 for right  >
# 1 for down   v
# 2 for left   <
# 3 for up     ^

# 90 degrees turns
#        R   clockwise
#        L   counterclockwise

input_file = 'day_22.txt'


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
    new_direction = direction

    # if direction is right >
    if direction == 0:
        # if position is at the end of line
        if x == 149:
            y_temp = 149 - y
            x_temp = 99
            new_direction = 2
        elif x == 99 and y >= 50:
            if y <= 99:
                y_temp = 49
                x_temp = y + 50
                new_direction = 3
            else:
                y_temp = 149 - y
                x_temp = 149
                new_direction = 2
        elif x == 49 and y >= 150:
            y_temp = 149
            x_temp = y - 100
            new_direction = 3
        else:
            y_temp = y
            x_temp = x+1
        # if next tile is # (no way)
        if board_map[y_temp][x_temp] == '#':
            # no change - no movement
            return [y, x], direction
        elif board_map[y_temp][x_temp] == '.':
            # forward one step right >
            return [y_temp, x_temp], new_direction

    # if direction is downward v
    elif direction == 1:
        # if position is at the end of column
        if x >= 100 and y == 49:
            y_temp = x - 50
            x_temp = 99
            new_direction = 2
        elif x >= 50 and y == 149:
            y_temp = x + 100
            x_temp = 49
            new_direction = 2
        elif y == 199:
            y_temp = 0
            x_temp = x + 100
        # if there is tiles downward from current position
        else:
            y_temp = y + 1
            x_temp = x
        # if next tile is # (no way)
        if board_map[y_temp][x_temp] == '#':
            # no change - no movement
            return [y, x], direction
        elif board_map[y_temp][x_temp] == '.':
            # forward one step downward v
            return [y_temp, x_temp], new_direction

    # if direction is left <
    elif direction == 2:
        # if position is at the beginning of line
        if x == 50 and y <= 49:
            y_temp = 149 - y
            x_temp = 0
            new_direction = 0
        elif x == 50 and y <= 99:
            y_temp = 100
            x_temp = y - 50
            new_direction = 1
        elif x == 0 and y <= 149:
            y_temp = 149 - y
            x_temp = 50
            new_direction = 0
        elif x == 0 and y <= 199:
            y_temp = 0
            x_temp = y - 100
            new_direction = 1
        # if there is tiles before current position
        else:
            x_temp = x - 1
            y_temp = y
        # if previous tile is # (no way)
        if board_map[y_temp][x_temp] == '#':
            # no change - no movement
            return [y, x], direction
        elif board_map[y_temp][x_temp] == '.':
            # forward one step left <
            return [y_temp, x_temp], new_direction

    # if direction is up ^
    elif direction == 3:
        # if position is at the beginning of column
        if y == 0 and x >= 100:
            y_temp = 199
            x_temp = x - 100
            new_direction = 3
        elif y == 0 and x >= 50:
            y_temp = x + 100
            x_temp = 0
            new_direction = 0
        elif y == 100 and x <= 49:
            y_temp = x + 50
            x_temp = 50
            new_direction = 0
        # if there is tiles upward from current position
        else:
            y_temp = y - 1
            x_temp = x
        # if upward tile is # (no way)
        if board_map[y_temp][x_temp] == '#':
            # no change - no movement
            return [y, x], direction
        elif board_map[y_temp][x_temp] == '.':
            # forward one step upward ^
            return [y_temp, x_temp], new_direction


def do_instruction(board_map, instruction, position, direction):
    if instruction == 'L':
        new_direction = (direction-1) % 4
        return position, new_direction
    if instruction == 'R':
        new_direction = (direction+1) % 4
        return position, new_direction

    new_position = position
    for i in range(instruction):
        new_position, direction = forward_one_step(board_map, new_position, direction)

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
    password = find_final_password(input_file)

    print(f"Final Password:   {password}")
    