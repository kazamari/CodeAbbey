from sys import stdin
from collections import deque, defaultdict

def bfs(graph, start):
    q, seen = deque([start]), {start: -1}
    while q:
        v = q.popleft()
        for w in sorted(graph[v]):
            if w not in seen:
                q.append(w)
                seen[w] = v
    return seen.values()


