from collections import deque


def solution(maps):
    # 왼오아래위
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    r = len(maps)
    c = len(maps[0])

    # 도달할 수 없으면 -1
    graph = [[-1 for _ in range(c)] for _ in range(r)]

    q = deque()
    q.append([0, 0])
    graph[0][0] = 1

    while q:
        y, x = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= ny < r and 0 <= nx < c and maps[ny][nx] == 1:
                if graph[ny][nx] == -1:
                    graph[ny][nx] = graph[y][x] + 1
                    q.append([ny, nx])

    answer = graph[-1][-1]
    return answer