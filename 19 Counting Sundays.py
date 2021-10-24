year = {
'Jan' : 31,
'Feb' : 28,
'Mar' : 31,
'Apr' : 30,
'May' : 31,
'Jun' : 30,
'Jul' : 31,
'Aug' : 31,
'Sep' : 30,
'Oct' : 31,
'Nov' : 30,
'Dec' : 31

}

y = []

for i in range(1901,2001):
    if i in [a for a in range(1901,2001) if a%4 == 0]:
        year.update({'Feb' : 29})
        y += list(year.values())
        year.update({'Feb' : 28})
    else:
        y += list(year.values())

a,b = 2,0
count = 0
for num in y:
    b,a = divmod(num + a, 7)
    if a == 0:
        count += 1

print(y)
print(count)
