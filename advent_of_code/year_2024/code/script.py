def loadExample():
    with open("../txt/example.txt") as file:
        return [line.replace("\n", "") for line in file.readlines()]


def loadTxt(name):
    with open(f'../txt/{name}.txt') as file:
        return [line.replace("\n", "") for line in file.readlines()]