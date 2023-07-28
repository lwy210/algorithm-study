import sys
input = sys.stdin.readline

# 테스트 케이스 수
p = int(input())

for i in range(p):
    heights = list(map(int, input().split()))
    t = heights[0]
    line = [heights[1]] # 아무나 한 명을 뽑아 줄의 맨 앞에 세운다.
    heights = heights[2:]
    answer = 0 # 걸음 수
    for j in range(len(heights)):
        if max(line) < heights[j]:
            line.append(heights[j])
        else:
            k = 0
            for height in line:
                if height > heights[j]:
                    break
                k += 1
            line.insert(k, heights[j])
            answer += len(line) - 1 - k
    print(t, answer)