magnets = ''.join([input() for _ in range(int(input()))])

print(magnets.count('00') + magnets.count('11') + 1)