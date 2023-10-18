n = int(input())
seq = input()
lst = []
openl = ['(', '{', '[']
closel = [')', '}', ']']
err = False
for i in range(n):
    char = seq[i]
    if char in openl:
        lst.append(char)
    else:
        ind = closel.index(char)
        if lst and openl[ind] == lst[-1]:
            lst.pop()
        else:
            err = True
if lst:
    err = True
print('Invalid' if err else 'Valid')