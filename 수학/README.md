## 최대공약수 구하기
유클리드 호제법을 이용해서 함수를 작성한다.
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
