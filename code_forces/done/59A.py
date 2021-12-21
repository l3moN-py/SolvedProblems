word = input()

upper = sum([1 for l in word if l.isupper()])

if upper > len(word)//2:
    print(word.upper())
else:
    print(word.lower())