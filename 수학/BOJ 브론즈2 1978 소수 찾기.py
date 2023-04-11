import sys
input = sys.stdin.readline

def is_prime(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num%i == 0:
            return False
    return True

n = int(input())
arr = list(map(int, input().split()))

answer = 0
for num in arr:
    if is_prime(num):
        answer += 1

print(answer)