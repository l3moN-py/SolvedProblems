def too_long(word):
    lenght = len(word)
    if lenght > 10:
        return word[0] + str(lenght-2) + word[-1]
    return word

for word in [input() for _ in range(int(input()))]:
    print(too_long(word))

