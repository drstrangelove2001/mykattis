inp = input()
w = int(input())
s,m,l = [int(i) for i in inp.split()]
n = 0
ddict = {}
def shelves(s,m,l,filled):
    if s==m==l==0:
        return int(filled>0)
    t = (s,m,l,filled)
    if t in ddict:
        return ddict[t]
    n = 10**7
    if s:
        if filled <= w-1:
            n = min(n, shelves(s-1,m,l,filled+1))
        else:
            n = min(n, 1 + shelves(s-1,m,l,1))
    if m:
        if filled <= w-2:
            n = min(n, shelves(s,m-1,l,filled+2))
        else:
            n = min(n, 1 + shelves(s,m-1,l,2))
    if l:
        if filled <= w-3:
            n = min(n, shelves(s,m,l-1,filled+3))
        else:
            n = min(n, 1 + shelves(s,m,l-1,3))
    ddict[t] = n
    return n
print(shelves(s,m,l,0))
