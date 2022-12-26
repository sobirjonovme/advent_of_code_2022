from pprint import pprint

input_file = 'day_21.txt'
test_file = 'test.txt'


def get_monkeys_yells(file_name):
    monkeys_yells = {}
    with open(file_name, 'r') as file:
        for line in file:
            line = line.split(':')
            line[1] = line[1].split('\n')[0][1:]
            if line[0] == 'humn':
                monkeys_yells[line[0]] = None
            elif line[0] == 'root':
                monkeys_yells['root'] = line[1].split(' ')
                monkeys_yells['root'][1] = '-'
            elif line[1].isdigit():
                monkeys_yells[line[0]] = int(line[1])
            else:
                monkeys_yells[line[0]] = line[1].split(' ')
    return monkeys_yells


def get_monkey_number(monkeys_yells, monkey_name):

    if monkeys_yells[monkey_name] is None:
        return None

    if type(monkeys_yells[monkey_name]) in [int, float]:
        return monkeys_yells[monkey_name]

    task = monkeys_yells[monkey_name]
    num1 = get_monkey_number(monkeys_yells, task[0])
    num2 = get_monkey_number(monkeys_yells, task[2])

    if num1 is None or num2 is None:
        return None

    if task[1] == '+':
        result = num1 + num2
    elif task[1] == '-':
        result = num1 - num2
    elif task[1] == '*':
        result = num1 * num2
    elif task[1] == '/':
        result = num1 / num2

    monkeys_yells[monkey_name] = result
    return result


def find_humn_number(monkeys_yells, monkey_name, result):

    if monkey_name == 'humn':
        return result

    task = monkeys_yells[monkey_name]
    num1 = get_monkey_number(monkeys_yells, task[0])
    num2 = get_monkey_number(monkeys_yells, task[2])

    if num1 is None:
        if task[1] == '+':
            # X + num2 = result
            # X = result - num2
            return find_humn_number(monkeys_yells, task[0], result-num2)
        elif task[1] == '-':
            # X - num2 = result
            # X = result + num2
            return find_humn_number(monkeys_yells, task[0], result+num2)
        elif task[1] == '*':
            # X * num2 = result
            # X = result / num2
            return find_humn_number(monkeys_yells, task[0], result/num2)
        elif task[1] == '/':
            # X / num2 = result
            # X = result * num2
            return find_humn_number(monkeys_yells, task[0], result*num2)
    elif num2 is None:
        if task[1] == '+':
            # num1 + X = result
            # X = result - num1
            return find_humn_number(monkeys_yells, task[2], result-num1)
        elif task[1] == '-':
            # num1 - X = result
            # X = num1 - result
            return find_humn_number(monkeys_yells, task[2], num1-result)
        elif task[1] == '*':
            # num1 * X = result
            # X = result/num1
            return find_humn_number(monkeys_yells, task[2], result/num1)
        elif task[1] == '/':
            # num1 / X = result
            # X = num1/result
            return find_humn_number(monkeys_yells, task[2], num1/result)


if __name__ == '__main__':
    # monkeys_yells = get_monkeys_yells(test_file)
    monkeys_yells = get_monkeys_yells(input_file)

    print(find_humn_number(monkeys_yells, 'root', 0))
