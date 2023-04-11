import sys
input = sys.stdin.readline

#  입력 받기
n = int(input())
arr = set(list(map(int, input().split())))

# 에라토스테네스의 체 : 소수 구하기
is_prime = [False, False] + [True] * (1000000-1)

for i in range(2, len(is_prime)):
    if is_prime[i]:
        for j in range(2*i, len(is_prime), i):
            is_prime[j] = False


# 소수들의 최소공배수 출력하기
answer = 1
for num in arr:
    if is_prime[num]:
        answer *= num
if answer == 1:
    answer *= -1
print(answer)

