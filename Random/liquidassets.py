#one test case not passing

n = int(input())
S = input().split()
vowels = ['a', 'e', 'i', 'o', 'u']
ans = []
for word in S:
    new_word = ''
    for i, char in enumerate(word):
        if char in vowels:
            if i==0 or i==len(word)-1 and len(word)!=2:
                new_word += char
        else:
            if i==0:
                new_word += char
            elif char != word[i-1]:
                new_word += char
    ans.append(new_word)
print(' '.join(ans))