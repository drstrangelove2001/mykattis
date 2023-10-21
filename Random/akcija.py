N = int(input())
A = sorted([int(input()) for _ in range(N)], reverse=True)
print(sum([A[i] for i in range(N) if (i+1)%3 != 0]))
