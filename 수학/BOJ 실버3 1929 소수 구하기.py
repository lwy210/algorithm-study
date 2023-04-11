import sys
input = sys.stdin.readline

# m이상 n이하의 소수를 모두 출력하는 프로그램

# 에라토스테네스의 체 : 소수 판별 리스트
is_prime = [False, False] + [True] * (1000000-1)
for i in range(2, len(is_prime)):
    if is_prime[i]:
        for j in range(2*i, len(is_prime), i):
            is_prime[j] = False

# 입력 받기
m, n = map(int, input().split())

# 출력 하기
for i in range(m, n+1):
    if is_prime[i]:
        print(i)