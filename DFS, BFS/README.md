## 그래프 구현방법
### 1. 인접 행렬로 구현하기
`인접 행렬` 
- 2차원 배열로 그래프의 연결 관계를 표현하는 방식
- 모든 관계를 저장하므로 메모리 이슈
- 정보 얻는 속도는 빠름
```python
# 인접 행렬 방식 예제
INF = 999999999 # 무한의 비용 선언

# 2차원 리스트를 이용해 인접 행렬 표현
graph = [
	[0, 7, 5],
	[7, 0, INF],
	[5, INF, 0]
]

print(graph)

## 출력 결과 ##
# [[0, 7, 5], [7, 0, 999999999], [5, 999999999, 0]]
```

<br>
<br>

### 2. 인접 리스트로 구현하기
`인접 리스트` 
- 리스트로 그래프의 연결 관계를 표현하는 방식
- 메모리 공간 낭비가 비교적 적음
- 앞에서부터 차례대로 확인해야 원하는 정보 얻을 수 있음
```python
# 인접 리스트 방식 예제

# 행이 3개인 2차원 리스트로 인접 리스트 표현 
graph = [[] for _ in range(3)]

# 노드 0에 연결된 노드 정보 저장 (노드, 거리)
graph[0].append((1, 7))
graph[0].append((2, 5))

# 노드 1에 연결된 노드 정보 저장 (노드, 거리)
graph[1].append((0, 7))

# 노드 2에 연결된 노드 정보 저장 (노드, 거리)
graph[2].append((0, 5))

print(graph)

## 출력 결과 ##
# [[(1, 7), (2, 5)], [(0, 7)], [(0, 5)]]
```

# DFS (Depth-First Search)
- 깊이 우선 탐색이라고도 부른다.
- 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘이다.
- 동작 원리 : **스택**
- 구현 방법 : **재귀 함수 이용**

```python
# DFS 메서드 정의
def dfs(graph, v, visited):
	# 현재 노드를 방문 처리
	visited[v] = True
	print(v, end=' ')
	# 현재 노드와 연결된 다른 노드를 재귀적으로 방문
	for i in graph[v]:
		if not visited[i]:
			dfs(graph, i, visited)
	
# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
	[],
	[2, 3, 8],
	[1, 7],
	[1, 4, 5],
	[3, 5],
	[3, 4],
	[7],
	[2, 6, 8],
	[1, 7]
]

# 각 노드가 방문된 정보를 리스트 자료현으로 표현(1차원 리스트)
visited = [False] * 9

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)

## 출력 결과 ##
# 1 2 7 6 8 3 4 5
```

<br>
<br>

# BFS (Breadth-First Search)

- 너비 우선 탐색이라고도 부른다.
- 가까운 노드부터 탐색하는 알고리즘이다.
- 동작원리 : **큐**
- 구현방법 : **큐 자료구조 이용**

```python
from collections import deque

# BFS 메서드 정의
def bfs(graph, start, visited):
	# 큐(Queue) 구현을 위해 deque 라이브러리 사용
	queue = deque([start])
	# 현재 노드를 방문 처리
	visited[start] = True
	# 큐가 빌 때까지 반복
	while queue:
		# 큐에서 하나의 원소를 뽑아서 출력
		v = queue.popleft()
		print(v, end=' ')
		# 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
		for i in graph[v]:
			if not visited[i]:
				queue.append(i)
				visited[i] = True

# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
	[],
	[2, 3, 8],
	[1, 7],
	[1, 4, 5],
	[3, 5],
	[3, 4],
	[7],
	[2, 6, 8],
	[1, 7]
]

# 각 노드가 방문된 정보를 리스트 자료현으로 표현(1차원 리스트)
visited = [False] * 9

# 정의된 DFS 함수 호출
bfs(graph, 1, visited)

## 출력 결과 ##
# 1 2 3 8 7 4 5 6
```