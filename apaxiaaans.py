name = input()
ans = ''
for index,char in enumerate(name):
    if index==0 or char != name[index-1]:
        ans += char
print(ans)