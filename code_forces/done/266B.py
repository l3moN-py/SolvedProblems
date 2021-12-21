import re
l, p = map(int, input().split())
pos = input()

for _ in range(p):
    for iter in re.finditer(r'BG',pos):
        x,y = iter.span()
        pos = pos[:x] + pos[y-1] + pos[x] + pos[y:]

print(pos)
