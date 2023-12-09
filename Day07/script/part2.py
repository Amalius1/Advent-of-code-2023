from Day07.script.common import read_hands, determine_points, sort_by_rank_and_points, _hand_types, determine_rank

_card_points = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'J': 1,
    'Q': 12,
    'K': 13,
    'A': 14
}


def count_cards_of_same_type(cards):
    cards_by_value = {}
    for card_name in _card_points:
        cards_by_value[card_name] = 0

    for card in cards:
        cards_by_value[card] += 1

    return {x: y for x, y in cards_by_value.items() if y != 0}


def check_if_cards_contain_joker(cards):
    for card in cards:
        if card == 'J':
            return True
    return False


def determine_rank_with_jokers(_counted_cards):
    _counted_cards_copy = _counted_cards.copy()
    _jokers = _counted_cards_copy.get('J')
    del _counted_cards_copy['J']
    _different_cards_count = len(_counted_cards_copy)
    _counted_cards_list_values = list(_counted_cards_copy.values())
    if _different_cards_count == 1 or _different_cards_count == 0:
        return _hand_types['five_of_kind']
    if _jokers == 3:
        return _hand_types['four_of_kind']
    if _jokers == 2:
        if _different_cards_count == 2:
            return _hand_types['four_of_kind']
        elif _different_cards_count == 3:
            return _hand_types['three_of_kind']

    if _jokers == 1:
        if _different_cards_count == 2:
            if _counted_cards_list_values[0] == 3 or _counted_cards_list_values[1] == 3:
                return _hand_types['four_of_kind']
            elif _counted_cards_list_values[0] == 2 or _counted_cards_list_values[1] == 2:
                return _hand_types['full_house']
            elif _different_cards_count == 3:
                return _hand_types['pair']
        if _different_cards_count == 3:
            if (_counted_cards_list_values[0] == 2
                    or _counted_cards_list_values[1] == 2
                    or _counted_cards_list_values[2] == 2):
                return _hand_types['three_of_kind']
            else:
                return _hand_types['pair']
        if _different_cards_count == 4:
            return _hand_types['pair']
    return 0


# main

found_hands = read_hands('../res/real/hands.txt')

hand_results = []

for hand in found_hands:
    count_cards = count_cards_of_same_type(hand['cards'])
    _jokers_count = 0
    if check_if_cards_contain_joker(hand['cards']):
        _jokers_count = count_cards.get('J')
        rank = determine_rank_with_jokers(count_cards)
    else:
        rank = determine_rank(count_cards)

    points = determine_points(hand['cards'], _card_points)
    hand_results.append(
        {'cards': hand['cards'], 'bid': hand['bid'], 'rank': rank, 'points': points, 'jokers': _jokers_count})

sorted_result = sort_by_rank_and_points(hand_results)
print(sorted_result)
_i = 1
_sum = 0
for _hand in sorted_result:
    _sum += _hand['bid'] * _i
    _i += 1
print(_sum)
