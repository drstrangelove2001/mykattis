t = int(input())
lst = []
for _ in range(t):
    x = input()
    y = input()
    lst.append((int(x.replace(" ","")),int(y.replace(" ",""))))
for item in lst:
    total = sum(item)
    print(' '.join(map(str, str(total))))