import sys
input = sys.stdin.readline

n, k = map(int, input().split())

arr = [i for i in range(2, n+1)]

answer = 0

while arr:
    min_num = min(arr)
    for n in arr:
        if (n % min_num == 0):
            arr.remove(n)
            answer += 1
            if (answer == k):
                print(n)