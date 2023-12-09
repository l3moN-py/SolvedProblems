import math

from script import loadExample, loadTxt
import re


def calcWinning(cardDeck):
    count = 0

    winningCards, elfsCard = cardDeck

    for winningCard in winningCards:
        if winningCard in elfsCard:
            count += 1

    return 0 if count == 0 else 2**(count-1)


def partOne():
    cards = loadExample()
    cards = loadTxt("day4")
    cards = [card.split(": ")[1].split(" | ") for card in cards]
    cards = [[set(card[0].split()), set(card[1].split())] for card in cards]
    cardsWinningSum = sum([calcWinning(card) for card in cards])
    return cardsWinningSum


def partTwo():

    return -1


if __name__ == "__main__":
    print(
        f"Part One: {partOne()}\n"
        f"Part Two: {partTwo()}"
    )



