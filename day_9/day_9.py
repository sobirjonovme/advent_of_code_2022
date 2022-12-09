
file_name = 'day_9.txt'
# file_name = 'test.txt'


def move_tail(hx, hy, tx, ty):
    if abs(hx - tx) <= 1 and abs(hy - ty) <= 1:
        return tx, ty

    # condition 'vertical'
    if hy > ty:
        ty += 1
    elif hy < ty:
        ty -= 1

    # condition 'horizontal'
    if hx > tx:
        tx += 1
    elif hx < tx:
        tx -= 1

    return tx, ty


# Part I
def take_step_part_1(hx, hy, tx, ty, add_x, add_y, number, positions_list):

    for i in range(number):
        hx += add_x
        hy += add_y
        tx, ty = move_tail(hx, hy, tx, ty)

        if [tx, ty] not in positions_list:
            positions_list.append([tx, ty])

    return hx, hy, tx, ty, positions_list


def find_positions_part_1(file_name):

    with open(file_name, 'r') as file:

        # initial positions
        hx, hy, tx, ty = 0, 0, 0, 0
        positions_list = [[0, 0]]

        for line in file:
            line = line.split(' ')
            if line[0] == 'R':
                hx, hy, tx, ty, positions_list = take_step_part_1(hx, hy, tx, ty, 1, 0, int(line[1]), positions_list)
            elif line[0] == 'L':
                hx, hy, tx, ty, positions_list = take_step_part_1(hx, hy, tx, ty, -1, 0, int(line[1]), positions_list)
            elif line[0] == 'U':
                hx, hy, tx, ty, positions_list = take_step_part_1(hx, hy, tx, ty, 0, 1, int(line[1]), positions_list)
            elif line[0] == 'D':
                hx, hy, tx, ty, positions_list = take_step_part_1(hx, hy, tx, ty, 0, -1, int(line[1]), positions_list)

    return len(positions_list)


# Part II
def take_step_part_2(knot_postions, add_x, add_y, number, tail_positions):

    for i in range(number):
        knot_postions[0][0] += add_x
        knot_postions[0][1] += add_y
        for j in range(9):
            # print(j)
            tail_pos = move_tail(knot_postions[j][0], knot_postions[j][1], knot_postions[j+1][0], knot_postions[j+1][1])
            knot_postions[j+1] = list(tail_pos)
        if knot_postions[9] not in tail_positions:
            tail_positions.append(knot_postions[9])

    return knot_postions, tail_positions


def find_positions_part_2(file_name):

    with open(file_name, 'r') as file:

        # initial positions
        knot_positions = []
        for i in range(10):
            knot_positions.append([0, 0])
        tail_positions = [[0, 0]]

        for line in file:
            line = line.split(' ')
            if line[0] == 'R':
                knot_positions, tail_positions = take_step_part_2(knot_positions, 1, 0, int(line[1]), tail_positions)
            elif line[0] == 'L':
                knot_positions, tail_positions = take_step_part_2(knot_positions, -1, 0, int(line[1]), tail_positions)
            elif line[0] == 'U':
                knot_positions, tail_positions = take_step_part_2(knot_positions, 0, 1, int(line[1]), tail_positions)
            elif line[0] == 'D':
                knot_positions, tail_positions = take_step_part_2(knot_positions, 0, -1, int(line[1]), tail_positions)

    return len(tail_positions)


if __name__ == '__main__':
    # Part I
    print(f"Part I:   {find_positions_part_1(file_name)}")

    # Part II
    print(f"Part II: {find_positions_part_2(file_name)}")
