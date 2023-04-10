import sys
input = sys.stdin.readline

n = int(input())
ropes = []

# 리스트의 로프의 길이 저장 (큰수 부터)
for _ in range(n):
    ropes.append(int(input()))
ropes.sort(reverse=True)

# ropes[i]: 선택한 로프 중 가장 작은 로프
answers = []
for i in range(n):
    answers.append(ropes[i] * (i+1))

print(max(answers))
