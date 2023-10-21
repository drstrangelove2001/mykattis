x = input()
lst = [int(i) for i in x.split()]
if sum(lst[:-1]) == lst[-1]:
    print("correct!")
else:
    print("wrong!")