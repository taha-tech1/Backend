import random as rn
import math


def asc_sort(players):
    sorted_list = []
    for i in range(0, 4):
        min = players[i]
        for j in range(i, 4):
            if  min['Total Points'] > players[j]['Total Points']:
                min = players[j]
                counter = j
        swap = players[i]
        players[i] = min
        players[counter] = swap



def winning(player1, player2, p1_chance, p2_chance):
    rand = rn.uniform(0, 1)
    draw = 0.2
    if rand <= draw:
        player1['Total Points'] += 0.5
        player2['Total Points'] += 0.5
      #  elo_rating_update(player1, player2)
        return None
    if p1_chance > p2_chance:
        if draw < rand <= p1_chance:
            player1['Total Points'] += 1
       #     elo_rating_update(player1, player2)
            return player1
        else:
            player2['Total Points'] += 1
        #    elo_rating_update(player2, player1)
            return player2
    else:
        if draw < rand <= p2_chance:
            player2['Total Points'] += 1
        #    elo_rating_update(player2, player1)
            return player2

        else:
            player1['Total Points'] += 1
        #    elo_rating_update(player1, player2)
            return player1



def game_start(players):

    for i in range(0, 2):
        if i == 0:
            p1_chance, p2_chance = chance_of_winning(players[0], players[3])
            winner = winning(players[0], players[3], p1_chance, p2_chance)
            p1_chance, p2_chance = chance_of_winning(players[1], players[2])
            winner = winning(players[1], players[2], p1_chance, p2_chance)
        else:
            p1_chance, p2_chance = chance_of_winning(players[0], players[1])
            winner = winning(players[0], players[1], p1_chance, p2_chance)
            p1_chance, p2_chance = chance_of_winning(players[2], players[3])
            winner = winning(players[2], players[3], p1_chance, p2_chance)


def chance_of_winning(player1, player2):
    if player1['Rank'] <= player2['Rank']:
        ratio = 1 - (player1['Rank'] / player2['Rank'])
        player1_chance = 0.4 + ratio
        player2_chance = 0.4 - ratio

    elif player2['Rank'] < player1['Rank']:
        ratio = 1 - (player2['Rank'] / player1['Rank'])
        player1_chance = 0.4 - ratio
        player2_chance = 0.4 + ratio

    return player1_chance, player2_chance

def elo_rating_update(winner, loser):

    winner['Rank'] += 1/(1+(10**((winner['Rank']-loser['Rank'])/400)))
    loser['Rank'] -= 1/(1+(10**(loser['Rank']-winner['Rank']/400)))
    return


player1 = {'Rank': rn.randint(1500, 2000), 'name': 'Taha', 'Total Points': 0}
player2 = {'Rank': rn.randint(1500, 2000), 'name': 'aa', 'Total Points': 0}
player3 = {'Rank': rn.randint(1500, 2000), 'name': 'vv', 'Total Points': 0}
player4 = {'Rank': rn.randint(1500, 2000), 'name': 'ww', 'Total Points': 0}

players = [player1, player2, player3, player4]

rank_in_start = [player['Rank'] for player in players]
print(rank_in_start)
game_start(players)
max = player1

for player in players:
    if player['Total Points'] > max['Total Points']:
        max = player

print(f'The Winner is : {max}')

asc_sort(players)

print(players)





