#random results
from random import randint
A,B = map(int, input().split())
arr = set()
size = randint(A,B)
while len(arr) != size:
    word = ''
    length = randint(1,15)
    while len(word) != length:
        char = chr(randint(97,122))
        word += char
    arr.add(word)
print(' '.join(arr))