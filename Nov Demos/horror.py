import sys
from collections import defaultdict
N,H,L = map(int, sys.stdin.readline().split())
horror_list = list(map(int, sys.stdin.readline().split()))
movie_AL = defaultdict(lambda: list())
for _ in range(L):
    a,b = map(int, sys.stdin.readline().split())
    movie_AL[a].append(b)
    movie_AL[b].append(a)
horror_index = defaultdict(lambda: 10**6)
for movie in horror_list:
    horror_index[movie] = 0
while horror_list:
    tmp = horror_list
    horror_list = []
    for movie in tmp:
        for similar_movie in movie_AL[movie]:
            if similar_movie not in horror_index:
                horror_index[similar_movie] = horror_index[movie] + 1
                horror_list.append(similar_movie)
max_horror = 0
max_movie = 0
for i in range(N):
    if horror_index[i] > max_horror:
        max_horror = horror_index[i]
        max_movie = i
print(max_movie)