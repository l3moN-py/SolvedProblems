from script import loadExample, loadTxt
import re




def isNumber(num):
    numbers = "".join([str(n) for n in range(10)])

    return num in numbers

def isEngine(file, it, lineIndex):


    lenOfLine = len(file[0])

    startColumnIndex = max(0, it.start() - 1)
    endColumnIndex = min(it.end() + 1, lenOfLine)

    startRowIndex = max(0, lineIndex-1)
    endRowIndex = min(len(file), lineIndex + 2)

    box = []
    for rowIndex in range(startRowIndex, endRowIndex):
        row = file[rowIndex][startColumnIndex:endColumnIndex]
        box.append(row)

    box = "".join(box)
    box = [letter for letter in box if (letter != ".") and not (isNumber(letter))]

    return len(box) > 0

def partOne():
    file = loadExample()
    file = loadTxt("day3")
    pattern = r"\d+"
    result = 0

    for i in range(len(file)):
        data = file[i]
        foundNumbers = re.finditer(pattern, data)
        for foundNumber in foundNumbers:
            if isEngine(file, foundNumber, i):
                result += int(foundNumber.group())
    return result


def partTwo():
    return -1


if __name__ == "__main__":
    print(
        f"Part One: {partOne()}\n"
        f"Part Two: {partTwo()}"
    )



