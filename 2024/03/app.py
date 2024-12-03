import re

def get_sum_of_muls(muls):
    solution = 0
    for mul in muls:
            nums = [int(x) for x in mul.replace('mul(', '').replace(')', '').split(',')]
            solution += (nums[0]*nums[1])
    return solution

def main():
    pattern = re.compile('mul\([0-9]{1,3},[0-9]{1,3}\)')
    with open('input.txt', 'r') as f:
        txt = f.read()
    muls = pattern.findall(txt)
    solution = get_sum_of_muls(muls)
    print(f'Star 1 solution: {solution}')
    split = re.split("(do\(\)|don't\(\))", txt)
    split_solution = 0
    enabled = True
    for split_line in split:
        if "don't()" == split_line:
            enabled = False
        elif "do()" == split_line:
            enabled = True
        elif enabled:
            split_muls = pattern.findall(split_line)
            split_solution += get_sum_of_muls(split_muls)
    print(f'Star 2 solution: {split_solution}')

if __name__=='__main__':
    main()
