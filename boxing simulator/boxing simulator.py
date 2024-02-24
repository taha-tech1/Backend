import random

boxing_moves = {1: 'Jab', 2: 'Cross', 3: 'Hook', 4: 'Uppercut'}

beat_rules = [[0]*4 for _ in range(4)]
for i in range(0, 4):
    for j in range(i, 4):
        if j % 2 == 0:
            beat_rules[i][j] = 1
            beat_rules[j][i] = 1
        else:
            beat_rules[i][j] = 0
            beat_rules[j][i] = 0

p1_fighter = int(input('select a number of move: Jab - 1, Cross - 2, Hook - 3, Uppercut - 4 : '))
p2_fighter = random.randint(1, 4)
print(f'You chose {boxing_moves[p1_fighter]}')
print(f'p2 chose {boxing_moves[p2_fighter]}')

if beat_rules[p1_fighter-1][p2_fighter-1] == 1:
    print('Congrats! p1 is the winner')
else:
    print('p2 is the winner')

