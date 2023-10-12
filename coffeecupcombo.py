n = int(input())
lectures = input()
coffees = 0
fresh_lectures = 0
for lec in lectures:
    if lec == '1' and coffees == 0:
        fresh_lectures += 1
        coffees += 2
    elif lec == '0' and coffees > 0:
        fresh_lectures += 1
        coffees = coffees - 1
    elif lec == '1' and coffees > 0:
        fresh_lectures += 1
        coffees = 2
print(fresh_lectures)
