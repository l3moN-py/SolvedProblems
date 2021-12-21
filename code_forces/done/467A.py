n = int(input())
rooms = [tuple(map(int, input().split())) for room in range(n)]

print(len(list(filter(lambda x: x[1]-x[0] >= 2, rooms))))