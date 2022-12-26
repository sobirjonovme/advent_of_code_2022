from pprint import pprint
import sys
import threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

import time


input_file = 'day_24.txt'
test_file = 'test.txt'


def get_input_data(file_name):
    rightward_blizzards = []
    leftward_blizzards = []
    upward_blizzards = []
    downward_blizzards = []

    with open(file_name, 'r') as file:
        y = -1
        for line in file:
            x = 1
            for symbol in line:
                if symbol == '>':
                    rightward_blizzards.append([x, y])
                elif symbol == '<':
                    leftward_blizzards.append([x, y])
                elif symbol == '^':
                    upward_blizzards.append([x, y])
                elif symbol == 'v':
                    downward_blizzards.append([x, y])
                x += 1
            y -= 1

    return [rightward_blizzards, leftward_blizzards, upward_blizzards, downward_blizzards], -y-1, x-1


def move_blizzards(blizzards, height, width):

    # right ward blizzards
    for i in range(len(blizzards[0])):
        if blizzards[0][i][0] == (width-1):
            blizzards[0][i][0] = 2
        else:
            blizzards[0][i][0] += 1

    # left ward blizzards
    for i in range(len(blizzards[1])):
        if blizzards[1][i][0] == 2:
            blizzards[1][i][0] = (width-1)
        else:
            blizzards[1][i][0] -= 1

    # up ward blizzards
    for i in range(len(blizzards[2])):
        if blizzards[2][i][1] == -2:
            blizzards[2][i][1] = -(height-1)
        else:
            blizzards[2][i][1] += 1
    # up ward blizzards
    for i in range(len(blizzards[3])):
        if blizzards[3][i][1] == -(height-1):
            blizzards[3][i][1] = -2
        else:
            blizzards[3][i][1] -= 1

    return blizzards


def find_min_required_minutes(blizzs, x_pos, y_pos, counter, height, width, extra_con):
    if x_pos == (width-1) and y_pos == -(height-1):
        print(f"Counter return: {counter}")
        # print(f"positions: {x_pos}, {y_pos}")
        return counter
    # print(counter)
    # print(x_pos, y_pos)
    # pprint(blizzs)
    # time.sleep(0.5)
    counter += 1
    blizzards = []
    for i in range(len(blizzs)):
        blizzards.append([])
        for j in range(len(blizzs[i])):
            blizzards[i].append(blizzs[i][j][::])
    blizzards = move_blizzards(blizzards, height, width)
    minutes = []
    # print("after movement")
    # pprint(blizzards)

    if extra_con >= 3:
        return None

    # right >
    new_pos = [x_pos+1, y_pos]
    if x_pos < (width-1) and new_pos not in blizzards[0] and new_pos not in blizzards[1]\
            and new_pos not in blizzards[2] and new_pos not in blizzards[3]:
        temp_counter = find_min_required_minutes(blizzards, x_pos+1, y_pos, counter, height, width, 0)
        if temp_counter is not None:
            minutes.append(temp_counter)
    # down v
    new_pos = [x_pos, y_pos-1]
    if y_pos > -(height-1) and new_pos not in blizzards[0] and new_pos not in blizzards[1]\
            and new_pos not in blizzards[2] and new_pos not in blizzards[3]:
        temp_counter = find_min_required_minutes(blizzards, x_pos, y_pos-1, counter, height, width, 0)
        if temp_counter is not None:
            minutes.append(temp_counter)

    # wait
    new_pos = [x_pos, y_pos]
    if new_pos not in blizzards[0] and new_pos not in blizzards[1]\
            and new_pos not in blizzards[2] and new_pos not in blizzards[3]:
        temp_counter = find_min_required_minutes(blizzards, x_pos, y_pos, counter, height, width, extra_con)
        if temp_counter is not None:
            minutes.append(temp_counter)

    # up ^
    new_pos = [x_pos, y_pos+1]
    if y_pos < -2 and new_pos not in blizzards[0] and new_pos not in blizzards[1]\
            and new_pos not in blizzards[2] and new_pos not in blizzards[3]:
        temp_counter = find_min_required_minutes(blizzards, x_pos, y_pos+1, counter, height, width, extra_con+1)
        if temp_counter is not None:
            minutes.append(temp_counter)
    # left <
    new_pos = [x_pos-1, y_pos]
    if x_pos > 2 and new_pos not in blizzards[0] and new_pos not in blizzards[1]\
            and new_pos not in blizzards[2] and new_pos not in blizzards[3]:
        temp_counter = find_min_required_minutes(blizzards, x_pos-1, y_pos, counter, height, width, extra_con+1)
        if temp_counter is not None:
            minutes.append(temp_counter)

    # print(f"minutes {minutes}")

    if len(minutes) == 0:
        return None

    return min(minutes)


