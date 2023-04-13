import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    stack = list(input().rstrip())
    count = 0
    for x in stack:
        if x=='(':
            count += 1
        elif x==')':
            count -= 1
        if count < 0:
            print('NO')
            break

    if count > 0:
        print('NO')
    elif count == 0:
        print('YES')
