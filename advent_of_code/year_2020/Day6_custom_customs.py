from functools import reduce

with open(r'Python\Advent of Code\2020\day6input') as f: 
    answers = ''.join([line if line != '\n' else '|' for line in f.readlines()]).split('|')

#first star
def foo(answers, s=0):
    return sum([len(set(answer.replace('\n', ''))) for answer in answers])

print('Sum of "YES" answers (first star):', foo(answers))

#second star
def doo(answers, s=0):
    for answer in answers:
        answer = [set(a) for a in answer.split('\n') if a != '']
        yes_answers = reduce((lambda x,y : x & y),answer)
        if yes_answers:
            s += len(yes_answers)
    return s

print('Sum of "YES" answers (second star):', doo(answers))