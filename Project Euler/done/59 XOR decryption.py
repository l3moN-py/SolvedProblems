#ASCII
#a=97; z=122
import re
from itertools import combinations_with_replacement

with open(r'C:\Users\Klacik\Desktop\Programing\Python\Project Euler\Text\p059_cipher.txt') as f:
    f = list(map(int, f.read().split(',')))
#print(f)

def comb():
    for i in range(97, 122+1):
        for j in range(97, 122+1):
            for l in range(97, 122+1):
                yield [i,j,l]
                
    # arange = range(97,123)
    # brange = range(97,123)
    # crange = range(97,123)
    # ranges = [arange, brange, crange]


    

def foo(file, passwd):
    return ''.join([chr(file[i] ^ passwd[i%len(passwd)]) for i in range(len(file))])

def too():
    for i in list(comb()):
        text = foo(f[:20], i)
        if bool(re.match(r'^[a-zA-Z\s\d]+$', text)):
            print(i, text)
    #print(text)
#too()

def decrypt(file, code):
    return sum([int(file[i] ^ code[i%len(code)]) for i in range(len(file))])

print(decrypt(f, [101, 120, 112]))