# TODO: min function, edit this shit down


def get_nums(first, second):
    result = []
    if len(first) < len(second):
        for a in range(len(first)):
            result.append(first[a] + second[a])
            result.append(first[a] + second[a + 1])
    else:
        for a in range(len(first) - 1):
            try:
                result.append(first[a] + second[a])
                result.append(first[a] + second[a -1])
            except: pass
    return result
def get_binary(matrix, coord):
    x = []
    for i in range(coord + coord - 1):
        y = []
        for m in range(i + 1):
            try:
                y += [matrix[m].pop(0)]
            except: pass
        x.append(y)
    return x

#matrix = [[131, 673, 234, 103, 18], [201, 96, 342, 965, 150], [630, 803, 746, 422, 111], [537, 699, 497, 121, 956], [805, 732, 524, 37, 331]]
#coord = len(matrix)
#binary_tree = get_binary(matrix, coord) #[[131], [673, 201], [234, 96, 630], [103, 342, 803, 537], [18, 965, 746, 699, 805], [150, 422, 497, 732], [111, 121, 524], [956, 37], [331]]
coord = 80
f = open(r'C:\Users\Klacik\Desktop\Python\Project Euler\Text\p081_matrix.txt')
matrix = [list(map(int, row.split(','))) for row in f.readlines()]

#print(matrix)

binary_tree = get_binary(matrix, coord)
#print(binary_tree)
'''
          [131]                         [131]
       [673, 201]                    [804, 332]
     [234, 96, 630]               [1038, 428, 962]
  [103, 342, 803, 537]         [1141, 770, 1231, 1499]
[18, 965, 746, 699, 805]   [1159, 1735, 1516, 1930, 2304]
  [150, 422, 497, 732]         [1309, 1938, 2013, 3036]
     [111, 121, 524]              [1420, 2059, 3560]
        [956, 37]                   [2376, 2096]
          [331]                        [2427]
'''


res = [list(binary_tree[0])]
for i in range(int(len(binary_tree)) // 2 ):
    x = []
    for n in range(len(binary_tree[i + 1])):
        if n == 0:
            x.append(binary_tree[i + 1][n] + res[i][0])
        elif n == len(binary_tree[i + 1]) - 1:
            x.append(binary_tree[i + 1][n] + res[i][-1])
        else:
            if res[i][n - 1] < res[i][n]:
                x.append(binary_tree[i + 1][n] + res[i][n - 1])
            if res[i][n - 1] > res[i][n]:
                x.append(binary_tree[i + 1][n] + res[i][n])
    res.append(x)

for i in range(int(len(binary_tree)) // 2, len(binary_tree) -1):
    x = []
    for n in range(len(binary_tree[i + 1])):

        if n == 0 and len(binary_tree[i + 1]) != 1:
            x.append(binary_tree[i + 1][n] + res[i][0])
        elif n == len(binary_tree[i + 1]) - 1 and n != 1 and n != 0:
            x.append(binary_tree[i + 1][n] + res[i][-1])
        else:
            if res[i][n] < res[i][n + 1]:
                x.append(binary_tree[i + 1][n] + res[i][n])
            if res[i][n] > res[i][n + 1]:
                x.append(binary_tree[i + 1][n] + res[i][n + 1])
    res.append(x)






print('Answer:', res[-1][0])
