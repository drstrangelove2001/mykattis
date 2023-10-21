n = int(input())
A = [int(input()) for _ in range(n)]
[print(f'{item} is even' if abs(item)%2 == 0 else f'{item} is odd') for item in A]