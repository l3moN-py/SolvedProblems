from script import loadExample, loadTxt


def calculate(loadedData):
    calibrationValue = 0

    for data in loadedData:
        value = ''.join([letter for letter in data if letter.isdigit()])
        if value == "":
            value = "0"
        value = value[0] + value[-1]
        calibrationValue += int(value)
        print(value, end=" ")
    print("\n")

    return calibrationValue


def partOne():
    loadedData = loadTxt("day1")

    return calculate(loadedData)


def partTwo():
    loadedData = loadTxt("day1")
    # loadedData = loadExample()

    numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    for lineIndex in range(len(loadedData)):
        front = []
        back = []
        for num in numbers:
            front.append([num, loadedData[lineIndex].find(num)])
            back.append([num, loadedData[lineIndex][::-1].find(num[::-1])])

        front = list(filter(lambda x: x[1] != -1, front))
        front.sort(key=lambda x: x[1])
        if front:
            frontNumber = front[0]
            loadedData[lineIndex] = loadedData[lineIndex][:(frontNumber[1]+len(frontNumber[0]))].replace(frontNumber[0], str(numbers.index(frontNumber[0]) + 1)) + loadedData[lineIndex][(frontNumber[1]+len(frontNumber[0])):]

        back = list(filter(lambda x: x[1] != -1, back))
        back.sort(key=lambda x: x[1])
        if back:
            backNumber = back[0]
            loadedData[lineIndex] = loadedData[lineIndex][::-1].replace(backNumber[0][::-1], str(numbers.index(backNumber[0])+1))[::-1]

    print(loadedData)

    return calculate(loadedData)


if __name__ == "__main__":
    print(
        f"Part One: {partOne()}\n"
        f"Part Two: {partTwo()}"
    )
