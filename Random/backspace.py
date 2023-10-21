from collections import deque
a = deque()
for char in input():
    if char == '<':
        a.pop()
    else:
        a.append(char)
print(''.join(list(a)))