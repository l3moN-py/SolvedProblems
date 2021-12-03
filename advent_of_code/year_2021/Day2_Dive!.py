if __name__ == '__main__':
    with open(r'txt_files/day2.txt') as f:
        data = f.read().splitlines()
    data = [d.split() for d in data]

    def first_star():
        depth = 0
        horizontal = 0
        for instruction, value in data:
            value = int(value)
            if instruction == 'forward':
                horizontal += value
            elif instruction == 'down':
                depth += value
            else:
                depth = depth - value if depth - value >= 0 else 0
        return depth*horizontal
    print(f'First star answer: {first_star()}\n')

    def second_star():
        depth, horizontal, aim = 0, 0, 0
        for instruction, value in data:
            value = int(value)
            if instruction == 'down':
                aim += value
            elif instruction == 'up':
                aim -= value
            else:
                horizontal += value
                depth += aim*value
        return depth*horizontal
    print(f'Second star answer: {second_star()}')