def is_arrived(pos, height, width):
    if pos[0] == (width - 1) and pos[1] == -(height - 1):
        return True
    return False


def find_required_minutes(file_name):
    blizzards, height, width = get_input_data(file_name)

    # x_pos, y_pos = 2, -1
    x_pos, y_pos = 2, -2
    counter_1 = 0

    while True:
        blizzards = move_blizzards(blizzards, height, width)
        counter_1 += 1
        if [2, -2] not in blizzards[0] and [2, -2] not in blizzards[1] \
                and [2, -2] not in blizzards[2] and [2, -2] not in blizzards[3]:
            break

    print(find_min_required_minutes(blizzards, 2, -2, counter_1, height, width, 0))

    # elf_positions = [[2, -2], ]
    # children = 0
    # max_children = 1
    # counter_2 = 0
    # blizzards = move_blizzards(blizzards, height, width)
    #
    # while True:
    #     children += 1
    #     print(children)
    #
    #     # print(counter)
    #     if elf_positions[0] is None:
    #         continue
    #
    #     x_pos = elf_positions[0][0]
    #     y_pos = elf_positions[0][1]
    #
    #     # right >
    #     # new_pos = [x_pos + 1, y_pos]
    #     if x_pos < (width - 1) and [x_pos+1, y_pos] not in blizzards[0] and [x_pos + 1, y_pos] not in blizzards[1] \
    #             and [x_pos + 1, y_pos] not in blizzards[2] and [x_pos + 1, y_pos] not in blizzards[3]:
    #
    #         if is_arrived([x_pos+1, y_pos], height, width):
    #             break
    #         elf_positions.append([x_pos+1, y_pos])
    #     # else:
    #     #     elf_positions.append(None)
    #
    #     # wait
    #     # new_pos = [x_pos, y_pos]
    #     if [x_pos, y_pos] not in blizzards[0] and [x_pos, y_pos] not in blizzards[1] \
    #          and [x_pos, y_pos] not in blizzards[2] and [x_pos, y_pos] not in blizzards[3]:
    #         if is_arrived([x_pos, y_pos], height, width):
    #             break
    #         elf_positions.append([x_pos, y_pos])
    #     # else:
    #     #     elf_positions.append(None)
    #
    #     # down v
    #     # new_pos = [x_pos, y_pos - 1]
    #     if y_pos > -(height - 1) and [x_pos, y_pos - 1] not in blizzards[0] and [x_pos, y_pos - 1] not in blizzards[1] \
    #             and [x_pos, y_pos - 1] not in blizzards[2] and [x_pos, y_pos - 1] not in blizzards[3]:
    #         if is_arrived([x_pos, y_pos-1], height, width):
    #             break
    #         elf_positions.append([x_pos, y_pos-1])
    #     # else:
    #     #     elf_positions.append(None)
    #
    #     # up ^
    #     # new_pos = [x_pos, y_pos + 1]
    #     if y_pos < -2 and [x_pos, y_pos + 1] not in blizzards[0] and [x_pos, y_pos + 1] not in blizzards[1] \
    #             and [x_pos, y_pos + 1] not in blizzards[2] and [x_pos, y_pos + 1] not in blizzards[3]:
    #         if is_arrived([x_pos, y_pos+1], height, width):
    #             break
    #         elf_positions.append([x_pos, y_pos+1])
    #     # else:
    #     #     elf_positions.append(None)
    #
    #     # left <
    #     # new_pos = [x_pos - 1, y_pos]
    #     if x_pos > 2 and [x_pos - 1, y_pos] not in blizzards[0] and [x_pos - 1, y_pos] not in blizzards[1] \
    #             and [x_pos - 1, y_pos] not in blizzards[2] and [x_pos - 1, y_pos] not in blizzards[3]:
    #         if is_arrived([x_pos-1, y_pos], height, width):
    #             break
    #         elf_positions.append([x_pos-1, y_pos])
    #     # else:
    #     #     elf_positions.append(None)
    #
    #     # remove pos
    #     elf_positions.pop(0)
    #     if children == max_children:
    #         counter_2 += 1
    #         children = 0
    #         max_children *= 4
    #         blizzards = move_blizzards(blizzards, height, width)

    # if children == max_children:
    #     counter_2 += 1
    #     children = 0
    #     max_children *= 4

    # print(counter_1+counter_2)

    # pprint(blizzards)


if __name__ == '__main__':
    # find_required_minutes(test_file)
    find_required_minutes(input_file)
