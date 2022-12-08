from pprint import pprint

file_name = 'day_8.txt'
# file_name = 'test.txt'


def make_trees_matrix(file_name):
    with open(file_name, 'r') as file:
        data = file.read()

    trees_matrix = data.split('\n')

    for i in range(len(trees_matrix)):
        temp = []
        for j in trees_matrix[i]:
            temp.append(int(j))

        trees_matrix[i] = temp

    return trees_matrix


def is_visible(trees_matrix, row, column):
    row_number = len(trees_matrix)
    column_number = len(trees_matrix[0])

    left = True
    for i in range(column):
        if trees_matrix[row][i] >= trees_matrix[row][column]:
            left = False

    right = True
    for i in range(column+1, column_number):
        if trees_matrix[row][i] >= trees_matrix[row][column]:
            right = False

    top = True
    for i in range(row):
        if trees_matrix[i][column] >= trees_matrix[row][column]:
            top = False

    down = True
    for i in range(row+1, row_number):
        if trees_matrix[i][column] >= trees_matrix[row][column]:
            down = False

    if left or right or top or down:
        return True

    return False


def calculate_tree_score(trees_matrix, row, column):
    row_number = len(trees_matrix)
    column_number = len(trees_matrix[0])
    score = 1

    counter = 0
    for i in range(column-1, -1, -1):
        counter += 1
        if trees_matrix[row][i] >= trees_matrix[row][column]:
            break
    score *= counter

    counter = 0
    for i in range(column+1, column_number):
        counter += 1
        if trees_matrix[row][i] >= trees_matrix[row][column]:
            break
    score *= counter

    counter = 0
    for i in range(row-1, -1, -1):
        counter += 1
        if trees_matrix[i][column] >= trees_matrix[row][column]:
            break
    score *= counter

    counter = 0
    for i in range(row+1, row_number):
        counter += 1
        if trees_matrix[i][column] >= trees_matrix[row][column]:
            break
    score *= counter

    return score


def count_visible_trees(file_name):

    trees_matrix = make_trees_matrix(file_name)
    row_number = len(trees_matrix)
    column_number = len(trees_matrix[0])
    counter = 2 * (row_number+column_number) - 4

    for i in range(1, row_number-1):
        for j in range(1, column_number-1):
            if is_visible(trees_matrix, i, j):
                counter += 1

    return counter


def find_highest_score(file_name):
    trees_matrix = make_trees_matrix(file_name)
    row_number = len(trees_matrix)
    column_number = len(trees_matrix[0])

    result = 0

    for i in range(1, row_number - 1):
        for j in range(1, column_number - 1):
            score = calculate_tree_score(trees_matrix, i, j)
            if score > result:
                result = score

    return result


if __name__ == '__main__':
    number = count_visible_trees(file_name)
    score = find_highest_score(file_name)

    print(f"Number:   {number}")
    print(f"Score:   {score}")

