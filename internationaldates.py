date = input()
day, month, year = date.split("/")
if int(month)>12:
    print("US")
elif int(day)>12:
    print("EU")
else:
    print("either")