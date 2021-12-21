n, h = map(int, input().split())
heights = list(map(int, input().split()))

lower = len(list(filter(lambda x: x <= h, heights)))
upper = (n-lower)*2

print(lower + upper)
