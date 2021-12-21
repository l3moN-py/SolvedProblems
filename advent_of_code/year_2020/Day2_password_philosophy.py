import re

with open(r"Python\Advent of Code\2020\day2input") as f:
    passwords = f.readlines()

#first star
def foo(passwords, i = 0):
    for password in passwords:
        pattern = '(\d+)-(\d+)\s(\w):\s(\w+)'
        text = password.strip()
        match = re.search(pattern, text)
        m, n, l, s = match.groups()
        m, n = map(int, [m,n])

        if s.count(l) in range(m, n+1):
            i += 1
    return i
print("Num of valid passwords:", foo(passwords))

#second star
def doo(passwords, i = 0):
    for password in passwords:
        pattern = '(\d+)-(\d+)\s(\w):\s(\w+)'
        text = password.strip()
        match = re.search(pattern, text)
        m, n, l, s = match.groups()
        m, n = map(int, [m,n])

        if ((s[m-1] == l) or (s[n-1] == l)) and (s[n-1] != s[m-1]):
            i += 1
    return i
print("Num of valid passwords (second star):", doo(passwords))