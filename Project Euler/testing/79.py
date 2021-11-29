f = open(r'C:\Users\Klacik\Desktop\Python\Project Euler\Text\p079_keylog.txt')
x = []
for num in f.readlines():
    if int(num) not in x:
        x.append(int(num))

#print(sorted([int(line) for line in f.readlines()]))
print(x)
