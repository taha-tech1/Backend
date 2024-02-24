import math
plants = []
herbs = ['Sun', 'High', 'Yes']
shrubs = ['Sun', 'Mid', 'Yes']
creepers = ['Rain', 'Low', 'No']

plants.append(herbs)
plants.append(shrubs)
plants.append(creepers)
plants_name = ['herbs', 'shrubs', 'creepers']
weather = []
weather.append(input("its Sunny day or Rainy day? Sun / Clouds "))
rain_percent = int(input("What is the percent of the rain in this Day? "))
if 0 <= rain_percent <= 33:
    weather.append('Low')
elif 33 < rain_percent <= 66:
    weather.append('Mid')
elif 66 < rain_percent <= 100:
    weather.append('High')
weather.append(input("In this day There is wind? Yes / No "))

print('\nIn this weather each plant like: \n')
for j in range(0, 3):
    for i in range(0, 3):
            if plants[j][i] == weather[i]:
                if i == 0:
                    print(plants_name[j], 'Likes the ', weather[i], 'days')
                elif i == 1:
                    print(f'{plants_name[j]} likes the {weather[i]} rainy days')
                else:
                    match weather[i]:
                        case 'Yes':
                            if plants[j][i] == weather[i]:
                                print(f'{plants_name[j]} likes the wind')
                        case 'No':
                            if plants[j][i] == weather[i]:
                                print(f'{plants_name[j]} likes that there is no wind')

