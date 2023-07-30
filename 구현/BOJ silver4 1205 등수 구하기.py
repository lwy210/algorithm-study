import sys
input = sys.stdin.readline

n, new_score, p = map(int, input().split())

if n:
    arr = list(map(int, input().split()))
    arr.append(new_score)
    arr.sort(reverse=True)
    index = arr.index(new_score) + 1
    if index > p:
        print(-1)
    else:
        if n==p and new_score == arr[-1]:
            print(-1)
        else:
            print(index)
else:
    print(1)
