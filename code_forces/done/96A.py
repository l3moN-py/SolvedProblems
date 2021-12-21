team = input()

if len(max(team.split('0'))) >= 7 or len(max(team.split('1'))) >= 7:
    print('YES')
else:
    print('NO')


# NOTE: mozno cez regex tiez ?