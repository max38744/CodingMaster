'''
영희는 3개의 양의 정수를 가지고 있습니다.
영희는 그 수를 a, b, c라고 이름을 붙였습니다.
영희는 이 a, b, c를 이용하여 x, y, z라는 수를 만들어냈습니다.

영희가 만들어낸 x, y, z는 다음과 같습니다. 
영희는 이 연산 과정을 최댓값 연산이라는 이름을 붙였습니다.

x = max(a, b), y = max(b, c), z = max(c, a)

영희는 그러던 중, a, b, c 3개의 수를 잊어버렸습니다.
뿐만 아니라, 가지고 있는 x, y, z 3개의 수가 a, b, c로부터 만들어진 수인지조차 불분명하다는 것을 인지하였습니다.

영희는 먼저 이 x, y, z라는 수가 임의의 3 수에 최댓값 연산을 해서 나올 수 있는 수인지부터 알아내려고 합니다.
3개의 양의 정수 x, y, z가 주어졌을 때, 이 3개의 수가 최댓값 연산을 해서 나올 수 있는 수인지 알아내는 프로그램을 작성하세요.


예제 입력1
3 5 5
예제 출력1
possible

예제 입력2
49 49 50
예제 출력2
impossible

입력값 설명
3개의 정수 x, y, z가 공백으로 구분되어 주어집니다. (1 ≤ x ≤ y ≤ z ≤ 1,000)
출력값 설명
이 3개의 수가 최댓값 연산을 해서 나올 수 있는 수이면 possible, 아니면 impossible을 출력합니다. 답은 무조건 소문자로만 출력해야 함에 유의하세요.
'''

# 제가 손으로 계산했을때 3가지 가능성만 존재하는 걸 확인했습니다
# 1) (a,a,b)(a>b)
# 2) (a,b,a)(a>b)
# 3) (b,a,a)(a>b)
# 위에 상황이라면 possible
# 아니라면 impossible

# -*- coding: utf-8 -*-
import sys

input = sys.stdin.readline

def maximum_value_operation(x,y,z):
    a = max(x,y,z)
    b = min(x,y,z)
    
    if [x,y,z] == [a,a,b] or [x,y,z] == [a,b,a] or [x,y,z] == [b,a,a]:
        return print('possible')
    else: return print('impossible')        


x, y, z = map(int, input().split())
maximum_value_operation(x,y,z)
