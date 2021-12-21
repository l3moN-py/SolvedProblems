n = input()
opinions = list(map(int, input().split()))

if any(opinions):
    print('HARD')
else:
    print('EASY')
