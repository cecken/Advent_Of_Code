def check_safe(levels: list[int]):
    mono_down = True
    mono_up = True
    diff_max = 0
    for i in range(1,len(levels)):
        if levels[i] <= levels[i-1]:
            mono_up = False
        if levels[i] >= levels[i-1]:
            mono_down = False
        diff = abs(levels[i] - levels[i-1])
        if diff > diff_max:
            diff_max = diff
    monotonic = mono_down or mono_up
    if monotonic and (diff_max < 4):
        return True
    return False


def main():
    safe = 0
    with open('input.txt', 'r') as f:
        for idx, line in enumerate(f.readlines()):
            levels = [int(x) for x in line.split(' ')]
            if check_safe(levels):
                safe += 1
            else:
                for i in range(len(levels)):
                    ### Brute Forcing. This is inelegant, but quick
                    new_levels = levels.copy()
                    new_levels.pop(i)
                    if check_safe(new_levels):
                        safe += 1
                        break

    print(f'Num Safe: {safe}')


if __name__=='__main__':
    main()
