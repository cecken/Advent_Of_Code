def main():
    input_str = get_input()
    floor, first_down = get_floor(input_str) 
    return floor, first_down

def get_input() -> str:
    with open('input.txt', 'r') as f:
        input_str = f.read()
    return input_str

def get_floor(input_str):
    floor = 0
    first_down = len(input_str)+1
    check = True
    for i, char in enumerate(input_str):
        if char == '(':
            floor += 1
        elif char == ')':
            floor -= 1
        if check:
            if floor < 0:
                first_down = i
                check = False
    return floor, first_down + 1


if __name__=='__main__':
    floor, first_down = main()
    print(floor)
    print(first_down)
