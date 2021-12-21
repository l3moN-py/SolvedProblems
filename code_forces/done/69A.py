vectors = [list(map(int, input().split())) for _ in range(int(input()))]

#print(vectors)
if [sum(item) for item in list(zip(*vectors))] == [0,0,0]:
    print('YES')
else:
    print('NO')