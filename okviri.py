peterpan = [['.', '.', '#', '.', '.'], ['.', '#', '.', '#', '.'], ['#', '.', 'char', '.', '#'], ['.', '#', '.', '#', '.'], ['.', '.', '#', '.', '.']]
wendy = [['.', '.', '*', '.', '.'], ['.', '*','.','*', '.'], ['*', '.', 'char', '.', '*'], ['.', '*','.','*', '.'], ['.', '.', '*', '.', '.']]
ans = ''
def prettyprint(A,x):
    ret = ''
    for i in range(len(A)):
         ret += ''.join(A[i][0:x])
    return ret

word = input()
for index,char in enumerate(word):
    if (index+1)%3 == 0:
        wendy[2][2] = char
        ans += prettyprint(wendy,None)
    else:
        peterpan[2][2] = char
        ans += prettyprint(peterpan,-1 if index < len(word) - 1 else None)
print(ans)
