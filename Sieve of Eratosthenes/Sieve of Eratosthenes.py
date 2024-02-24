

main_number_list = []
for i in range(4, 151):
    main_number_list.append(i)

prime_number_list = [2, 3]

prime_check = True

counter = 2

for j in range(4, 151):
    number = j
    for prime_divider in prime_number_list:
        if (number % prime_divider) == 0:
            print(number)
            prime_check = False
            break

    if prime_check == True:
        print(number)
        counter += 1
        prime_number_list.append(number)
        main_number_list.remove(number)
        for i in range(2, round(150/number)+1):
            if number*i in main_number_list:
                main_number_list.remove(number*i)

    prime_check = True

print(f'I found {counter} prime numbers: ')
print(prime_number_list)




