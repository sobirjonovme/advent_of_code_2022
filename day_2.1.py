
file_name = 'day_2.txt'

#                 Rock   Paper   Scissors
# for opponent     A       B        C    
# for me           X       Y        Z
opp_dict = {'A': 1, 'B': 2, 'C': 3}
my_dict = {'X': 1, 'Y': 2, 'Z': 3}

def get_round_result(opponent, me):
    
    if opponent == 'C' and me == 'X':
        return 6
    if opponent == 'A' and me == 'Z':
        return 0
    
    if opp_dict[opponent] > my_dict[me]:
        return 0
    if opp_dict[opponent] == my_dict[me]:
        return 3
    if opp_dict[opponent] < my_dict[me]:
        return 6

total_score = 0

with open(file_name, 'r') as file:
    for line in file:
        opponent, me = line.split(' ') # shapes chosen by me and my opponent
        me = me.split('\n')[0] # for the reason that line ends with '\n' in files

        total_score += get_round_result(opponent, me) + my_dict[me]


print(f"Total Score:   {total_score}")
