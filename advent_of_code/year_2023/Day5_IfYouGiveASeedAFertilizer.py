from script import loadExample, loadTxt


def getCorrespondingValue(converter, value):
    for valueRange in converter:
        if value in range(valueRange[1], valueRange[1] + valueRange[2]):
            return value - valueRange[1] + valueRange[0]
    else:
        return value


def partOne():
    data = loadExample()
    data = loadTxt("day5")
    formattedData = [[]]
    for d in data:
        if d != "":
            formattedData[-1].append(d)
        else:
            formattedData.append([])

    formattedData[0] = list(map(lambda x: int(x), "".join(formattedData[0]).replace("seeds: ", "").split()))

    for i in range(1, len(formattedData)):
        converterValues = list(map(lambda x: [int(y) for y in x.split()], formattedData[i][1:]))
        formattedData[i] = converterValues

    seedValues = []

    for seed in formattedData[0]:
        lookingValue = seed
        for converter in formattedData[1:]:
            lookingValue = getCorrespondingValue(converter, lookingValue)
        else:
            # print("Seed:", seed, "| Seed location:", lookingValue)
            seedValues.append(lookingValue)

    return min(seedValues)


def partTwo():
    return -1


if __name__ == "__main__":
    print(
        f"Part One: {partOne()}\n"
        f"Part Two: {partTwo()}"
    )
