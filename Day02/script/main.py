from io import open

# props
allowed_amounts = {
    'blue': 14,
    'green': 13,
    'red': 12
}


def reset_min_color_cubes():
    min_color_cubes = {
        'blue': 0,
        'red': 0,
        'green': 0
    }
    return min_color_cubes


def part1():
    file_path = '../res/part1/real_data.txt'
    file = open(file_path)

    summary = 0
    for line in file.readlines():
        # get game number
        line_split = line.split(':')
        game_number = int(line_split[0][4:])
        cubes = line_split[1]
        break_flag = False
        for cube_draw in cubes.split(';'):
            separate_color_cubes = cube_draw.split(',')
            if break_flag:
                break
            for single_color_cube in separate_color_cubes:
                cubes_color_split = single_color_cube.strip().split(' ')
                amount = int(cubes_color_split[0])
                color = cubes_color_split[1]
                max_amount_for_color = int(allowed_amounts[color])
                if max_amount_for_color < amount:
                    break_flag = True
                    break
        if not break_flag:
            summary += game_number

    print('No. of possible games: ' + str(summary))


def part2():
    file_path = '../res/part2/real_data.txt'
    file = open(file_path)

    summary = 0

    min_color_cubes = reset_min_color_cubes()
    summary = 0
    for line in file.readlines():
        # get game number
        line_split = line.split(':')
        cubes = line_split[1]
        for cube_draw in cubes.split(';'):
            separate_color_cubes = cube_draw.split(',')
            for single_color_cube in separate_color_cubes:
                cubes_color_split = single_color_cube.strip().split(' ')
                amount = int(cubes_color_split[0])
                color = cubes_color_split[1]

                if min_color_cubes[color] < amount:
                    min_color_cubes[color] = amount
        power_for_game = 1
        for color, amount in min_color_cubes.items():
            if amount > 0:
                power_for_game *= amount
        summary += power_for_game
        min_color_cubes = reset_min_color_cubes()
    print("Total sum: " + str(summary))


# main
print('########## PART 1 ##########')
part1()
print('########## PART 2 ##########')
part2()
