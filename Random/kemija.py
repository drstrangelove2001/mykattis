sentence = input()
wrongs = ['apa', 'epe', 'ipi', 'opo', 'upu']
rights = ['a', 'e', 'i', 'o', 'u']
for i in range(5):
    sentence = sentence.replace(wrongs[i],rights[i])
print(sentence)