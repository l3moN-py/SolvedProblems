matrix = ''.join([input().replace(' ', '') for _ in range(5)])
ind = matrix.index('1')

x = ind // 5
y = ind % 5

print(abs(2-x) + abs(2-y))
