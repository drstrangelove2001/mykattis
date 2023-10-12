dup = set()
ans = []
while True:
    line = input().split()
    if line:
        for word in line:
            if word.lower() in dup:
                ans.append('.')
            else:
                ans.append(word)
                dup.add(word.lower())
    else:
        break
print(' '.join(ans))