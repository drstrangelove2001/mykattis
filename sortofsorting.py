while True:
    n = int(input())
    if n==0:
        break
    lst = [input() for _ in range(n)]
    lst.sort(key=lambda name:name[1])
    lst.sort(key=lambda name:name[0])
    [print(name) for name in lst]