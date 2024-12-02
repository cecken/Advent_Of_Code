def main():
    safe = 0
    with open('input.txt', 'r') as f:
        for idx, line in enumerate(f.readlines()):
            mono_down = True
            mono_up = True
            diff_max = 0
            levels = [int(x) for x in line.split(' ')]
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
                safe += 1
                print(f'{idx}: {line}')
                print(f'mono_up: {mono_up}, mono_down: {mono_down}')
    print(f'Num Safe: {safe}')


if __name__=='__main__':
    main()
