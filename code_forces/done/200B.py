n = int(input())
drinks = sum(map(int, input().split()))

print('{:.10f}'.format(drinks/n))