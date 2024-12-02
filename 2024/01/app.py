

def main():
    left = []
    right = []
    with open('puzzle_input.txt', 'r') as f:
        for line in f.readlines():
            y = line.split(' ')
            left.append(int(y[0]))
            right.append(int(y[-1]))

    left.sort()
    right.sort()

    dist = 0
    sim_score = 0
    j = 0
    for i in range(len(left)):
        single_dist = abs(left[i] - right[i])
        print(f'{left[i]}, {right[i]}, {single_dist}')
        dist += single_dist
        print(f'i: {i}')
        print(f'j: {j}')
        if left[i] != left[i-1]:
            mult = 0
            if j < len(right)-1:
                while right[j] <= left[i]:
                    if right[j] == left[i]:
                        mult += 1
                    j += 1
        sim_score += (mult * left[i])

    print(f'Distance: {dist}')
    print(f'Sim Score: {sim_score}')
        
if __name__=='__main__':
    main()
