from io import open


def get_ascii_value(char):
    return ord(char)


def load_data(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read().split(",")


def run_HASH_algorithm(step):
    current_value = 0
    for c in step:
        ascii_for_c = get_ascii_value(c)
        current_value += ascii_for_c
        current_value *= 17
        current_value %= 256
    return current_value


def part1():
    data = load_data("../res/input.txt")
    _sum = 0
    for step in data:
        current_value = run_HASH_algorithm(step)
        _sum += current_value
    print(_sum)


# main
if "__main__" == __name__:
    data = load_data("../res/input.txt")
    boxes = {}
    for step in data:
        _splitted = step.split('=')
        if len(_splitted) == 2:
            # add to the box,
            _label = _splitted[0].strip()
            _focal_val = int(_splitted[1].strip())
            _box_idx = str(run_HASH_algorithm(_label))
            if _box_idx not in boxes:
                boxes[_box_idx] = []

            # check if the label is already in the box or else add it
            _is_in_box = False
            for item in boxes[_box_idx]:
                if item.get('label') == _label:
                    _is_in_box = True
                    break
            if not _is_in_box:
                boxes[_box_idx].append({'label': _label, 'focal_val': _focal_val})
            else:
                for item in boxes[_box_idx]:
                    if item.get('label') == _label:
                        item['focal_val'] = _focal_val
                        break

        else:
            # remove from the box if is in the box
            _label = step.replace('-', '').strip()
            _box_idx = str(run_HASH_algorithm(_label))
            if _box_idx in boxes:
                # get box with the hash
                _box = boxes[_box_idx]
                # remove from the box element with _label
                _box[:] = [x for x in _box if x.get('label') != _label]
    # clear empty boxes
    boxes = {k: v for k, v in boxes.items() if v}

    _sum = 0
    for box_number, items in boxes.items():
        box_number_multiplier = int(box_number) + 1
        item_slot_multiplier = 1
        for item in items:
            _focal_val = item.get('focal_val')
            item_value = (_focal_val * box_number_multiplier * item_slot_multiplier)
            _sum = _sum + item_value
            item_slot_multiplier += 1

    print(_sum)
