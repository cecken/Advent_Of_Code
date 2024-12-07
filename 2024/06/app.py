import re

def get_initial_position(board):
    for i, row in enumerate(board):
            if '^' in row:
                index = row.index('^')
                return index, i
    return

def move_guard(board, x, y):
    guard = board[y][x]
    new_x = x
    new_y = y
    new_guard = ''
    match guard:
        case '^':
            new_y = y - 1
            new_guard = '>'
        case '>':
            new_x = x + 1
            new_guard = 'v'
        case 'v':
            new_y = y + 1
            new_guard = '<'
        case '<':
            new_x = x - 1
            new_guard = '^'
    y_valid = (new_y >= 0) and (new_y < len(board))
    x_valid = (new_x >= 0) and (new_x < len(board[0]))
    if not y_valid or not x_valid:
        board[y][x] = 'X'
        new_x = -1
        new_y = -1
    elif board[new_y][new_x] == '#':
        board[y][x] = new_guard
        new_x = x
        new_y = y
    else:
        board[new_y][new_x] = guard
        board[y][x] = 'X'
    return board, new_x, new_y

def remove_guard_from_board(board_str):
    new_board = board_str.replace('^', 'X').replace('>', 'X')
    new_board = new_board.replace('v', 'X').replace('<', 'X')
    return new_board

def get_edges(current_guard, board, edges):
    new_edges = edges
    new_guard = current_guard
    if current_guard not in '\n'.join([''.join(row) for row in board]):
        match current_guard:
            case '^':
                new_guard = '>'
            case '>':
                new_guard = 'v'
            case 'v':
                new_guard = '<'
            case '<':
                new_guard = '^'
        for i, row in enumerate(board):
            if new_guard in row:
                new_edges.append([i, row.index(new_guard)])
    return new_edges, new_guard

def main():
    with open('input.txt', 'r') as f:
        data = f.read()
    data = data.split('\n')
    data = [list(datum) for datum in data[:-1]]
    init_x, init_y = get_initial_position(data)
    edges = [[init_y, init_x]]
    board, x, y = move_guard(data, init_x, init_y)
    current_guard = '^'
    while (x > 0) or (y > 0):
        board, x, y = move_guard(board, x, y)
        board_str = '\n'.join([''.join(row) for row in board])
        edges, current_guard = get_edges(current_guard, board, edges)
    print('Complete')
    num_positions = len(re.findall('X', board_str))
    print(num_positions)
    print(len(edges))
    print(edges)


if __name__=='__main__':
    main()

