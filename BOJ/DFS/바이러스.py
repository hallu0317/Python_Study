import sys

n1 = int(sys.stdin.readline())
n2 = int(sys.stdin.readline())
graph = [[]for i in range(n1+1)]
visited = [0]*(n1+1)

for i in range(n2):
    a,b=map(int,sys.stdin.readline().split())
    graph[a] += [b]
    graph[b] += [a]

def dfs(n2):
    visited[n2] = 1
    for nx in graph[n2]:
        if visited[nx]==0:
            dfs(nx)

dfs(1)
print(sum(visited)-1)