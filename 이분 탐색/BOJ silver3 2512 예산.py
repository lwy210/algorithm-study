import sys
input = sys.stdin.readline

n = int(input())
requests = list(map(int, input().split()))
m = int(input())

start = 0
end = max(requests)

while start <= end:
    mid = (start + end) // 2
    current = 0

    for request in requests:
        if request >= mid:
            current += mid
        else:
            current += request

    if current <= m: # 예산 이하
        start = mid + 1
    else:
        end = mid - 1

print(end)
