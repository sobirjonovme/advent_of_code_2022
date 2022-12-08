from pprint import pprint

file_name = 'day_7.txt'
# file_name = 'test.txt'


# def find_directories_size(dir_elements):
#     dirs_size = {}
#
#     for dir in dir_elements.keys():
#         dir_size = directory_size(dir, dir_elements, dirs_size)
#
#     return dirs_size

def make_path(dir_stack):
    path = ''
    for dir in dir_stack:
        path += dir + '/'
    return path


def find_directories_elements(file_name):
    with open(file_name) as file:
        current_dir = None
        current_dir_elements = []
        dir_stack = []
        dir_elements = {}

        for line in file:
            line = line.split(' ')

            if line[0] == '$':
                if line[1] == 'cd':
                    if current_dir_elements:
                        dir_elements[current_dir] = current_dir_elements

                        # if current_dir == 'djtchhmw':
                        #     pprint(current_dir_elements)
                        #
                        # if current_dir_elements == ['287664', '307590']:
                        #     print(current_dir)

                    if line[2] == '..\n':
                        dir_stack.pop()
                        current_dir = dir_stack[-1]
                    else:
                        current_dir = line[2].split('\n')[0]
                        dir_stack.append(current_dir)
                        current_dir = make_path(dir_stack)
                    current_dir_elements = []

            elif line[0] == 'dir':
                temp = line[1].split('\n')[0]
                current_dir_elements.append(make_path(dir_stack) + temp + '/')
            else:
                current_dir_elements.append(line[0])
        if current_dir_elements:
            dir_elements[current_dir] = current_dir_elements
        # pprint(dir_elements)
        return dir_elements


def directory_size(dir, dir_elements, dirs_size):
    dir_size = dirs_size.get(dir, 0)
    if dir_size != 0:
        return dir_size

    for element in dir_elements[dir]:
        if element.isdigit():
            dir_size += int(element)
        else:
            dir_size += directory_size(element, dir_elements, dirs_size)

    dirs_size[dir] = dir_size
    return dir_size


def find_total_size_of_target_directories(file_name):
    dir_elements = find_directories_elements(file_name)

    dirs_size = {}
    total = 0

    for dir in dir_elements.keys():
        dir_size = directory_size(dir, dir_elements, dirs_size)
        if dir_size <= 100000:
            total += dir_size

    return total


def find_target_directory_size(file_name):
    dir_elements = find_directories_elements(file_name)

    dirs_size = {}
    target_directory_size = 70000001

    for dir in dir_elements.keys():
        dir_size = directory_size(dir, dir_elements, dirs_size)
        if dir == '//':
            target_size = 30000000 - (70000000-dir_size)

        if (dir_size >= target_size) and (dir_size < target_directory_size):
            target_directory_size = dir_size

    return target_directory_size


if __name__ == '__main__':
    total_size = find_total_size_of_target_directories(file_name)
    target_directory_size = find_target_directory_size(file_name)
    print(total_size)
    print(target_directory_size)
