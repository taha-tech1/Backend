def convertion(convertion_range, type1, convert_type, source_value):
    if type1 == convert_type:
        return source_value
    match convertion_range:
        case 'temp':
            match type1:
                case 'F':
                    return (source_value - 32) * (5/9)
                case 'C':
                    return source_value
                case _:
                    print('Invalid input!')
        case 'speed':
            match type1:
                case 'MPH':
                    return 1.6093440006147 * source_value
                case 'KPH':
                    return source_value / 1.6093440006147
                case _:
                    print('Invalid input!')

        case 'weight':
            match type1:
                case 'kg':
                    match convert_type:
                        case 'stone':
                            return source_value/6.35
                        case 'lbs':
                            return source_value*2.205
                        case _:
                            print('Invalid input!')
                case 'lbs':
                    match convert_type:
                        case 'stone':
                            return source_value/14
                        case 'kg':
                            return source_value/2.205
                        case _:
                            print('Invalid input!')
                case 'stone':
                    match convert_type:
                        case 'lbs':
                            return source_value*14
                        case 'kg':
                            return source_value*6.35
                        case _:
                            print('Invalid input!')
                case _:
                    print('Invalid input!')
        case _:
            print('Invalid input!')

print('Hello this is the coverter! you can convert many types of data from one type to another. ')
print('the supported conversions are:temp (F <-> C),speed (MPH <-> KPH),weight (kg <-> stone <-> lbs).')

source_value = int(input('What is your source value '))
convertion_title = input('Write your convertion type(choose one): temp \ speed \ weight ')

match convertion_title:
    case 'temp':
        convertion_type = input('What is the type of the item that you want to convert: F / C ')
        to_type = input('What type you want to convert to: F / C ')
    case 'speed':
        convertion_type = input('What is the type of the item that you want to convert: MPH / KPH ')
        to_type = input('What type you want to convert to: MPH / KPH ')
    case 'weight':
        convertion_type = input('What is the type of the item that you want to convert: kg / stone / lbs ')
        to_type = input('What type you want to convert to: kg / stone / lbs ')

if convertion_type == to_type:
    print(f'The same type no convertion needed! the result it {source_value}')
    result = source_value
else:
    result = convertion(convertion_title, convertion_type, to_type, source_value)
    print(f'the result is {result}')
