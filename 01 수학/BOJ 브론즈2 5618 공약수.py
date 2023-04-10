import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))

# 최소 공약수를 구하는 함수
def gcd(a, b):
    while b!=0:
        a, b = b, a%b
    return a

# n의 개수에 따라 my_gcd 구하기
if n==2:
    my_gcd = gcd(numbers[0], numbers[1])
elif n==3:
    my_gcd = gcd(gcd(numbers[0], numbers[1]), numbers[2])
# my_gcd = gcd(numbers[0], gcd(numbers[1], numbers[-1]))

for i in range(1, my_gcd//2 + 1):
    if my_gcd % i == 0:
        print(i)
print(my_gcd)