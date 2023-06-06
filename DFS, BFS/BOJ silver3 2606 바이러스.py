# https://www.acmicpc.net/problem/2606

import sys
from collections import deque
input = sys.stdin.readline

n = int(input()) # 컴퓨터의 수
m = int(input()) # 네트워크 수

arr = [[] for _ in range(n+1)] # 양방향 네트워크를 저장할 배열

for i in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

visited = [False for _ in range(n+1)]

q = deque([1])
visited[1] = True
answer = -1

while q:
    x = q.popleft()
    answer += 1

    for nx in arr[x]:
        if not visited[nx]:
            visited[nx] = 1
            q.append(nx)

print(answer)