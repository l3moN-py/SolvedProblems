import re
from pprint import *

with open(r'Python\Advent of Code\2020\day7input') as f:
    data = f.read().split('.')

#first star
def doo(bags={}, s=0):
    for d in data[:-1]:
        pattern = r'(\w+\s\w+) bags?'
        match = re.findall(pattern, d)
        bags[match[0]] = match[1:]
    return sum([1 for bag in bags if foo(bag, bags)])

def foo(bag, bags, mine_bag='shiny gold'):
    if 'no other' == bag:
        return False
    if mine_bag in bags[bag]:
        return True
    else:
        for bag in bags[bag]:
            if foo(bag, bags):
                return True
    return False

#print('1.) Possible bags for shiny bag:', doo())
            
#second star
def zoo(bags={}):
    for d in data[:-1]:
        pattern = r'(\d\s)?(\w+\s\w+) bags?'
        match = re.findall(pattern, d)
        #return match
        bags[match[0][1]] = match[1:]
    
    return bags
#print(zoo())
bags=zoo()
def goo(bag, s=0):
    if 'no other' in bags[bag]:
        return 0 
    # for n,b in bags[bag]:
    #    s += n + goo(b)   

    return sum([0 if 'no other' == b else (int(n) + int(n)*goo(b)) for n,b in bags[bag]])
       #print(s)
    #return s  

print(goo('shiny gold'))










