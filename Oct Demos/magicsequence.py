# Kattis score: 79/100, using counting sort.

Q = int(input())
for _ in range(Q):
    N = int(input())
    A,B,C = map(int, input().split())
    X,Y = map(int, input().split())
    def hashValue(max_val, count_lst):
        V = 0
        for i in range(0,max_val+1):
            while count_lst[i] != 0:
                V = (V*X + i) % Y
                count_lst[i] -= 1
        return V
    def magicSeq(n):
        max_val = val = A
        count_lst = [0]*10**6
        count_lst[A] = 1
        for _ in range(1,n):
            val = (val*B+A)%C
            max_val = max(val, max_val)
            count_lst[val] += 1
        print(hashValue(max_val, count_lst))
    magicSeq(N)