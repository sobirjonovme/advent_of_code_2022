
# file_name = 'test.txt'
file_name = 'day_6.txt'


def is_repeated(datastream, end, start) -> bool:
    if end == start:
        return False

    for i in range(end-1, start-1, -1):
        if datastream[end] == datastream[i]:
            return True
    return is_repeated(datastream, end-1, start)


def find_number_of_marker(file_name, length):
    with open(file_name, 'r') as file:
        datastream = file.read()

        for i in range(3, len(datastream)):
            if is_repeated(datastream, i, i-length+1) is False:
                return i+1


if __name__ == '__main__':
    # Part I
    start_packet = find_number_of_marker(file_name, 4)
    print(f"Start packet:   {start_packet}")

    # Part II
    start_message = find_number_of_marker(file_name, 14)
    print(f"Start message:   {start_message}")
