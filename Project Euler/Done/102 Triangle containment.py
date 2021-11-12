def split_list(alist, wanted_parts):
    length = len(alist)
    return [alist[i*length // wanted_parts: (i+1)*length // wanted_parts] for i in range(wanted_parts)]
def Test(r):
    for test in ['x+', 'y-', 'y+', 'x-']:
        if test not in r:
            return False
    return True
def rovnica(X, Y):
    x = ''
    y = ''
    if X[0] - Y[0] == 0:
        a = 0
    elif X[0] - Y[0] != 0:
        a = (X[1] - Y[1]) / (X[0] - Y[0])

    b = X[1] - a*X[0]

    if a == 0:
        Px = 0
    elif a != 0:
        Px = -b/a

    Py = a*0 + b

    if X[0] <= Px <= Y[0] or X[0] >= Px >= Y[0]:
        if Px > 0:
            x = 'x+'
        else:
            x = 'x-'
    if X[1] <= Py <= Y[1] or X[1] >= Py >= Y[1]:
        if Py > 0:
            y = 'y+'
        else:
            y = 'y-'
    return x,y

count = 0
f = open(r'C:\Users\Klacik\Desktop\Programing\Python\Project Euler\Text\p102_triangles.txt')
x = [[a for a in map(int, line.split(','))] for line in f]
#x = [list(map(int, input().split())) for _ in range(int(input()))] 
print(x)
import sys
sys.exit()
for num in x:
    num = split_list(num, 3)
    result = rovnica(num[0], num[1]) + rovnica(num[1], num[2]) + rovnica(num[0], num[2])
    if Test(result):
        count += 1
print('Answer:', count)
