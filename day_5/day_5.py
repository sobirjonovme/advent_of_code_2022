

# file_name = 'test.txt.txt'
file_name = 'day_5.txt'

with open(file_name, 'r') as file:
    data = file.read()

    stack_part, movement_part = data.split('\n\n')

    # Assigning stacks list
    stack_part = stack_part.split('\n')
    stacks = stack_part.pop().split('   ')

    for i in range(len(stacks)):
        stacks[i] = []

    for i in range(len(stack_part)-1, -1, -1):
        line = stack_part[i]
        index = -1
        for j in range(1, len(line), 4):
            index += 1
            if line[j] not in [' ', '[', ']']:
                stacks[index].append(line[j])

    # print(stacks)

    # Do movements
    movement_part = movement_part.split('\n')
    # print(movement_part)

    # 5, 12, 17
    for line in movement_part:
        line = line.split(' ')

        number = int(line[1])
        from_stack = int(line[3])
        to_stack = int(line[5])
        # print(line[5], line[12], line[17])

        for i in range(number):
            stacks[to_stack-1].append(stacks[from_stack-1].pop())
        
    result = ''
    for i in range(len(stacks)):
        if stacks[i]:
            result += stacks[i][-1]

    print(f"result:   {result}")






    
    