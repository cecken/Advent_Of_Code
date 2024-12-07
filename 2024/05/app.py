def get_direction_dictionary(data):
    lines = data.split('\n')
    directions = {}
    for line in lines:
        order = line.split('|')
        num_str = order[0]
        if num_str not in directions.keys():
            directions[num_str] = []
        directions[num_str].append(line)
    return directions

def check_valid_update(pages, directions):
    for page in pages:
        if page not in directions.keys():
            continue
        direction = directions[page]
        for order in direction:
            left, right = order.split('|')
            if (left in pages) and (right in pages):
                if pages.index(right) < pages.index(left):
                    return False
    return True

def find_correct_order(pages, directions):
    new_pages = pages.copy()
    i = len(new_pages)
    incorrect = True
    while incorrect:
        check = True
        incorrect = not check_valid_update(new_pages, directions)
        if new_pages[i-1] not in directions.keys():
            i -= 1
            continue
        page_directions = directions[new_pages[i - 1]]
        for order in page_directions:
            left, right = order.split('|')
            if right in new_pages[:i-1]:
                if new_pages.index(left) > new_pages.index(right):
                    check = False
                    idx = new_pages.index(right)
                    new_pages.pop(idx)
                    new_pages.insert(i-1, right)
        if check:
            i -= 1
    return new_pages
            
def main():
    with open('input.txt', 'r') as f:
        data = f.read()
    split_data = data.split('\n\n')
    directions = get_direction_dictionary(split_data[0])
    updates = split_data[1].split('\n')
    middle_page_total = 0
    corrected_total = 0
    for update in updates:
        if len(update) < 1:
            continue
        pages = update.split(',')
        valid = check_valid_update(pages, directions)
        if valid:
            middle_page_total += int(pages[len(pages)//2])
        else:
            sorted_pages = find_correct_order(pages, directions)
            corrected_total += int(sorted_pages[len(sorted_pages)//2])
    print(f'Puzzle 1: {middle_page_total}')
    print(f'Puzzle 2: {corrected_total}')

if __name__=='__main__':
    main()

