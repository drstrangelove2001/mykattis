n = int(input())
listofwords = []
for i in range(int(n)):
    listofwords.append(input())
newlistofwords = []
for i in range(len(listofwords)):
    chars = list(listofwords[i])
    flag = False
    for ch in chars:
        temp = []
        temp[:] = chars
        temp.remove(ch)
        if ch in temp:
            flag = True
            break
    if flag == False:
        newlistofwords.append(listofwords[i])
    
if len(newlistofwords) == 0:
    print('neibb!')
else:
    best =  ''
    for entry in newlistofwords:
        if len(entry) >= 5:
            if best == '':
                best = entry
            else:
                if len(entry) < len(best):
                    best = entry
                elif len(entry) == len(best):
                    if entry > best:
                        best = entry
    if best == '':
        print('neibb!')
    else:
        print(best)
