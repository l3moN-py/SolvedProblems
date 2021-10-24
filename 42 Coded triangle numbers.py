import string

def triangle(word):
    t = sum([int(alphabetic.index(n) + 1) for n in list(word)])
    x = (-1+(1-4*(-2*t))**0.5)/2
    if x == int(x):
        return True
    return False

alphabetic = list(string.ascii_uppercase)
file = open(r'C:\Users\Klacik\Desktop\Python\Project Euler\Text\p042_words.txt').readlines()
word_list = [a.replace('"', '') for a in ''.join(file).split(',')]
c = 0

for word in word_list:
    if triangle(word):
        c += 1

print('Answer:', c)


#Other solution (not mine)

#from itertools import permutations
#print(sum(int(''.join(x)) for x in permutations('0123456789', 10) if all([not int(''.join(x)[n[0]:n[1]]) % n[2] for n in [(1, 4, 2), (2, 5, 3), (3, 6, 5), (4, 7, 7), (5, 8, 11), (6, 9, 13), (7, 10, 17)][:7]])))
