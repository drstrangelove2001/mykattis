Q = int(input())
for _ in range(Q):
    N = int(input())
    A,B,C = map(int, input().split())
    X,Y = map(int, input().split())
    def hashValue(R):
        V = 0
        for i in range(0,N):
            V = (V*X + R[i]) % Y
        return V
    def magicSeq(n):
        lst = [A]
        for i in range(1,n):
            lst.append((lst[i-1]*B+A)%C)
        return sorted(lst)
    S = magicSeq(N)
    print(hashValue(S))