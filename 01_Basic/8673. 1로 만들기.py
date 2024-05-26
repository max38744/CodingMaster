'''
정수 X가 주어질 때 정수 X에 사용할 수 있는 연산은 다음과 같이 4가지입니다.

1. X가 5로 나누어 떨어지면, 5로 나눕니다
2. X가 3으로 나누어 떨어지면, 3으로 나눕니다
3. X가 2로 나누어 떨어지면, 2로 나눕니다
4. X에서 1을 뺍니다.

정수 X가 주어졌을 때, 위와 같은 연산 4개를 적절히 사용해서 1을 만들려고 합니다. 연산을 사용하는 횟수의 최솟값을 출력합니다.

예를 들어 정수가 26인 경우 26 -> 25 -> 5 -> 1로 3번의 연산이 최솟값입니다.
------------------------------------------------------------------------
[입력값 설명]
『첫째 줄에 정수 X가 주어집니다. (1 ≤ X ≤ 30,000)』

[출력값 설명]
『첫째 줄에 연산을 하는 횟수의 최솟값을 출력합니다.』
------------------------------------------------------------------------
예제 입력1
26

예제 출력1
3

예제 입력2
99

예제 출력2
5
'''
# -*- coding: utf-8 -*-
import sys
input = sys.stdin.readline
from collections import deque

if __name__ == "__main__":
    X = int(input())
    
    Q = deque()
    Q.append((X, 0))
    while True:
        X, cnt = Q.popleft()
        if X == 1:
            answer = cnt
            break
        
        if X % 5 == 0: Q.append((X//5, cnt+1))
        if X % 3 == 0: Q.append((X//3, cnt+1))
        if X % 2 == 0: Q.append((X//2, cnt+1))
        Q.append((X-1, cnt+1))
    
    print(answer)
    
    
    
    
# 중복 파일 정리
'''
import sys

N = int(sys.stdin.readline())

cnt = 0
while(N != 1):
    if N % 5 == 1:
        N = N - 1
        cnt+= 1
    elif N % 5 == 2 and N % 3 != 0:
        N = N - 1
        cnt += 1
    elif N % 5 == 0:
        N = N / 5
        cnt += 1
    elif N % 3 == 0:
        N = N / 3
        cnt += 1
    elif N % 2 == 0:
        N = N /2
        cnt += 1
    else:
        N = N - 1
        cnt += 1

print(cnt)



'''
