last = ''
count = 0

r = int(input())
text = input()

for i in range(r):
    if last == text[i]:
        count += 1
    else:
        last = text[i]

print(count)