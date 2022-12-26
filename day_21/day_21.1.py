

input_file = 'day_21.txt'
test_file = 'test.txt'


def get_monkeys_yells(file_name):
    monkeys_yells = {}
    with open(file_name, 'r') as file:
        for line in file:
            line = line.split(':')
            line[1] = line[1].split('\n')[0][1:]
            # print(line)
            if line[1].isdigit():
                monkeys_yells[line[0]] = int(line[1])
            else:
                monkeys_yells[line[0]] = line[1].split(' ')
    return monkeys_yells


def get_monkey_number(monkeys_yells, monkey_name):
    if type(monkeys_yells[monkey_name]) is int:
        return monkeys_yells[monkey_name]

    task = monkeys_yells[monkey_name]

    if task[1] == '+':
        result = get_monkey_number(monkeys_yells, task[0]) + get_monkey_number(monkeys_yells, task[2])

    elif task[1] == '-':
        result = get_monkey_number(monkeys_yells, task[0]) - get_monkey_number(monkeys_yells, task[2])

    elif task[1] == '*':
        result = get_monkey_number(monkeys_yells, task[0]) * get_monkey_number(monkeys_yells, task[2])

    elif task[1] == '/':
        result = get_monkey_number(monkeys_yells, task[0]) / get_monkey_number(monkeys_yells, task[2])

    monkeys_yells[monkey_name] = result
    return result


if __name__ == '__main__':
    # monkeys_yells = get_monkeys_yells(test_file)
    monkeys_yells = get_monkeys_yells(input_file)
    print(get_monkey_number(monkeys_yells, 'root'))
