import sys
input = sys.stdin.readline

# 소수인지 판별하는 함수
def is_prime(n):
    if n==1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# 입력받기
m = int(input())
n = int(input())
primes = []

# m~n 범위의 소수인 수를 primes에 append
for num in range(m, n+1):
    if is_prime(num):
        primes.append(num)

# 출력하기
if len(primes) == 0:
    print(-1)
else:
    print(sum(primes))
    print(min(primes))