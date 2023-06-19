# https://www.acmicpc.net/problem/4963

"""


"""

import sys
from collections import deque
input = sys.stdin.readline

# 상하좌우 대각선
dx = [0, 0, -1, 1, -1, -1, 1, 1]
dy = [1, -1, 0, 0, 1, -1, 1, -1]

def bfs(graph, x, y):
    q = deque()
    q.append((x, y))
    graph[y][x] = 0

    while q:
        a, b = q.popleft()

        for i in range(8):
            nx = a + dx[i]
            ny = b + dy[i]

            if 0 <= nx < w and 0 <= ny < h:
                if graph[ny][nx] == 1:
                    graph[ny][nx] = 0
                    q.append((nx, ny))


while True:
    w, h = map(int, input().split())  # w : 너비, h : 높이

    if w == 0 and h == 0:
        break

    graph = []
    for _ in range(h):
        graph.append(list(map(int, input().split(' '))))

    answer = 0
    for i in range(w):
        for j in range(h):
            if graph[j][i] == 1:
                answer += 1
                bfs(graph, i, j)

    print(answer)