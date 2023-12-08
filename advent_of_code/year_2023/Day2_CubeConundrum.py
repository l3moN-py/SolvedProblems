from functools import reduce

from script import loadExample, loadTxt

bag = {
    "red": 12,
    "green": 13,
    "blue": 14
}


def calcLine(line):
    gameId, lineData = line.split(": ")
    gameId = gameId.split(" ")[1]
    for gameSet in lineData.split("; "):
        for cube in gameSet.split(", "):
            num, color = cube.split(" ")
            if bag.get(color) < int(num):
                return 0
    return int(gameId)


def calcLineMin(line):
    colors = dict()
    lineData = line.split(": ")[1]
    for gameSet in lineData.split("; "):
        for cube in gameSet.split(", "):
            num, color = cube.split(" ")
            if color not in colors:
                colors[color] = int(num)
            elif color in colors and colors[color] < int(num):
                colors[color] = int(num)

    lineValue = reduce(lambda x, y: x*y, list(colors.values()))
    return lineValue


def partOne():
    data = loadExample()
    data = loadTxt("day2")
    validGames = 0
    for line in data:
        validGames += calcLine(line)

    return validGames


def partTwo():
    data = loadExample()
    data = loadTxt("day2")
    power = 0
    for line in data:
        power += calcLineMin(line)

    return power


if __name__ == "__main__":
    print(
        f"Part One: {partOne()}\n"
        f"Part Two: {partTwo()}"
    )
