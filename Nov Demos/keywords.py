import sys
n = int(sys.stdin.readline())
keys = set()
for _ in range(n):
    word = sys.stdin.readline()
    word = word.replace('-', ' ').lower()
    keys.add(word)
print(len(keys))