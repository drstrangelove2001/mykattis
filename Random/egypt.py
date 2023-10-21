while True:
    a,b,c = sorted(list(map(int, input().split())))
    if not any((a,b,c)):
        break
    if a**2+b**2==c**2:
        print('right')
    else:
        print('wrong')
