import sys
input = sys.stdin.readline

# 최대공약수 구하는 함수
def gcd(a, b):
    while b!=0:
        a, b = b, a%b
    return a

# 최소공배수 구하는 함수
def lcm(a, b):
    my_gcd = gcd(a, b)
    return my_gcd * (a//my_gcd) * (b//my_gcd)
    # return (a * b) // my_gcd

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(lcm(a, b))