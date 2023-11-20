from sys import stdin
from collections import defaultdict, deque
n = int(stdin.readline())
source_code = defaultdict(lambda: set())
for _ in range(n):
    dependent_file, impacted_files = stdin.readline().split(':')
    if impacted_files:
        for file in impacted_files.split():
            source_code[file].add(dependent_file)
changed_file = stdin.readline().strip()
pq = deque([changed_file])
visited = defaultdict(lambda: False)
dependency_matrix = defaultdict(lambda: -1)
dependency_matrix[changed_file] = 0

# BFS for counting degrees of each vertice
while pq:
    file = pq.popleft()
    for dependent_file in source_code[file]:
        if not visited[dependent_file]:
            pq.append(dependent_file)
            visited[dependent_file] = True
        dependency_matrix[dependent_file] = dependency_matrix[dependent_file] + 1 if dependency_matrix[dependent_file] != -1 else 1
pq = deque([changed_file])

# toposort
while pq:
    file = pq.popleft()
    print(file)
    for dependent_file in source_code[file]:
        if dependency_matrix[dependent_file] > 0:
            dependency_matrix[dependent_file] -= 1
            if dependency_matrix[dependent_file] == 0:
                pq.append(dependent_file)
