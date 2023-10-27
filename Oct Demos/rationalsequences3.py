from math import log2, floor
for i in range(int(input())):
    K,N = map(int, input().split())
    binary_equivalent = bin(N)[-floor(log2(N)):]
    num,den = 1,1
    if N!=1:
        for dig in binary_equivalent:
            if dig == '0':
                den += num
            else:
                num += den
    print(K,f'{num}/{den}')
