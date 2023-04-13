import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
q = deque([])

for _ in range(n):
    command = input().split()
    if command[0] == 'push':
        q.append(command[1])
    elif command[0] == 'pop':
        print(-1 if len(q)==0 else q.popleft())
    elif command[0] == 'size':
        print(len(q))
    elif command[0] == 'empty':
        print(1 if len(q)==0 else 0)
    elif command[0] == 'front':
        print(-1 if len(q)==0 else q[0])
    elif command[0] == 'back':
        print(-1 if len(q) == 0 else q[-1])