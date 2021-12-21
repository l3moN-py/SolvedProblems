n = int(input())
strength = sorted([int(input()) for a in range(n)])
d = 0
for i in range(len(strength)-1):
    if strength[i+1]-strength[i] < d or strength[i] == strength[0]:
        d = strength[i+1]-strength[i]
print(d)
