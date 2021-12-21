import re

word = input()

if re.match(r'.*h.*e.*l.*l.*o', word):
    print('YES')
else:
    print('NO')