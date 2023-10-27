n = int(input())
A = []
err = False
for i in range(n):
    line = input().split()
    if len(line) == 2:
        A.append(line[1])
    else:
        for assumption in line[:-2]:
            if assumption not in A:
                err = True
                print(i+1)
                break
if not err:
    print('correct')