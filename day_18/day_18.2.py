from pprint import pprint

input_file = 'day_18.txt'
test_file = 'test.txt'


def get_input_positions(file_name):
    cube_positions = []

    with open(file_name, 'r') as file:
        for line in file:
            cube_positions.append([int(num) for num in line.split(',')])

    return cube_positions


def get_borders_matrix(cubes):
    # z -> top, bottom
    # y -> front, tail
    # x -> left, right

    left, right = cubes[0][0], cubes[0][0]  # x
    front, tail = cubes[0][1], cubes[0][1]  # y
    bottom, top = cubes[0][2], cubes[0][2]  # z

    for cube in cubes:
        if cube[0] < left:
            left = cube[0]
        if cube[0] > right:
            right = cube[0]

        if cube[1] < front:
            front = cube[1]
        if cube[1] > tail:
            tail = cube[1]

        if cube[2] < bottom:
            bottom = cube[2]
        if cube[2] > top:
            top = cube[2]

    return [[left, right], [front, tail], [bottom, top]]


def find_cube_surface(cube, cubes_positions, borders):
    surface = 0

    # check left border
    is_count = True
    for i in range(cube[0]-1, borders[0][0]-1, -1):
        if [i, cube[1], cube[2]] in cubes_positions:
            is_count = False
            break
    if is_count:
        print("left")
        surface += 1
    # check right border
    is_count = True
    for i in range(cube[0]+1, borders[0][1]+1):
        if [i, cube[1], cube[2]] in cubes_positions:
            is_count = False
            break
    if is_count:
        print("right")
        surface += 1

    # check front border
    is_count = True
    for i in range(cube[1]-1, borders[1][0]-1, -1):
        if [cube[0], i, cube[2]] in cubes_positions:
            is_count = False
            break
    if is_count:
        print("front")
        surface += 1
    # check tail border
    is_count = True
    for i in range(cube[1]+1, borders[1][1]+1):
        if [cube[0], i, cube[2]] in cubes_positions:
            is_count = False
            break
    if is_count:
        print("tail")
        surface += 1

    # check bottom border
    is_count = True
    for i in range(cube[2]-1, borders[2][0]-1, -1):
        if [cube[0], cube[1], i] in cubes_positions:
            is_count = False
            break
    if is_count:
        print("bottom")
        surface += 1

    # check top border
    is_count = True
    for i in range(cube[2]+1, borders[2][1]+1):
        if [cube[0], cube[1], i] in cubes_positions:
            is_count = False
            break
    if is_count:
        print("top")
        surface += 1

    return surface


def find_whole_surface(file_name):
    cubes = get_input_positions(file_name)
    borders = get_borders_matrix(cubes)

    print(borders)

    surface = 0

    # for cube in cubes:
    #     surface += find_cube_surface(cube, cubes, borders)

    cube = [2, 1, 5]
    print(find_cube_surface(cube, cubes, borders))
    # cube = [2, 1, 5]
    counter = 0
    cube_positions = cubes
    for i in [-1, 1]:
        if [cube[0] + i, cube[1], cube[2]] in cube_positions:
            counter += 1
        if [cube[0], cube[1] + i, cube[2]] in cube_positions:
            counter += 1
        if [cube[0], cube[1], cube[2] + i] in cube_positions:
            counter += 1
    print(counter)
    return surface


if __name__ == '__main__':
    # surface = find_whole_surface(input_file)
    surface = find_whole_surface(test_file)

    print(surface)
