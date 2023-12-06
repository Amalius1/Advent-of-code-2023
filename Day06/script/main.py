def count_ways(race):
    r_time = race['time']
    r_distance = race['distance']

    count = 0

    for min_speed in range(0, r_time):
        time_left = r_time - min_speed
        distance = time_left * min_speed
        if distance > r_distance:
            count += 1
    return count


def part1():
    races = []
    races.append({'time': 53, 'distance': 333})
    races.append({'time': 83, 'distance': 1635})
    races.append({'time': 72, 'distance': 1289})
    races.append({'time': 88, 'distance': 1532})

    result = 1
    for race in races:
        result *= count_ways(race)

    print(result)


def part2():
    res = count_ways({'time': 53837288, 'distance': 333163512891532})
    print(res)


# main

print('########## PART 1 ##########')
part1()

print('########## PART 2 ##########')
part2()
