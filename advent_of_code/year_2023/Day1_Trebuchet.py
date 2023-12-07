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
        line = loadedData[lineIndex]

        mostRecentNumberPosition = (len(line), "none")

        for num in numbers:
            foundNumber = line.find(num)
            if foundNumber != -1 and foundNumber < mostRecentNumberPosition[0]:
                mostRecentNumberPosition = (foundNumber, str(num))

        letter = mostRecentNumberPosition[1]

        mostRecentNumberPosition = (len(line), "none")

        for num in numbers:
            num = num[::-1]
            foundNumber = line[::-1].find(num)
            if foundNumber != -1 and foundNumber < mostRecentNumberPosition[0]:
                mostRecentNumberPosition = (foundNumber, num)

        letter2 = mostRecentNumberPosition[1]

        start = line.replace(letter, str(numbers.index(str(letter)) + 1)) if letter != "none" else line
        end = line[::-1].replace(letter2, str(numbers.index(str(letter2[::-1])) + 1))[::-1] if letter2 != "none" else line

        loadedData[lineIndex] = start + end



    return calculate(loadedData)


if __name__ == "__main__":
    print(
        f"Part One: {partOne()}\n"
        f"Part Two: {partTwo()}"
    )
