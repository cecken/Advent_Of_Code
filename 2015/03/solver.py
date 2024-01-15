class Santa():

    def __init__(self):
        self.x = 0
        self.y = 0
        self.visited = set()
        self.visited.add(f'{self.x}_{self.y}')

    def move(self, direction):
        if direction == '>':
            self.x += 1
        elif direction == '<':
            self.x -= 1
        elif direction == 'v':
            self.y -= 1
        elif direction == '^':
            self.y += 1
        self.visited.add(f'{self.x}_{self.y}')
     

def main():
    with open('input.txt', 'r') as f:
        input = f.read()
    santa = Santa()
    robot_santa = Santa()

    for i, direction in enumerate(input):
        if i % 2 == 0:
            santa.move(direction)
        else:
            robot_santa.move(direction)

    visted_houses = santa.visited.union(robot_santa.visited)
    return len(visted_houses)

if __name__ == '__main__':
    num_houses_visited = main()
    print(num_houses_visited)
