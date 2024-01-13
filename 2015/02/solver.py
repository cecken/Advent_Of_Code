def main():
    with open('input.txt', 'r') as f:
        lines = f.readlines()

    total_paper = 0
    total_ribbon = 0
    for line in lines:
        dim = [int(x) for x in line.replace('\n', '').split('x')]
        dim.sort()
        wl = dim[0] * dim[1]
        lh = dim[1] * dim[2]
        wh = dim[0] * dim[2]
        total_paper += (2*wl) + (2*lh) + (2*wh) + min([wl, lh, wh])

        vol = dim[0] * dim[1] * dim[2]
        total_ribbon = total_ribbon + vol + 2*dim[0] + 2*dim[1]
    
    return total_paper, total_ribbon

if __name__=='__main__':
    total_paper, total_ribbon = main()
    print(total_paper)
    print(total_ribbon)
