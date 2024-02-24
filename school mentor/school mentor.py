from math import sqrt


def english_task(abcd, task):
    match task:
        case 'lowercase':
            print(abcd.keys())
        case 'uppercase':
            print(str(abcd.keys()).upper())
        case 'letter':
            letter = input('Enter an egnlsih letter: ')
            print(abcd[letter])
        case _:
            print('Invalid Input!')

def math_task(task):
    match task:
        case 'multi':
            num = int(input('Enter the range of the multipication table: '))
            rows, cols = (num, num)
            arr = [[0]*cols]*rows
            for i in range(0, num):
                for j in range(0, num):
                    arr[i][j] = (i+1)*(j+1)
                print(arr[i])
        case 'square':
            num = int(input('Enter a number: '))
            print(num**2)
        case 'primeCheck':
            num = int(input('Enter a number to check if its a prime number: '))
            prime_check = True # the result (if its prime number or not)'
            if num == 2:
                print('Its a prime number!')
            elif num <= 1:
                print('Its not prime number!')
            else:
                for i in range(2, int(sqrt(num))+1):
                    if num % i == 0:
                        prime_check = False
                        break
                print('Its a prime number!') if prime_check else print('Its not prime number!')
        case _:
            print('Invalid Input!')





def run_task(subject):
    match subject:
        case 'math':
            task = input('Enter a specific task in math : multi / square / primeCheck ')
            math_task(task)
        case 'english':
            abcd_english = {'a': 'Apple', 'b': 'Balance', 'c': 'Cat', 'd': 'Door', 'e': 'East', 'f': 'Festival',
                           'g': 'Game', 'h': 'Home', 'i': 'Input', 'j': 'Jacket', 'k': 'Key', 'l': 'Like',
                           'm': 'Machine', 'n': 'Nose', 'o': 'Owl', 'p': 'Pet', 'q': 'Quiz', 'r': 'Rabbit', 's': 'Sun',
                           't': 'Type', 'u': 'Umbrella', 'v': 'Vibe', 'w': 'Window', 'x': 'Xbox', 'y': 'Year',
                           'z': 'Zoom'}
            task = input('Enter a specific task in english : for abc in uppercase write : uppercase / for abc in '
                         'lowercase write : lowercase / to generate a word starting with specific letter write: letter ')
            english_task(abcd_english, task)
        case _:
            print("Invalid input!")



command = input('Whats the subject that you want help with? math / english ')
run_task(command)
