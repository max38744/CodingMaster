
'''
8700. 좋은 배열


배열 a에 1부터 N까지의 양의 정수가 각각 2개씩 포함되어 있습니다. 
즉, 배열 a의 길이는 2N입니다.

a의 i번째 원소를 a_i라고 할 때, 다음 조건을 만족하는 a를 “좋은 배열”이라고 정의합니다.

- 모든 정수 i, j, p, q (1 ≤ i < j < p < q ≤ 2N)에 대해 a_i = a_p이면 a_j ≠ a_q이다.

배열 a가 주어질 때, 배열 a가 좋은 배열인지 아닌지 판단하는 프로그램을 작성하세요.


예제 입력1
3
2 1 1 2 3 3

예제 출력1
YES

예제 입력2
3
2 1 1 3 2 3

예제 출력2
NO

입력값 설명

첫째 줄에 양의 정수 N이 주어집니다. (2 ≤ N ≤ 1,000)
둘째 줄에 2N개의 양의 정수 a_1, a_2, …, a_2N이 공백으로 구분되어 주어집니다. (1 ≤ a_i ≤ N)

출력값 설명

좋은 배열이면 “YES”, 좋은 배열이 아니면 “NO”를 출력합니다. (큰 따옴표 제외)

'''

# -*- coding: utf-8 -*-
import sys

def div(arr): # 한 배열을 같은 숫자를 기준으로 안쪽 바깥쪽 배열 두개로 나누기
    if len(arr) % 2 != 0: # 좋지 않은 배열일 경우 flags에 0 추가
        flags.append(0)
        return
    if len(arr) == 2 or len(arr) == 0: # 정상적인 배열일 경우 1 추가
        flags.append(1)
        return
        
    s = arr[0]
    e = arr[1:].index(s)+1
    
    arr1 = arr[1:e]
    arr2 = arr[e+1:]
    div(arr1) # 나눈 배열을 재귀로 다시 넣어주기
    div(arr2)
    
n = int(input())

arr = list(map(int, input().split()))

flags = []

div(arr)
# print(flags)
if 0 in flags:
    print('NO')
else:
    print('YES')
