x = int(input())
ans = 1
while x>0:
    rem = x%10
    x = x//10
    if rem>0:
        ans = ans*rem
    if x==0 and ans>9:
        x = ans
        ans = 1
print(ans)