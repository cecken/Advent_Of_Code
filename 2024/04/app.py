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

    max_input = len(lst_of_lsts) + len(lst_of_lsts[1])
    diag_mat = []
    for i in range(max_input+1):
        x = min(i, len(lst_of_lsts)-1)
        y = i - x
        diag_mat.append([])
        while (x + y <= i) and (x >= 0) and (y < len(lst_of_lsts)):
            diag_mat[i].append(lst_of_lsts[x][y])
            x -= 1
            y += 1
    return [''.join(x) for x in diag_mat]

def main():
    solution = 0
    ## Start with left/right case
    with open('input.txt', 'r') as f:
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



if __name__=='__main__':
    main()
