N = int(input())
A = [input() for _ in range(N)]
for instruction in A:
    if instruction.startswith('Simon says'):
        print(instruction[len('Simon says '):])