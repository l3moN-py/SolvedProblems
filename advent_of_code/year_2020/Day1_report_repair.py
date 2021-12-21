with open(r"Python\Advent of Code\2020\day1input") as f:
    report = f.readlines()

report = set([int(r.strip()) for r in report])

#first star
def foo(report, year):  
    for r in report:
        if year-r in report:
            return (year-r)*r 
    return False

print("First star:", foo(report, 2020))

#second star
def doo(report):
     for r in report:
        result = foo(report-{r}, 2020-r)
        if result:
            return r*result

print("Second star:", doo(report)) 