import sys
input = sys.stdin.readline

n = int(input())

new_n = (n%10)*10 + ((n//10)+(n%10))%10
answer = 1

while n != new_n:
    answer += 1
    new_n = (new_n%10)*10 + ((new_n//10)+(new_n%10))%10

print(answer)