n = int(input())
printers = 1
days = 1
while printers*2 <= n:
    printers = printers*2
    days += 1
if printers < n:
    days += 1
print(days)