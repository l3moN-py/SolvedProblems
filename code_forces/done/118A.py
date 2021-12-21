word = input().lower()

print(''.join(['.'+letter for letter in word if letter not in ['a', 'e', 'i', 'o', 'u', 'y']]))
