from collections import deque

n = int(input())
truth_values = {'T': True, 'F': False}
values = input().split()
inp = 'A'
mapping = dict()
for val in values:
    mapping[inp] = truth_values[val]
    inp = chr(ord(inp) + 1)
seq = input().split()
ops = ['*', '+', '-']
A = deque()
for entry in seq:
    if entry not in ops:
        A.appendleft(mapping[entry])
    else:
        if entry == '*':
            i = A.popleft()
            j = A.popleft()
            A.appendleft(i and j)
        elif entry == '+':
            i = A.popleft()
            j = A.popleft()
            A.appendleft(i or j)
        else:
            i = A.popleft()
            A.appendleft(not i)
print('T' if A.pop() else 'F')