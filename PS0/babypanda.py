inp = input()
n,m = [int(i) for i in inp.split()]
days = ''
while m > 0:
    rem = m%2
    days += str(rem)
    m = m//2
sneezes = len(list(filter(lambda x:x=='1', list(days))))
print(sneezes)