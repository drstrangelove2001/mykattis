A = list(map(int, input().split()))
first, second = A[1] - A[0], A[2] - A[1]
if first == second:
    print('cruised')
elif first*second < 0:
    print('turned')
elif first*second > 0 and abs(second) > abs(first):
    print('accelerated')
else:
    print('braked')