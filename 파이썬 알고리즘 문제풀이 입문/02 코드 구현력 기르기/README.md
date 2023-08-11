# 알게 된 문법 & 팁
> for-else문, set 자료구조, 파이썬에서 가장 큰 값, 반올림, enumerate() 함수, dict 정렬

## for-else문
- else문은 for문이 break 등으로 중간에 빠져나오지 않고 끝까지 실행 됐을 경우 실행된다.

```python
for i in range(5):
    if i == 2:
        print(i)
        break
else:
    print("-1")
```
출력 결과 : 0 1

<br>

## set 자료구조
https://wikidocs.net/1015

- 중복을 없앨 수 있다.
- 정렬 기능이 없기 때문에 정렬을 위해서는 list 자료구조로 변환해야 한다.
- `s1.add(2)` : 값 1개 추가
- `s1.update([4, 5])` : 값 여러 개 추가
- `s1.remove(2)` : 특정 값 제거
- 교집합 - `&`, 합집합 `|`, 차집합 `-`

<br>

## 파이썬에서 가장 큰 값

`float(’inf’)`

<br>

## 반올림

- round는 사사오입 X
- 사사오입 반올림을 위해서는 다음과 같이 하면 된다.
```python
a = 66.5
a = a + 0.5
a = int(a)
print(a)
```
출력 결과 : 67

<br>

## enumerate() 함수
- 인덱스와 원소를 동시에 접근하면서 루프를 돌릴 수 있다.
- 2차원 리스트를 이중 중첩 for문에 enumerate() 함수를 적용해서 접근할 수도 있다.
```python
for e in enumerate(['A', 'B', 'C']):
    print(e)

# 출력 결과
# (0, 'A')
# (1, 'B')
# (2, 'C')
```

```python
for i, char in enumerate(['A', 'B', 'C']):
    print(i, char)

# 출력 결과
# 0 A
# 1 B
# 2 C
```

<br>

## dict 정렬
- key를 기준으로 정렬 : `sorted_dict = sorted(my_dict.items())`
- value를 기준으로 정렬 : `sorted_dict = sorted(my_dict.items(), key = lambda item: item[1])`


<br>
<br>
<br>

# 문제풀이

## K번째 약수
<details>
<summary>문제</summary>
<pre>
현수는 1부터 100사이의 자연수가 적힌 N장의 카드를 가지고 있습니다. 같은 숫자의 카드가 
여러장 있을 수 있습니다. 현수는 이 중 3장을 뽑아 각 카드에 적힌 수를 합한 값을 기록하려
고 합니다. 3장을 뽑을 수 있는 모든 경우를 기록합니다. 기록한 값 중 K번째로 큰 수를 출력
하는 프로그램을 작성하세요.

만약 큰 수부터 만들어진 수가 25 25 23 23 22 20 19......이고 K값이 3이라면 K번째 큰 값
은 22입니다.

▣ 입력설명
첫 줄에 자연수 N(3<=N<=100)과 K(1<=K<=50) 입력되고, 그 다음 줄에 N개의 카드값이 입력
된다.

▣ 출력설명
첫 줄에 K번째 수를 출력합니다. K번째 수는 반드시 존재합니다.

▣ 입력예제 1 
10 3
13 15 34 23 45 65 33 11 26 42

▣ 출력예제 1
143
</pre>
</details>

<br>



```python
import sys
# sys.stdin = open("input.txt", "rt")

n, k = map(int, input().split())
a = list(map(int, input().split()))
res = set()
for i in range(n):
    for j in range(i+1, n):
        for m in range(j+1, n):
            res.add(a[i]+a[j]+a[m])

res = list(res)
res.sort(reverse=True)
print(res[k-1])
```
- 중복을 피하기 위해 set 자료형을 사용했음

<br>

## 대표값

<details>
<summary>문제</summary>
<pre>
N명의 학생의 수학점수가 주어집니다. N명의 학생들의 평균(소수 첫째자리 반올림)을 구하고, 
N명의 학생 중 평균에 가장 가까운 학생은 몇 번째 학생인지 출력하는 프로그램을 작성하세
요.
평균과 가장 가까운 점수가 여러 개일 경우 먼저 점수가 높은 학생의 번호를 답으로 하고, 높
은 점수를 가진 학생이 여러 명일 경우 그 중 학생번호가 빠른 학생의 번호를 답으로 합니다.

