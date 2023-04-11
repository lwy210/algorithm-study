## 최대공약수 구하기
`유클리드 호제법`을 이용해서 함수를 작성한다.
```python
def gcd(a, b):
    while b!=0:
        a, b = b, a%b
    return a

```
<br/>
<br/>

## 최소공배수 구하기
최소공약수를 구하는 함수를 이용해서 최소공배수를 구한다.
```python
def lcm(a, b):
    my_gcd = gcd(a, b)
    # return (a * b) // my_gcd
```

<br/>
<br/>

## 공약수 구하기
두 수의 공약수를 구할 경우, 최대공약수의 약수를 구하면 된다.
```python
for i in range(1, my_gcd//2 + 1):       # 최대공약수의 절반을 탐색 구간으로 설정
    if my_gcd % i == 0:
        print(i)
print(my_gcd)                           # 최대공약수 자기 자신 출력
``` 

<br/>
<br/>

## 에라토스테네스의 체
`에라토스테네스의 체`를 이용해서 소수를 구한다.
<br/><br/>
![Sieve_of_Eratosthenes_animation](https://user-images.githubusercontent.com/33020581/231061079-b242fd95-9b18-4c88-a96d-a3a935439856.gif)
1. 소수 판별 리스트 is_prime을 생성한다. (2~N)
2. 지우지 않은 수 중 가장 작은 수 P를 찾는다. (P: 소수)
3. P를 지우고, 아직 지우지 않은 P의 배수를 크기 순서대로 지운다. `range(2*i, len(is_prime), i)`
4. 아직 모든 수를 지우지 않았다면 다시 2번 단계로 간다.
<br/><br/>
### 소수 판별하기
```python
is_prime = [False, False] + [True] * (1000000-1)
for i in range(2, len(is_prime)):
    if is_prime[i]:
        for j in range(2*i, len(is_prime), i):
            is_prime[j] = False
```
<br/><br/>
### 소수 구하기
```python
is_prime = [False, False] + [True] * (1000000-1)           # 소수 판별
primes = []                                                # 소수 저장
for i in range(2, len(is_prime)):
    if is_prime[i]:
        primes.append(i)
        for j in range(2*i, len(is_prime), i):
            is_prime[j] = False
```
<br/><br/>
