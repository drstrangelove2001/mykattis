import sys
from collections import defaultdict
N = int(sys.stdin.readline())
code = defaultdict(lambda: list())
variables = defaultdict(lambda: 0)
code_at_level = defaultdict(lambda: list())
level = 0
for _ in range(N):
    line = sys.stdin.readline().split()
    if line[0] == 'DECLARE':
        var,typ = line[1],line[2]
        variables[var] = typ
        if code[var]:
            if code[var][-1][2] == level:
                print('MULTIPLE DECLARATION')
                break
        code[var].append((var,typ,level))
        code_at_level[level].append(var)
    elif line[0] == 'TYPEOF':
        var = line[1]
        print(variables[var] if variables[var] else 'UNDECLARED')
    elif line[0] == '{':
        level += 1
    elif line[0] == '}':
        for var in code_at_level[level]:
            code[var].pop()
            if code[var]:
                variables[var] = code[var][-1][1]
            else:
                variables[var] = 0
        code_at_level[level] = []
        level -= 1