import sys
sys.setrecursionlimit(10000)
maze = ['??????????????????????????????', '#..............???????????????', '#.#############???????????????', '#.....T........???????????????', '#.......................#.#..#', '#.#######################.#..#', '#.....##......##......#....###', '#...####..##..##..##..#..#...#', '#.........##......##.....#.C.#', '##############################']
rows = len(maze)
columns = len(maze[0])
c = [[x, maze[x].index('C')] for x in range(rows) if 'C' in maze[x]][0]
t = [[x, maze[x].index('T')] for x in range(rows) if 'T' in maze[x]][0]
x = [c]
def find_path(start, end):
    global x
    for i in range(4):
        if x[-1] == end:
            return x
        #print(x[-1])
        if 0 < x[-1][0] <= rows and maze[x[-1][0]-1][x[-1][1]] in ['.', 'T']: #up
            l = list(maze[x[-1][0]-1])
            l[x[-1][1]] = 'X'
            maze[x[-1][0]-1] = ''.join(l)
            x.append([x[-1][0]-1, x[-1][1]])
            find_path(maze[x[-1][0]][x[-1][1]], t)
            #find_path(maze[x[-1][0]-1][x[-1][1]], t)
        elif x[-1][0] < (rows-1) and maze[x[-1][0]+1][x[-1][1]] in ['.', 'T']: #down
            l = list(maze[x[-1][0]+1])
            l[x[-1][1]] = 'X'
            maze[x[-1][0]+1] = ''.join(l)
            x.append([x[-1][0]+1, x[-1][1]])
            find_path(maze[x[-1][0]][x[-1][1]], t)
            #find_path(maze[x[-1][0]+1][x[-1][1]], t)
        elif x[-1][1] < (columns-1) and maze[x[-1][0]][x[-1][1]+1] in ['.', 'T']: #right
            l = list(maze[x[-1][0]])
            l[x[-1][1]+1] = 'X'
            maze[x[-1][0]] = ''.join(l)
            x.append([x[-1][0], x[-1][1]+1])
            find_path(maze[x[-1][0]][x[-1][1]], t)
            #find_path(maze[x[-1][0]][x[-1][1]+1], t)
        elif 0 < x[-1][1] and maze[x[-1][0]][x[-1][1]-1] in ['.', 'T']: #left
            l = list(maze[x[-1][0]])
            l[x[-1][1]-1] = 'X'
            maze[x[-1][0]] = ''.join(l)
            x.append([x[-1][0], x[-1][1]-1])
            find_path(maze[x[-1][0]][x[-1][1]], t)
            #find_path(maze[x[-1][0]][x[-1][1]-1], t)
        else:
            x.pop()


path = find_path(c, t)
for
