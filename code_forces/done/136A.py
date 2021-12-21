n = int(input())
presents = list(map(int, input().split()))
result = [0 for _ in range(n)]
# print(list(enumerate(presents,1)))

for person in enumerate(presents,1):
    ind, rec= person
    result[rec-1] = ind

print(*result)
