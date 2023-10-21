N = int(input())
cards = sorted(list(map(int, input().split())))
Q = int(input())

def searchForL(i,j,l):
    while i<=j:
        mdpt = (i+j)//2
        if cards[mdpt] == l:
            j = mdpt - 1
        elif cards[mdpt] > l:
            j = mdpt - 1
        else:
            i = mdpt + 1
    return j

def searchForR(i,j,r):
    while i<=j:
        mdpt = (i+j)//2
        if cards[mdpt] == r:
            i = mdpt + 1
        elif cards[mdpt] > r:
            j = mdpt - 1
        else:   
            i = mdpt + 1
    return i

for _ in range(Q):
    l,r = map(int, input().split())
    indl = searchForL(0,N-1,l)
    indr = searchForR(0,N-1,r)
    print(indr-indl-1)
        