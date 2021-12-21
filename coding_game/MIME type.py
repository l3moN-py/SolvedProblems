import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.
file_type = [a.split() for a in [input() for _ in range(n)]]
tested_files = [input() for _ in range(q)]
dc = {}
for i in file_type:
    dc.update({i[0].lower():i[1]})
file_set = {a[0].lower() for a in file_type}

for t_file in tested_files:
    if '.' not in t_file:
        print('UNKNOWN')
    else:
        if t_file[-t_file[::-1].index('.'):].lower() not in file_set:
            print('UNKNOWN')
        else:
            print(dc.get(t_file[-t_file[::-1].index('.'):].lower()))
