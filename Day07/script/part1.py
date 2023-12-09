from Day07.script.common import read_hands, determine_rank, determine_points

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
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14
}

_hand_types = {
    'high': 1,
    'pair': 2,
    'two_pairs': 3,
    'three_of_kind': 4,
    'full_house': 5,
    'four_of_kind': 6,
    'five_of_kind': 7
}


def count_cards_of_same_type(cards):
    cards_by_value = {}
    for card_name in _card_points:
        cards_by_value[card_name] = 0

    for card in cards:
        cards_by_value[card] += 1

    return {x: y for x, y in cards_by_value.items() if y != 0}



def sort_by_rank_and_points(hands):
    hands.sort(key=lambda x: (x['rank'], x['points']), reverse=False)
    return hands


# main

found_hands = read_hands('../res/real/hands.txt')

hand_results = []

for hand in found_hands:
    count_cards = count_cards_of_same_type(hand['cards'])
    rank = determine_rank(count_cards)
    points = determine_points(hand['cards'], _card_points)
    hand_results.append({'rank': rank, 'points': points, 'bid': hand['bid'], 'cards': hand['cards']})

sorted_result = sort_by_rank_and_points(hand_results)
print(sorted_result)
_i = 1
_sum = 0
for _hand in sorted_result:
    _sum += _hand['bid'] * _i
    _i += 1
print(_sum)
