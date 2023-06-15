import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int,input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int,input().split())))

dx = [1,-1,0,0]
dy = [0,0,1,-1]

cnt = 0 # 처음 빈칸의 개수
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            cnt += 1

max_result = 0 # 안전 영역의 최대 크기

def virus():
    visited = [[0] * m for _ in range(n)]
    global max_result
    result = 0 # 해당 경우의 수에서의 바이러스 수
    q = deque()

    """바이러스를 퍼뜨리기 위해서 
       바이러스 있는곳을 방문처리하고 큐에 올린다"""
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                visited[i][j] = 1
                q.append((i, j))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny]==0:
                if graph[nx][ny] == 0:
                    visited[nx][ny] = 1
                    result += 1
                    q.append((nx, ny))

    max_result = max(max_result, cnt-result) # 기존 안전영역 - 바이러스의 수 = 해당 경우의 안전영역

"""
이부분이 헷갈림 ㅠ 생각하면서 보자 dfs는 항상 너무 어렵당
"""
def wall_dfs(cnt):
    if cnt == 3:
        virus()
        return
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                wall_dfs(cnt+1)
                graph[i][j] = 0
wall_dfs(0)
print(max_result-3)