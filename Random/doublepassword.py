pwd1 = input()
pwd2 = input()
ans = 1
for i in range(4):
    ans *= 1 if pwd1[i] == pwd2[i] else 2
print(ans)