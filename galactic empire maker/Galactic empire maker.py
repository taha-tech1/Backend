
import random as rn
materials = ['asdd', 'qwdsa', 'www', 'qzx', 'ggg', 'jhj', 'qwe', 'uuu', 'iyu', 'oup', 'ptr',
             'hgh', 'bbv', 'faa', 'laa', 'lxs', 'kla', 'xcv', 'mmm', 'wrt']

alien1 = ['all', rn.choice(materials), rn.choice(materials), rn.choice(materials), 4, False]
alien2 = ['zzz', rn.choice(materials), rn.choice(materials), rn.choice(materials), 5, False]
alien3 = ['ccc', rn.choice(materials), rn.choice(materials), rn.choice(materials), 8, False]
alien4 = ['rrr', rn.choice(materials), rn.choice(materials), rn.choice(materials), 2, False]

counter = 0
aliens = [alien1, alien2, alien3, alien4]

for alien in aliens:
    for i in range(alien[4]):
        suggest = rn.choice(materials)
        for i in range(1, 4):
            if alien[i] == suggest:
                alien[5] = True
                counter += 1
                alien.append(suggest)
                break
        if alien[5] == True:
            break

if counter / 4 >= 0.7:
    print('You succeeded in convincing them')
else:
    print('You failed in convince ')
for alien in aliens:
    print(f'alien name : {alien[0]}')
    if alien[5] == True:
        print(f'convinced successfully, accepting the material {alien[6]}')
    else:
        print('you failed to convince this alien')

print(f'The success percent is : {counter/4}')







