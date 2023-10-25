seq = input()
print(chr((sum([ord(ch) for ch in seq])//len(seq))))