s = input()
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
count = 0
for ch in s:
    if ch in vowels:
        count+=1
print(count)