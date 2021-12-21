num_games = int(input())
games = input()

Anton = games.count('A')
Danik = games.count('D')

if Anton > Danik:
    print('Anton')
elif Danik > Anton:
    print('Danik')
else:
    print('Friendship')