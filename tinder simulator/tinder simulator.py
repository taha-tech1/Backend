
first_user = ['alsqwd', 'male', 19, 'sww', 'aaa', 'bbb', 20 , 30] # age restriction in first_user[6] - first_user[7] and same for others
second_user = ['wwwq', 'female', 29, 'awq', 'ccc', 'qqq', 23, 26]
third_user = ['qqq', 'female', 35, 'zxc', 'vvv', 'mmm', 35, 45]
forth_user = ['ooo', 'male', 24, 'a', 'c', 'e', 20, 23]
built_in_users = [first_user, second_user, third_user, forth_user]
found = False

while found == False:

    user = []
    user.append(input('Enter your name: '))
    user.append(input('Enter your gender? male / female '))
    user.append(int(input('Enter your age ')))
    user.append(input('Enter your profession '))
    user.append(input('Whats your favorite tv show '))
    user.append(input('Whats your favorite food ? '))

    for i in built_in_users:
        if i[7] > user[2] > i[6]:
            print(f'Match founded! Congrats')
            found = True
    if found == False:
        print('Enter the data again!')
