D,M = map(int,input().split())
days = ['Thursday', 'Friday', 'Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday']
months = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
d = 0
for i in range(1,M):
    d += months[i]
d += D
print(days[(d-1)%7])