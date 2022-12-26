from pprint import pprint

input_file = 'day_18.txt'
test_file = 'test.txt'


def get_input_positions(file_name):
    cube_positions = []

    with open(file_name, 'r') as file:
        for line in file:
            cube_positions.append([int(num) for num in line.split(',')])

    return cube_positions


def count_adjacent_sides(cube_positions):
    counter = 0

    for cube in cube_positions:
        for i in [-1, 1]:
            if [cube[0]+i, cube[1], cube[2]] in cube_positions:
                counter += 1
            if [cube[0], cube[1]+i, cube[2]] in cube_positions:
                counter += 1
            if [cube[0], cube[1], cube[2]+i] in cube_positions:
                counter += 1

    return counter


if __name__ == '__main__':
    cubes = get_input_positions(input_file)
    # cubes = get_input_positions(test_file)

    surface = len(cubes)*6 - count_adjacent_sides(cubes)
    print(surface)
