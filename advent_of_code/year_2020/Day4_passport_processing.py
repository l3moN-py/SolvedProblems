import re

with open(r'Python\Advent of Code\2020\day4input') as f:
    data = f.readlines()

required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
data = ' '.join(data).split(' \n ')

#first star
def foo(data, s = 0):
    for i in range(len(data)):
        for req in required:
            if req not in data[i]:
                break
            elif req == required[-1]:
                s += 1
    return s

print('Valid passports:', foo(data))

#second star
def is_valid(s):
    if not bool(re.search(r'byr:(19[2-9][0-9])|(200[0-2])\b',s)):
        return False
    elif not bool(re.search(r'iyr:20(1[0-9]|20)\b',s)):
        return False
    elif not bool(re.search(r'eyr:20(2[0-9]|30)\b',s)):
        return False
    elif not (bool(re.search(r'hgt:1([5-8][0-9]|9[0-3])cm\b',s)) or bool(re.search(r'hgt:(59|6[0-9]|7[0-6])in\b',s))):
        return False
    elif not bool(re.search(r'hcl:#[\da-f]{6}\b',s)):
        return False
    elif not bool(re.search(r'ecl:(amb|blu|brn|gry|grn|hzl|oth)\b',s)):
        return False
    elif not bool(re.search(r'pid:[0-9]{9}\b',s)):
        return False
    return True
def has_req(s):
    for r in required:
        if r not in s:
            return False
    return True
    
def doo(data, s = 0):
    for d in data:
        if is_valid(d) and has_req(d):
            s += 1
    return s

print('Valid passports (second star):', doo(data))
