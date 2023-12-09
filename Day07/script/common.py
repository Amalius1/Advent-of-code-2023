_hand_types = {
    'high': 1,
    'pair': 2,
    'two_pairs': 3,
    'three_of_kind': 4,
    'full_house': 5,
    'four_of_kind': 6,
    'five_of_kind': 7
}


def read_hands(path):
    hands = []
    with open(path) as file:
        for line in file.readlines():
            game = line.split(' ')
            hands.append({'cards': game[0], 'bid': int(game[1])})
    return hands


def determine_points(_hand, _card_points):
    _score = 0
    _divider = 1.0
    for card in _hand:
        _score += _card_points.get(card) * _divider
        _divider = _divider / 100
    return _score


def sort_by_rank_and_points(hands):
    hands.sort(key=lambda x: (x['rank'], x['points']), reverse=False)
    return hands


def determine_rank(counted_cards):
    _card_count = list(counted_cards.values())
    _number_of_card_sets = len(counted_cards)
    if _number_of_card_sets == 1:
        return _hand_types['five_of_kind']
    if _number_of_card_sets == 2:
        if _card_count[0] == 4 or _card_count[1] == 4:
            return _hand_types['four_of_kind']
        elif _card_count[0] == 3 or _card_count[1] == 3:
            return _hand_types['full_house']
    if _number_of_card_sets == 3:
        if _card_count[0] == 3 or _card_count[1] == 3 or _card_count[2] == 3:
            return _hand_types['three_of_kind']
        elif _card_count[0] == 2 or _card_count[1] == 2 or _card_count[2] == 2:
            return _hand_types['two_pairs']
    if _number_of_card_sets == 4:
        return _hand_types['pair']
    if _number_of_card_sets == 5:
        return _hand_types['high']
    return 0
