from collections import deque
Q = int(input())
for _ in range(Q):
    seq = input()
    n = int(input())
    inp = input()
    nums = inp.strip('[]')
    lst = [int(x) for x in nums.split(',') if x]
    arr = deque(lst)
    fwd = True
    for move in seq:
        if move == 'D' and not arr:
            break
        elif move == 'D':
            if fwd:
                arr.popleft()
            else:
                arr.pop()
        elif move == 'R':
            fwd = not fwd
    if not fwd and arr:
        arr.reverse()
    print(str(list(arr)).replace(' ','') if arr else 'error')