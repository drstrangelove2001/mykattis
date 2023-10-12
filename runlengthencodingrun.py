algo,msg = input().split()
ans = ''
if algo == 'E':
    count = 0
    rep = msg[0]
    for index,char in enumerate(msg):
        if index == 0 or char == msg[index-1]:
            count += 1
        elif char != msg[index-1]:
            ans += rep + str(count)
            count = 1
        rep = char
    ans += rep + str(count)
else:
    for index in range(0,len(msg),2):
        ans += ''.join([msg[index] for _ in range(int(msg[index+1]))])
print(ans)