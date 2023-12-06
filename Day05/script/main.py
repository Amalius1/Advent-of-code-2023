from io import open
import numpy as np
import re


def remove_spaces(numbers_line):
    line = re.sub('\s+', ' ', numbers_line)
    return line.strip()


def to_number_array(str_array):
    new_array = []
    for item in str_array:
        new_array.append(int(item))
    return new_array


def read_file(file_path):
    with open(file_path) as file:
        return file.readlines()


def read_seeds(seeds_path):
    with open(seeds_path) as file:
        return to_number_array(remove_spaces(file.readlines()[0]).split(' '))


def read_seeds_part_2(seeds_path):
    seeds = read_seeds(seeds_path)
    new_seeds = []

    return new_seeds


def read_next_map(file_path):
    _map = []
    with open(file_path) as file:
        for line in file.readlines():
            number_line = remove_spaces(line)
            number_array = to_number_array(number_line.split(' '))
            _map.append({'destination': number_array[0], 'source': number_array[1], 'range': number_array[2]})
    return _map


def find_next(number, _map):
    for entry in _map:
        source = entry['source']
        destination = entry['destination']
        in_range = entry['range']
        top_source = source + in_range
        if source <= number <= top_source:
            return number + destination - source
    return number


def find_location_for_seed(seed):
    soil = find_next(seed, seed_to_soil_map)
    fertilizer = find_next(soil, soil_to_fertilizer_map)
    water = find_next(fertilizer, fertilizer_to_water_map)
    light = find_next(water, water_to_light_map)
    temp = find_next(light, light_to_temp_map)
    humid = find_next(temp, temp_to_humid_map)
    location = find_next(humid, humid_to_location_map)
    return location


def find_lowest(seed, _map):
    for idx, entry in enumerate(_map):
        print(entry)


def find_lowest_seed(seed):
    soil = find_lowest(seed, seed_to_soil_map)


def part1():
    seeds = read_seeds('../res/part1/test/seeds.txt')
    locations = []
    for seed in seeds:
        locations.append(find_location_for_seed(seed))

    print(min(locations))


def part2():
    locations = []


seed_to_soil_map = read_next_map('../res/part1/test/seed-to-soil.txt')
soil_to_fertilizer_map = read_next_map('../res/part1/test/soil-to-fertilizer.txt')
fertilizer_to_water_map = read_next_map('../res/part1/test/fertilizer-to-water.txt')
water_to_light_map = read_next_map('../res/part1/test/water-to-light.txt')
light_to_temp_map = read_next_map('../res/part1/test/light-to-temperature.txt')
temp_to_humid_map = read_next_map('../res/part1/test/temperature-to-humidity.txt')
humid_to_location_map = read_next_map('../res/part1/test/humidity-to-location.txt')

# main
print('########## PART 1 ##########')
part1()

print('########## PART 2 ##########')
part2()

