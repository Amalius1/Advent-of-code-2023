from io import open

# props
dict = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}


def find_first_digit(line):
    for c in line:
        if c.isdigit():
            return c

    return 0


def find_last_digit(line):
    for c in reversed(line):
        if c.isdigit():
            return c

    return 0


def find_first_text_digit(line):
    for i, char in enumerate(line):
        if char.isdigit():
            return char
        for text, digit in dict.items():
            if line[i:].startswith(text):
                return digit
    return 0


def find_last_text_digit(line):
    result = 0
    for i, char in enumerate(line):
        if char.isdigit():
            result = char
        for text, digit in dict.items():
            if line[i:].startswith(text):
                result = digit
    return result


def part_1():
    sums = 0

    file_path = '../res/part1/real_input.txt'

    file = open(file_path)
    for line in file.readlines():
        first_digit = find_first_digit(line)
        last_digit = find_last_digit(line)
        combined = first_digit + last_digit
        sums += int(combined)

    print('Total sum: ' + str(sums))


def part_2():
    sums = 0
    file_path = '../res/part2/real_input.txt'
    file = open(file_path)

    for line in file.readlines():
        combined = (str(find_first_text_digit(line)) + str(find_last_text_digit(line)))
        sums += int(combined)

    print('Total sum: ' + str(sums))


# main
print("################# PART 1 #######################")
part_1()
print("################# PART 2 #######################")
part_2()
