answer = 0

def dfs(index, value, numbers, target):
    global answer
    N = len(numbers)

    if index == N:
        if value == target:
            answer += 1
        return

    # [4, 1, 2, 1]
    dfs(index + 1, value + numbers[index], numbers, target)  # 4 ...
    dfs(index + 1, value - numbers[index], numbers, target)  # -4 ...

def solution(numbers, target):
    global answer
    dfs(0, 0, numbers, target)

    return answer


"""
처음 접근 방식
"""
# import sys
# sys.setrecursionlimit(100000)
# answer = 0
#
# def dfs(arr, n, numbers, target):
#     global answer
#     if len(arr) == n and sum(arr) == target:
#         answer += 1
#         print(answer)
#         return
#     for i in range(n):
#         for k in range(2):
#             if k == 0:
#                 arr.append(numbers[i])
#                 print(numbers[i])
#             else:
#                 arr.append(-1 * numbers[i])
#             dfs(arr, n, numbers, target)
#             arr.pop()
#
# def solution(numbers, target):
#     arr = []
#     n = len(numbers)
#     dfs(arr, n, numbers, target)
#     return answer