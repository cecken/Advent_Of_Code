import re

def get_line_score(line:str):
    score = len(re.findall('XMAS', line))
    score += len(re.findall('SAMX', line))
    return score

def transpose_list_of_str(str_lst):
    '''Only works for lists with consistently sized strings'''
    # TODO: Make dynamic
    lst_of_lsts = [list(string) for string in str_lst]
    transpose_list = []
    for i in range(len(lst_of_lsts[0])):
        transpose_list.append([])
        for lst in lst_of_lsts:
            if len(lst) > 0:
                transpose_list[i].append(lst[i])
    return [''.join(lst) for lst in transpose_list]

def rotate(str_lst, counterclockwise=False):
    lst_of_lsts = [list(string) for string in str_lst]
    if counterclockwise:
        for lst in lst_of_lsts:
            lst.reverse()

    max_ = len(lst_of_lsts) + len(lst_of_lsts[1])
    diag_mat = []
    for i in range(max_+1):
        x = min(i, len(lst_of_lsts)-1)
        y = i - x
        diag_mat.append([])
        while (x + y <= i) and (x >= 0) and (y < len(lst_of_lsts)):
            diag_mat[i].append(lst_of_lsts[x][y])
            x -= 1
            y += 1
    return [''.join(x) for x in diag_mat]

def get_cross_mas(str_lst):
    score = 0
    lst_of_lsts = [list(x) for x in str_lst]
    for i in range(1, len(lst_of_lsts)-1):
        for j in range(1, len(lst_of_lsts[0])-1):
                if lst_of_lsts[i][j] == 'A':
                    f_sl_1 = lst_of_lsts[i-1][j-1]=='S' and lst_of_lsts[i+1][j+1]=='M'
                    f_sl_2 = lst_of_lsts[i-1][j-1]=='M' and lst_of_lsts[i+1][j+1]=='S'
                    b_sl_1 = lst_of_lsts[i+1][j-1]=='S' and lst_of_lsts[i-1][j+1]=='M'
                    b_sl_2 = lst_of_lsts[i+1][j-1]=='M' and lst_of_lsts[i-1][j+1]=='S'
                    f_sl = f_sl_1 or f_sl_2
                    b_sl = b_sl_1 or b_sl_2
                    if (f_sl and b_sl):
                        score += 1
    return score

def main():
    solution = 0
    ## Start with left/right case
    with open('test.txt', 'r') as f:
        data = f.read()
    new_data = data.split('\n')[:-1] #take out null string at end
    for datum in new_data:
        solution += get_line_score(datum)
    print(f'Horizontal :{solution}')
    ## Transpose for up/down case
    transpose_list = transpose_list_of_str(new_data)
    for line in transpose_list:
        solution += get_line_score(line)
    print(f'Hor+Vert:{solution}')
    ## Diagonal Case
    ## Note that with forward and backward search (XMAS|SAMX) there
    ## Are two diagonal cases, rotate left / right 45 degrees
    clock_mat = rotate(new_data)
    for line in clock_mat:
        solution += get_line_score(line)
    print(f'Hor+Vert+clockwise:{solution}')
    counter_mat = rotate(new_data, True)
    for line in counter_mat:
        solution += get_line_score(line)
    print(f'All: {solution}')
    print('Solution 2')
    new_score = get_cross_mas(new_data)
    print(f'Score 2: {new_score}')

if __name__=='__main__':
    main()
