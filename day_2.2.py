
file_name = 'day_2.txt'
# file_name = 'test.txt'


# for opponent 
#        Rock    Paper    Scissors
#         A       B         C    
# 
# for me
#        Lose     Draw     Win
#         X        Y        Z


opp_dict = {'A': 1, 'B': 2, 'C': 3}
my_dict = {'X': 0, 'Y': 3, 'Z': 6}

def get_shape_result(opponent, me):

    if me == 'X':
        if opponent == 'A':
            return 3 # for scissor
        return opp_dict[opponent] - 1
    if me == 'Y':
        return opp_dict[opponent]
    if me == 'Z':
        if opponent == 'C':
            return 1 # for rock
        return opp_dict[opponent] + 1

    

total_score = 0

with open(file_name, 'r') as file:
    for line in file:
        opponent, me = line.split(' ') # shapes chosen by me and my opponent
        me = me.split('\n')[0] # for the reason that line ends with '\n' in files

        total_score += get_shape_result(opponent, me) + my_dict[me]


print(f"Total Score:   {total_score}")
