from io import open
import re
import uuid


def load_data(path):
    matrix = []
    with open(path) as file:
        for line in file.readlines():
            matrix.append(line.strip('\n'))
    return matrix


def find_numbers(line):
    number_index = []
    pattern = r'\d+'
    matches = re.finditer(pattern, line)
    for match in matches:
        number = match.group()
        number_id = uuid.uuid4()
        start_index = match.start()
        number_index.append({'number': number, 'idx': start_index, 'id': number_id})

    return number_index


def check_if_has_char_in_area(matrix, index_number, row_number, number):
    search_matrix = []
    number_length = len(str(number))
    matrix_length = len(matrix)
    index_start = 0
    index_end = index_number + number_length + 1
    if not index_number == 0:
        index_start = index_number - 1
    if 0 < row_number < matrix_length - 1:
        search_matrix.append(matrix[row_number - 1][index_start:index_end])
        search_matrix.append(matrix[row_number][index_start:index_end])
        search_matrix.append(matrix[row_number + 1][index_start:index_end])
    elif row_number == 0:
        search_matrix.append(matrix[row_number][index_start:index_end])
        search_matrix.append(matrix[row_number + 1][index_start:index_end])
    elif row_number == matrix_length - 1:
        search_matrix.append(matrix[row_number - 1][index_start:index_end])
        search_matrix.append(matrix[row_number][index_start:index_end])

    for line in search_matrix:
        for char in line:
            if not char == '.' and not char.isdigit():
                return True

    return False


def find_gears_coords(matrix):
    pattern = r'\*'
    indexes = []
    i = 0
    for line in matrix:
        matches = re.finditer(pattern, line)
        for match in matches:
            x = match.start()
            indexes.append({'col': x, 'row': i})
        i += 1
    return indexes


def find_numbers_coords_near_gear(matrix, col_num, row_num):
    max_row = len(matrix)
    max_col = len(matrix[row_num])
    search_matrix = []
    used_ids = []
    if not row_num == 0 and not col_num == 0 and not row_num == max_row and not col_num == max_col:
        for row in range(row_num - 1, row_num + 2):
            for col in range(col_num - 1, col_num + 2):
                field = matrix[row][col]
                if not isinstance(field, str) and field['number'].isnumeric() and field['id'] not in used_ids:
                    search_matrix.append(field['number'])
                    used_ids.append(field['id'])
    if len(search_matrix) == 2:
        return search_matrix
    else:
        return []


def normalize_matrix(matrix):
    target_matrix = []
    used_ids = []
    for line in matrix:
        array_line = [*line.strip()]
        target_matrix.append(array_line)
        numbers = find_numbers(line)
        for number in numbers:
            number_id_ = number['id']
            if number_id_ not in used_ids:
                value = number['number']
                number_of_swaps = len(str(value))
                idx = number['idx']
                for i in range(0, number_of_swaps):
                    array_line[idx] = {'number': value, 'id': number_id_}
                    idx += 1
                used_ids.append(number_id_)

    return target_matrix


def part1():
    data = load_data('../res/part1/real_data.txt')

    i = 0
    total_sum = 0
    for line in data:
        numbers = find_numbers(line)
        for number in numbers:
            result = check_if_has_char_in_area(data, number['idx'], i, number['number'])
            if result:
                total_sum += int(number['number'])
        i += 1

    print(total_sum)


def part2():
    data = load_data('../res/part2/real_data.txt')
    normalized = normalize_matrix(data)
    coords = find_gears_coords(data)
    ratio = 0
    for coord in coords:
        result = find_numbers_coords_near_gear(normalized, coord['col'], coord['row'])
        if len(result) == 2:
            ratio += int(result[0]) * int(result[1])

    print(ratio)


# main
print('########## PART 1 ##########')
part1()
print('########## PART 2 ##########')
part2()