▣ 입력설명
첫줄에 자연수 N(5<=N<=100)이 주어지고, 두 번째 줄에는 각 학생의 수학점수인 N개의 자연
수가 주어집니다. 학생의 번호는 앞에서부터 1로 시작해서 N까지이다.

▣ 출력설명
첫줄에 평균과 평균에 가장 가까운 학생의 번호를 출력한다.
평균은 소수 첫째 자리에서 반올림합니다.

▣ 입력예제 1 
10
45 73 66 87 92 67 75 79 75 80

▣ 출력예제 1
74 7

예제설명
평균이 74점으로 평균과 가장 가까운 점수는 73(2번), 75(7번), 75(9번)입니다. 여기서 점수가 높은 
75(7번), 75(9번)이 답이 될 수 있고, 75점이 두명이므로 학생번호가 빠른 7번이 답이 됩니다.
</pre>
</details>

<br>

```python
import sys
# sys.stdin = open("input.txt", "rt")

n = int(input())
a = list(map(int, input().split()))
avg = round(sum(a) / n)

min=2147000000
for idx, x in enumerate(a):
    tmp = abs(x-avg)
    if tmp < min:
        min=tmp
        score = x
        res=idx+1
    elif tmp==min:
        if x>score:
            score = x
            res=idx+1

print(avg, res)
```
- enumerate로 idx와 value(x)를 반복마다 가져왔음
- 현재 tmp(diff)가 최솟값보다 작으면 1) 최솟값 갱신, 2) 현재 score 기록, 3) 현재 학생 순서 res 기록
- "평균과 가장 가까운 점수가 여러 개일 경우 먼저 점수가 높은 학생의 번호를 답으로 하고, 높은 점수를 가진 학생이 여러 명일 경우 그 중 학생번호가 빠른 학생의 번호를 답으로 합니다." 
    - ⇒ 따라서, tmp(diff)가 최솟값과 같으면 현재 score가 이전 score보다 클 때만 갱신


<br>

## 정다면체

<details>
<summary>문제</summary>
<pre>
두 개의 정 N면체와 정 M면체의 두 개의 주사위를 던져서 나올 수 있는 눈의 합 중 가장 확
률이 높은 숫자를 출력하는 프로그램을 작성하세요.
정답이 여러 개일 경우 오름차순으로 출력합니다.

▣ 입력설명
첫 번째 줄에는 자연수 N과 M이 주어집니다. N과 M은 4, 6, 8, 12, 20 중의 하나입니다.

▣ 출력설명
첫 번째 줄에 답을 출력합니다.

▣ 입력예제 1 
4 6

▣ 출력예제 1
5 6 7
</pre>
</details>

<br>

```python
import sys
# sys.stdin = open("input.txt", "rt")

n, m = map(int, input().split())

dict = {}

for i in range(1, n+1):
    for j in range(1, m+1):
        if i+j in dict.keys():
            dict[i+j] += 1
        else:
            dict[i+j] = 1

dict = sorted(dict.items(), key = lambda x : x[1], reverse=True)
p_max = dict[0][1]

for d in dict:
    if d[1] == p_max:
        print(d[0], end=" ")
    else:
        break
```
- 나의 풀이 : dict 자료형 활용
- 강사 풀이 : list 자료형의 인덱스 활용

<br>

## 자릿수의 합

<details>
<summary>문제</summary>
<pre>
N개의 자연수가 입력되면 각 자연수의 자릿수의 합을 구하고, 그 합이 최대인 자연수를 출력
하는 프로그램을 작성하세요. 각 자연수의 자릿수의 합을 구하는 함수를 def digit_sum(x)를 
꼭 작성해서 프로그래밍 하세요.

▣ 입력설명
첫 줄에 자연수의 개수 N(3<=N<=100)이 주어지고, 그 다음 줄에 N개의 자연수가 주어진다.
각 자연수의 크기는 10,000,000를 넘지 않는다.

▣ 출력설명
자릿수의 합이 최대인 자연수를 출력한다. 자릿수의 합이 같을 경우 입력순으로 먼저인 숫자
를 출력합니다.

▣ 입력예제 1 
3
125 15232 97

▣ 출력예제 1
97
</pre>
</details>

<br>

