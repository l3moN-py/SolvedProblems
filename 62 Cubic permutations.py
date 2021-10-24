# link - https://www.xarg.org/puzzle/project-euler/problem-62/

from collections import Counter

nums = {i for i in range(1, 10_000)}
cubic_nums = [i**3 for i in nums]
sorted_cubic_nums = [''.join(sorted(str(i))) for i in cubic_nums]
picked_cubic_nums = [num[0] for num in Counter(sorted_cubic_nums).most_common(2)]


results = [num for num in cubic_nums if ''.join(sorted(str(num))) in picked_cubic_nums]
print('Result:',min(results))