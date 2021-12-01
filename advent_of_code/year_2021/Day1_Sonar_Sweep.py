with open(r'txt_files/day1.txt') as f:
    data = f.read().splitlines()
    data = list(map(int, data))


def first_star():
    count = 0
    for i in range(len(data)-1):
        if data[i] < data[i+1]:
            count += 1
    # print(data)
    print(count)
first_star()


def second_star():
    count = 0
    for i in range(len(data)-3):
        # print(data[i:i+3])
        if sum(data[i:i+3]) < sum(data[i+1:i+4]):
            count += 1
    print(count)
second_star()