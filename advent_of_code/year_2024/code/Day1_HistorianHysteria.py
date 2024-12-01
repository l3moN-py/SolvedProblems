from script import loadExample, loadTxt

def partOne():
    loadedData = loadTxt("day1")
    # loadedData = loadExample()

    array_1, array_2 = zip(*(map(int, s.split()) for s in loadedData))

    array_1 = list(array_1)
    array_2 = list(array_2)

    array_1.sort()
    array_2.sort()

    return sum([abs(a - b) for a, b in zip(array_1, array_2)])


def partTwo():
    loadedData = loadTxt("day1")
    # loadedData = loadExample()

    array_1, array_2 = zip(*(map(int, s.split()) for s in loadedData))

    counts_1 = {num: array_1.count(num) for num in set(array_1)}
    counts_2 = {num: array_2.count(num) for num in set(array_2)}

    return sum([counts_2[key] * key * value if key in counts_2 else 0 for key, value in counts_1.items()])


if __name__ == "__main__":
    print(
        f"Part One: {partOne()}\n"
        f"Part Two: {partTwo()}"
    )
