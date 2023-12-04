from io import open
import re
import numpy as np


def load_data(path):
    data = []
    with open(path) as file:
        for line in file.readlines():
            card_to_numbers = line.split(':')
            numbers = card_to_numbers[1].split('|')
            winning_numbers = to_number_array(remove_spaces(numbers[0]).split(' '))
            bets = to_number_array(remove_spaces(numbers[1]).split(' '))
            data.append({'winning': winning_numbers, 'bets': bets})
    return data


def remove_spaces(numbers_line):
    line = re.sub('\s+', ' ', numbers_line)
    return line.strip()


def to_number_array(str_array):
    new_array = []
    for item in str_array:
        new_array.append(int(item))
    return new_array


def part1():
    path = '../res/part1/real_data.txt'
    data = load_data(path)
    total_points = 0
    for game in data:
        winning = game['winning']
        bets = game['bets']
        points = 0
        arr = np.array(winning)
        for bet in bets:
            if bet in arr:
                if not points == 0:
                    points = points * 2
                else:
                    points += 1
        total_points += points
    print(total_points)


def part2():
    path = '../res/part2/real_data.txt'
    data = load_data(path)
    copies = []
    for i in range(0, len(data)):
        copies.append(1)
    for idx, game in enumerate(data):
        winning = game['winning']
        bets = game['bets']
        arr = np.array(winning)
        multiplier = copies[idx]
        wins = 0
        for bet in bets:
            if bet in arr:
                wins += 1
                copies[idx + wins] += multiplier

    print(sum(copies))


# main
print('########## PART 1 ##########')
part1()

print('########## PART 2 ##########')
part2()
