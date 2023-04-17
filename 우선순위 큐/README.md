# 우선순위 큐
- 각 원소들은 우선순위를 가지고 있다. <br/>
- 우선순위 큐에서, 높은 우선순위를 가진 원소는 낮은 우선순위를 가진 원소보다 먼저 처리된다. <br/>
- 같은 우선순위를 가진다면, 먼저 들어온 원소를 처리한다.
 <br/> <br/>
 
# 최대 힙 & 최소 힙
![image](https://user-images.githubusercontent.com/33020581/232496595-d22095bf-b6be-4385-9021-6ff8dfadcbfb.png)<br/>
## 힙 (heap)
- 힙은 이진트리의 일종이다.
- 정렬된 상태가 아니다. 
- 완전이진트리와는 다르게 중복값이 허용된다.

## 최대 힙
- `부모노드` > `자식노드`
- 따라서, 힙에 값을 넣게 되면 최댓값 순으로 값을 얻을 수 있다.
```python
import heapq

heap = []

# 아래 for문을 실행하고 나면 heap은 [1,2,3,5,4]로 힙 정렬이 되게 된다.
for i in range(1,6):
	heapq.heappush(heap, i)

# 작은 숫자 순서대로 1,2,3,4,5가 출력된다.
for i in range(5):
	print(heapq.heappop(heap))
```
 <br/> <br/>

## 최소 힙
- `부모노드` < `자식노드` 
- 따라서, 힙에 값을 넣게 되면 최솟값 순으로 값을 얻을 수 있다.
```python
import heapq

heap = []
values = [1,5,3,2,4]

# 아래 for문을 실행시키고 나면 heap은 [-5,-4,-3,-1,-2]가 된다.
for value in values:
	heapq.heappush(heap, -value)

# 아래 for문을 실행시키면 5,4,3,2,1이 출력된다. 즉, 큰 숫자부터 출력이 된다.
for i in range(5):
	print(-heapq.heappop(heap))
```

 <br/> <br/>
[참고블로그](https://velog.io/@yyj8771/Python-heapq%EB%A5%BC-%EC%9D%B4%EC%9A%A9%ED%95%9C-%EC%B5%9C%EC%86%8C-%ED%9E%99-%EC%B5%9C%EB%8C%80-%ED%9E%99)
