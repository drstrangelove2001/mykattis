import sys

A = []
completed = 0
for line in sys.stdin:
    if line.strip():
        st = line.count('*')
        A.append('.'*(len(line)-st-completed-1) + '*'*st + '.'*completed)
        completed += st
    else:
        A.append('')
        completed = 0

[print(item) for item in A]