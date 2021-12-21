import math

with open(r'Python\Advent of Code\2020\day3input') as f:
    area = f.readlines()

column = len(area[0].strip())
row = len(area)

#first star
def foo(area, s=0):
    for i in range(1, row):
        if area[i][max(0, (i*3) % column)] == '#':
            s+=1
    return s

print('How many trees?:', foo(area))

#second star
def doo(area, x, y, s=0):
    i = x
    j = y
    while True:
        if j > row - 1:
            return s
        if area[j][max(0, i % column)] == '#':
            s+=1
        i += x
        j += y
        

t = [[1,1], [3,1], [5,1], [7,1], [1,2]]
#print([doo(area, a, b) for a,b in t])
print('How many trees? (more routes) :', math.prod([doo(area, a, b) for a,b in t]))
