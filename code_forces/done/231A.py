sol = 0
for test in range(int(input())):
    if sum(list(map(int, input().split()))) >= 2:
        sol += 1

print(sol)