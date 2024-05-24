'''
정수론은 수학의 분야 중 하나로, 정수의 성질을 연구하는 학문입니다. 암호학, 정보 이론 등 다양한 분야에서 정수론 지식이 활용됩니다. 널리 알려진 정수론 문제로는 페르마의 마지막 정리(Fermat's Last Theorem)가 있습니다.



정수론에 관심이 많은 철수는 정수들을 나열해놓고 그 사이에서 규칙을 발견하는 것을 좋아합니다. 단, 정수가 너무 많으면 규칙을 발견하기 어렵기 때문에 N개의 서로 다른 정수만 나열하고, i번째로 나열된 정수를 편의상 a_i로 표기합니다.



평소처럼 정수를 관찰하던 철수는 당신에게 다음과 같은 질문을 던졌습니다.

- 어떤 양의 정수 p로 나눴을 때 나머지가 p - 1인 수들의 집합을 M(p)로 정의할 때, 10억 이하의 양의 정수 중에서 M(a_1), M(a_2), …, M(a_N) 중 적어도 하나에 속하는 정수의 개수는 얼마입니까?



예를 들어 N = 2, a_1 = 3, a_2 = 5라고 가정하겠습니다.

정수 1: a_1으로 나눴을 때 나머지가 1이고, a_2로 나눴을 때 나머지가 1입니다. 정수 1은 M(a_1), M(a_2) 중 어디에도 속하지 않으므로 조건을 만족하지 않습니다.

정수 4: a_1으로 나눴을 때 나머지가 1이고, a_2로 나눴을 때 나머지가 4입니다. 정수 4는 M(a_2)에 속하므로 조건을 만족하는 정수입니다.

정수 14: a_1으로 나눴을 때 나머지가 2이고, a_2로 나눴을 때 나머지가 4입니다. 정수 14는 M(a_1)과 M(a_2) 모두에 속하므로 조건을 만족하는 정수입니다.



철수의 질문에 대한 답을 구하는 프로그램을 작성해주세요.


예제 입력1

2
3 5

예제 출력1

466666667

예제 입력2

10
2 4 6 8 10 12 14 16 18 20

예제 출력2

500000000


입력값 설명

첫째 줄에 나열된 정수의 개수를 의미하는 양의 정수 N이 주어집니다. (1 ≤ N ≤ 15)
둘째 줄에 a_i가 공백으로 구분되어 주어집니다. (2 ≤ a_i ≤ 2,000)

출력값 설명

첫째 줄에 철수의 질문에 대한 답을 출력합니다.
'''

# -*- coding: utf-8 -*-
import sys
import math
from itertools import combinations

M = 1000000001

input = sys.stdin.readline

def lcm(a,b):
    return a*b // math.gcd(a,b)
    
def multi_lcm(arr):
    n = arr[0]
    for i in arr[1:]:
        n = lcm(n,i)
    return n

def integer_observe(N, int_list):
    sum = 0
    for i in range(1,N+1):
        for subset in combinations(int_list,i):
            key = multi_lcm(subset)
            if i % 2 == 1:
                sum += M // key
            else : 
                sum -= M // key

    return sum

N = int(input())
int_list = list(map(int,input().split()))

print(integer_observe(N ,int_list))
