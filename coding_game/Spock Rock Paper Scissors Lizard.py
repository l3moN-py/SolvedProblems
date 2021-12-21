def repeat(n):
    c = 0
    while n != 1:
        n = n//2
        c += 1
    return c

n = 8
n = int(input())

games = [[input() for _ in range(n)]]

for _ in range(repeat(n)):
    x = []

    for i in range(0, len(games[-1]),2):
        if games[-1][i][-1] == games[-1][i+1][-1]:
            if int(games[-1][i][:-2]) < int(games[-1][i+1][:-2]):
                x.append(games[-1][i])
            else:
                x.append(games[-1][i+1])
        elif games[-1][i][-1] == 'R':
            if games[-1][i+1][-1] in ['L', 'C']:
                x.append(games[-1][i])
            else:
                x.append(games[-1][i+1])
        elif games[-1][i][-1] == 'L':
            if games[-1][i+1][-1] in ['P', 'S']:
                x.append(games[-1][i])
            else:
                x.append(games[-1][i+1])
        elif games[-1][i][-1] == 'S':
            if games[-1][i+1][-1] in ['C', 'R']:
                x.append(games[-1][i])
            else:
                x.append(games[-1][i+1])
        elif games[-1][i][-1] == 'C':
            if games[-1][i+1][-1] in ['P', 'L']:
                x.append(games[-1][i])
            else:
                x.append(games[-1][i+1])
        elif games[-1][i][-1] == 'P':
            if games[-1][i+1][-1] in ['R', 'S']:
                x.append(games[-1][i])
            else:
                x.append(games[-1][i+1])
    games.append(x)


print(games[-1][0][:-2])
print(' '.join([a[a.index(''.join(games[-1]))-1][:-2] if a.index(''.join(games[-1]))%2 != 0 else a[a.index(''.join(games[-1]))+1][:-2] for a in games[:-1]]))
