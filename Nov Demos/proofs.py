import sys
from collections import defaultdict
n = int(sys.stdin.readline())
err = False
axioms = defaultdict(lambda:False)
for i in range(n):
    line = sys.stdin.readline().split()
    if line[0] == '->':
        axioms[line[1]] = True
    else:
        j = 0
        while line[j] != '->':
            if not axioms[line[j]]:
                err = True
                print(i+1)
                break
            j += 1
        axioms[line[-1]] = True
    if err:
        break
if not err:
    print('correct')