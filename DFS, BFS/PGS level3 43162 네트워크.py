from collections import deque

def solution(n, computers):
    def bfs(idx):
        q = deque()
        q.append(idx)

        while q:
            x = q.popleft()
            visited[x] = True
            for nx in range(n):
                if computers[x][nx] and not visited[nx]:
                    q.append(nx)

    answer = 0
    visited = [False for i in range(n)]
    for i in range(n):
        if not visited[i]:
            bfs(i)
            answer += 1

    return answer