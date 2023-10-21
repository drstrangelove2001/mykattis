from math import sqrt
a,b,c = [ tuple(map(int, input().split())) for _ in range(3) ]

def distance(A,B):
    return sqrt((A[0] - B[0])**2 + (A[1] - B[1])**2)

def midpoint(A,B):
    if (A[0]+B[0]) % 2 == 0:
        x = (A[0]+B[0])//2
    else:
        x = (A[0]+B[0])/2
    
    if (A[1]+B[1]) % 2 == 0:
        y = (A[1]+B[1])//2
    else:
        y = (A[1]+B[1])/2
    return (x,y)

sq = {(a,b):c, (b,c):a, (a,c):b}
ddict = { (a,b): distance(a,b), (b,c): distance(b,c), (a,c): distance(a,c) }
diag = max(ddict.values())
diag_vertex = tuple()
for key in ddict:
    if ddict[key] == diag:
        diag_vertex = key

side_vertex = sq[diag_vertex]

mdpt = midpoint(diag_vertex[0], diag_vertex[1])
ansx,ansy = int(2*mdpt[0]-side_vertex[0]), int(2*mdpt[1]-side_vertex[1])
print(ansx,ansy)



