while True:
    n = int(input())
    if n==0:
        break
    lst = [input() for _ in range(n)]
    lst.sort(key=lambda name:name[0] + name[1])
    [print(name) for name in lst]