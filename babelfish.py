dictionary = dict()
while True:
    try:
        value, key = input().split()
    except:
        break
    else:
        dictionary[key] = value
while True:
    try:
        word = input()
    except:
        break
    else:
        if word in dictionary:
            print(dictionary[word])
        else:
            print('eh')

