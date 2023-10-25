import heapq
n,m,k = map(int, input().split())
pile = [('Jane Eyre', k)]
time = 0
future_pile = []
for _ in range(n):
    unread_book, unread_book_pages = input().split('"')[1:]
    entry = (unread_book, int(unread_book_pages))
    heapq.heappush(pile, entry)
for _ in range(m):
    minute, book, book_pages = input().split('"')
    entry = (int(minute), book, int(book_pages))
    heapq.heappush(future_pile, entry)
read = heapq.heappop(pile)
while True:
    time += read[1]
    while future_pile and time >= future_pile[0][0]:
        heapq.heappush(pile, (heapq.heappop(future_pile)[1:]))
    if read[0] == 'Jane Eyre':
        print(time)
        break
    else:
        read = heapq.heappop(pile)
