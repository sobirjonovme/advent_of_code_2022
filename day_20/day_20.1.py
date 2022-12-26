
input_file = 'day_20.txt'
test_file = 'test.txt'


def print_final_array(input_array, final_range):
    # print final array
    for i in final_range:
        print(input_array[i], end=' ')


def get_input_array(file_name):
    input_array = []
    with open(file_name, 'r') as file:
        for line in file:
            input_array.append(int(line))
    return input_array


def find_coordinates_sum(file_name):
    input_array = get_input_array(file_name)
    length = len(input_array)
    # initial_range = list(range(length))
    final_range = list(range(length))

    for i in range(length):
        # to find current number's new position in ranged array
        for j in range(length):
            if i == final_range[j]:
                final_index = j
                break
        current_number = input_array[i]
        movement_number = current_number % (length-1)

        for j in range(movement_number):
            if final_index == length-1:
                temp = final_range.pop()
                final_range.insert(1, temp)
                final_index = 1
            else:
                final_range[final_index], final_range[final_index+1] = \
                    final_range[final_index+1], final_range[final_index]
                final_index += 1

    for i in range(length):
        if input_array[final_range[i]] == 0:
            zero_index = i
            break

    x = (zero_index+1000) % length
    y = (zero_index+2000) % length
    z = (zero_index+3000) % length

    print("three numbers indices:  ", x, y, z)
    print("three numbers:", input_array[final_range[x]], input_array[final_range[y]], input_array[final_range[z]])

    coordinates_sum = input_array[final_range[x]] + input_array[final_range[y]] + input_array[final_range[z]]
    return coordinates_sum


if __name__ == '__main__':
    # coordinates_sum = find_coordinates_sum(test_file)
    coordinates_sum = find_coordinates_sum(input_file)
    print("sum:  ", coordinates_sum)