```python
import sys
# sys.stdin = open("input.txt", "rt")

def digit_sum(x):
    arr = list(str(x))
    result = 0
    for a in arr:
        result += int(a)
    return result

n = int(input())
numbers = list(map(int, input().split()))
arr = []

for i in range(n):
    arr.append(digit_sum(numbers[i]))

max_idx = arr.index(max(arr))
print(numbers[max_idx])
```
- 내가 작성한 답 : 파이썬의 문자열을 이용하고 리스트를 하나 더 생성해서 max를 구했다.

<br>

```python
def digit_sum(x):
    sum = 0
    while x>0:
        sum += x%10
        x = x//10
    return sum

n = int(input())
numbers = list(map(int, input().split()))
max = -2147000000

for x in numbers:
    total = digit_sum(x)
    if total > max:
        max = total
        res = x

print(res)
```
- 강사 풀이 : 수학적인 접근을 통해 문제를 해결 - `digit_sum()`

<br>

## 소수의 개수(에라토스테네스 체)
참고 : https://github.com/lwy210/algorithm-study/tree/main/%EC%88%98%ED%95%99
<details>
<summary>문제</summary>
<pre>
자연수 N이 입력되면 1부터 N까지의 소수의 개수를 출력하는 프로그램을 작성하세요. 
만약 20이 입력되면 1부터 20까지의 소수는 2, 3, 5, 7, 11, 13, 17, 19로 총 8개입니다.
제한시간은 1초입니다. 

▣ 입력설명
첫 줄에 자연수의 개수 N(2<=N<=200,000)이 주어집니다.

▣ 출력설명
첫 줄에 소수의 개수를 출력합니다.

▣ 입력예제 1 
20

▣ 출력예제 1
8
</pre>
</details>

<br>

```python
import sys
# sys.stdin = open("input.txt", "rt")

n = int(input())
a = [0] * (n+1)
cnt = 0

for i in range(2, n+1):
    if a[i] == 0:
        cnt += 1
        for j in range(i, n+1, i):
            a[j] = 1

print(cnt)
```
- a가 `[False, False] + [True] * (n+1)`이 아닌 방법도 있다.
- a를 모두 0으로 초기화하고 인덱스 활용하는 방향임



<br>


## 점수 계산 (가산점)

<details>
<summary>문제</summary>
<pre>
OX 문제는 맞거나 틀린 두 경우의 답을 가지는 문제를 말한다. 여러 개의 OX 문제로 만들어진 
시험에서 연속적으로 답을 맞히는 경우에는 가산점을 주기 위해서 다음과 같이 점수 계산을 하기
로 하였다. 1번 문제가 맞는 경우에는 1점으로 계산한다. 앞의 문제에 대해서는 답을 틀리다가 
답이 맞는 처음 문제는 1점으로 계산한다. 또한, 연속으로 문제의 답이 맞는 경우에서 두 번째 
문제는 2점, 세 번째 문제는 3점, ..., K번째 문제는 K점으로 계산한다. 틀린 문제는 0점으로 계산한다.

예를 들어, 아래와 같이 10 개의 OX 문제에서 답이 맞은 문제의 경우에는 1로 표시하고, 틀린 경
우에는 0으로 표시하였을 때, 점수 계산은 아래 표와 같이 계산되어, 총 점수는 
1+1+2+3+1+2=10 점이다.

시험문제의 채점 결과가 주어졌을 때, 총 점수를 계산하는 프로그램을 작성하시오. 

▣ 입력설명
첫째 줄에 문제의 개수 N (1 ≤ N ≤ 100)이 주어진다. 둘째 줄에는 N개 문제의 채점 결과를 나
타내는 0 혹은 1이 빈 칸을 사이에 두고 주어진다. 0은 문제의 답이 틀린 경우이고, 1은 문제의 
답이 맞는 경우이다. 

▣ 출력설명
첫째 줄에 입력에서 주어진 채점 결과에 대하여 가산점을 고려한 총 점수를 출력한다. 

▣ 입력예제 1 
10
1 0 1 1 1 0 0 1 1 0

▣ 출력예제 1
10
</pre>
</details>

<br>

```python
import sys
sys.stdin = open("input.txt", "rt")

n = int(input())
a = list(map(int, input().split()))

sum = 0
cnt = 0 # 가산점

for x in a:
    if x==1:
        cnt += 1
        sum += cnt
    else:
        cnt = 0

print(sum)

```
