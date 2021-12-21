n = int(input())
feelings = ''

i = 1
for i in range(n-1):
    if i%2 != 1:
        feelings += 'I hate that '
    else:
        feelings += 'I love that '
else:
    if i%2 == 1:
        feelings += 'I hate it'
    else:
        feelings += 'I love it'

print(feelings)