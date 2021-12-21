import re

with open(r'Python\Advent of Code\2020\day8inputE') as f:
    data = f.readlines()

#first star
def foo(i=0, acc=0, pp = set()):
    while True:
        ins, num = re.search(r'(\w{3})\s(\+\d+|-\d+)', data[i]).groups()
        #print(ins, num)
        if i in pp or len(data) < i:
            return acc
        pp.add(i)
        if ins == 'acc':
            acc += int(num)

        if ins == 'jmp':
            i += int(num)
        else:
            i += 1

#print("First star:", foo())

#second star
def doo():
    return 

print("Second star:", doo())