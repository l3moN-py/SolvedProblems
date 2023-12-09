from script import loadExample, loadTxt


def calcScratchcards(cardDeck):
    cardsNumber = [1 for _ in range(len(cardDeck))]

    for i in range(len(cardDeck)):
        cardPack = cardDeck[i]
        winningCards, elfsCard = cardPack
        winningTimes = 0
        for winningCard in winningCards:
            if winningCard in elfsCard:
                winningTimes += 1
        cardsNumber = cardsNumber[:i+1] + list(map(lambda x: x+cardsNumber[i], cardsNumber[i+1:i+1+winningTimes])) + cardsNumber[i+1+winningTimes:]

    return sum(cardsNumber)


def calcWinning(cardDeck):
    count = 0

    winningCards, elfsCard = cardDeck

    for winningCard in winningCards:
        if winningCard in elfsCard:
            count += 1

    return 0 if count == 0 else 2**(count-1)


def processCards(cards):
    cards = [card.split(": ")[1].split(" | ") for card in cards]
    cards = [[set(card[0].split()), set(card[1].split())] for card in cards]
    return cards


def partOne():
    cards = loadExample()
    cards = loadTxt("day4")
    cards = processCards(cards)
    cardsWinningSum = sum([calcWinning(card) for card in cards])
    return cardsWinningSum


def partTwo():
    cards = loadExample()
    cards = loadTxt("day4")
    cards = processCards(cards)

    return calcScratchcards(cards)


if __name__ == "__main__":
    print(
        f"Part One: {partOne()}\n"
        f"Part Two: {partTwo()}"
    )



