### general points: 
### 1. DRY DRY DRY
### 2. good breakdown to small functions. good naming
###


import random

def attack(attacker, defender, type_modify):
    damage = type_modify*(random.randint(1, 20)* attacker['strength'])
    defender['life'] -= damage
    if defender['life'] < 0:
        defender['life'] = 0
    print(attacker['name'], 'attacks', defender['name'], f'. deals {damage} damage', defender['name'], 'now has', defender['life'], 'amount of life remaining\n')
    if defender['life'] < 0:
        print(defender['name'], 'have been died')
    return

def modifyType(attacker, defender):
    match attacker['type']:
        case 'fire':
            match defender['type']:
                case 'fire':
                    modify_type = 2
                    return modify_type
                case 'water':
                    modify_type = 2
                    return modify_type
                case 'earth':
                    modify_type = 1
                    return modify_type
                case 'wind':
                    modify_type = 2
                    return modify_type
                case _:
                    print('invalid input!')
        case 'water':
            match defender['type']:
                case 'fire':
                    modify_type = 2
                    return modify_type
                case 'water':
                    modify_type = 2
                    return modify_type
                case 'earth':
                    modify_type = 1
                    return modify_type
                case 'wind':
                    modify_type = 2
                    return modify_type
                case _:
                    print('invalid input!')
        case 'earth':
            match defender['type']:
                case 'fire':
                    modify_type = 2
                    return modify_type
                case 'water':
                    modify_type = 2
                    return modify_type
                case 'earth':
                    modify_type = 1
                    return modify_type
                case 'wind':
                    modify_type = 2
                    return modify_type
                case _:
                    print('invalid input!')
        case 'wind':
            match defender['type']:
                case 'fire':
                    modify_type = 2
                    return modify_type
                case 'water':
                    modify_type = 2
                    return modify_type
                case 'earth':
                    modify_type = 1
                    return modify_type
                case 'wind':
                    modify_type = 2
                    return modify_type
                case _:
                    print('invalid input!')
        case _:
            print('invalid input!')

### do it dynamicly - DRY
p1_first_pok = {'name': 'Rayquaza', 'level': 3, 'strength': 6, 'speed': 1, 'type': 'fire', 'life': 120}
p1_sec_pok = {'name': 'Mewtwo', 'level': 5, 'strength': 7, 'speed': 2, 'type': 'water', 'life': 120}
p1_third_pok = {'name': 'Lugia', 'level': 2, 'strength': 5, 'speed': 1, 'type': 'earth', 'life': 120}
p1_fourth_pok = {'name': 'Kyurem', 'level': 7, 'strength': 3, 'speed': 5, 'type': 'earth', 'life': 120}
p1_fifth_pok = {'name': 'Xerneas', 'level': 8, 'strength': 8, 'speed': 3, 'type': 'wind', 'life': 120}
player1 = [p1_first_pok, p1_sec_pok, p1_third_pok, p1_fourth_pok, p1_fifth_pok]
p1_pok_num = 5
### do it dynamicly - DRY
p2_first_pok = {'name': 'Eternatus', 'level': 10, 'strength': 9, 'speed': 3, 'type': 'fire', 'life': 120}
p2_sec_pok = {'name': 'Kyogre', 'level': 2, 'strength': 2, 'speed': 1, 'type': 'fire', 'life': 120}
p2_third_pok = {'name': 'Zacian', 'level': 6, 'strength': 5, 'speed': 2, 'type': 'wind', 'life': 120}
p2_fourth_pok = {'name': 'Suicune', 'level': 1, 'strength': 2, 'speed': 2, 'type': 'water', 'life': 120}
p2_fifth_pok = {'name': 'Lucario', 'level': 7, 'strength': 8, 'speed': 5, 'type': 'earth', 'life': 120}
player2 = [p2_first_pok, p2_sec_pok, p2_third_pok, p2_fourth_pok, p2_fifth_pok]
p2_pok_num = 5
### dry
p1_pokemon_choice = random.randint(0, p1_pok_num-1) #init
p2_pokemon_choice = random.randint(0, p2_pok_num-1) #init
### dry
p1_pokemon = player1[p1_pokemon_choice]
print(p1_pokemon['name'], 'has joined the fight\n')
### dry
p2_pokemon = player2[p2_pokemon_choice]
print(p2_pokemon['name'], 'has joined the fight\n')

for poke in player1:
    poke['speed'] += random.randint(1, 20)
for poke in player2:
    poke['speed'] += random.randint(1, 20)

attacker_turn = 0

p1_pok_loss = []
p2_pok_loss = []

while p1_pok_num > 0 and p2_pok_num > 0:

    if (player1[p1_pokemon_choice])['life'] <= 0:
        del player1[p1_pokemon_choice]
        p1_pokemon_choice = random.randint(0, p1_pok_num-1)
        p1_pokemon = player1[p1_pokemon_choice]
        print(p1_pokemon['name'], 'has joined the fight\n')

    if (player2[p2_pokemon_choice])['life'] <= 0:
        del player2[p2_pokemon_choice]
        p2_pokemon_choice = random.randint(0, p2_pok_num-1)
        p2_pokemon = player2[p2_pokemon_choice]
        print(p2_pokemon['name'], 'has joined the fight\n')

    type_modifier = modifyType(p1_pokemon, p2_pokemon)

    if attacker_turn == 0:
        if p1_pokemon['speed'] > p2_pokemon['speed']:
            attacker_turn = 1
            attacker = p1_pokemon
            defender = p2_pokemon

        else:
            attacker_turn = 2
            attacker = p2_pokemon
            defender = p1_pokemon

    while p1_pokemon['life'] > 0 and p2_pokemon['life'] > 0:
        attack(attacker, defender, type_modifier)
        if attacker_turn == 1:
            attacker_turn = 2
            attacker = p2_pokemon
            defender = p1_pokemon
        else:
            attacker_turn = 1
            attacker = p1_pokemon
            defender = p2_pokemon

    if p1_pokemon['life'] > 0:
        p2_pok_loss.append(p2_pokemon)
        p2_pok_num -= 1

    else:
        p1_pok_loss.append(p1_pokemon)
        p1_pok_num -= 1

    attacker_turn = 0 #Reset


