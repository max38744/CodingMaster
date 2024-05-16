'''
사원수는 아일랜드의 수학자 윌리엄 로원 해밀턴이 창시한 수 체계입니다. 

사원수는 복소수의 확장으로 허수 단위 i에 다른 허수 단위 j, k를 도입한 체계입니다. 



i, j, k의 정의는 다음과 같습니다. 

i² = j² = k² = ijk = -1

여기서 i≠j, j≠k, k≠i임을 유도할 수 있습니다. 



또한, 사원수 체계에서는 곱셈의 교환법칙이 성립하지 않고 아래와 같은 식이 성립됩니다. 

jk = -kj = i

ki = -ik = j

ij = -ji = k

하지만 곱셈의 결합법칙은 여전히 성립합니다. 



두 사원수가 주어졌을 때, 이 둘을 곱하는 프로그램을 작성하세요.


예제 입력1

0 1 0 0
0 0 1 0

예제 출력1

0 0 0 1

예제 입력2

0 0 1 0
0 1 0 0

예제 출력2

0 0 0 -1


입력값 설명

첫 번째 줄에 정수 4개 a, b, c, d가 공백으로 구분되어 주어집니다.
이는 첫 번째 사원수 a + bi + cj + dk를 의미합니다.
두 번째 줄에 정수 4개 w, x, y, z가 공백으로 구분되어 주어집니다.
이는 두 번째 사원수 w + xi + yj + zk를 의미합니다.

입력되는 모든 정수는 절댓값이 10,000을 넘지 않습니다.

출력값 설명

첫 번째 줄에 네 개의 정수 o, p, q, r을 출력합니다.
이는 첫 번째 사원수에 두 번째 사원수를 곱하면 o + pi + qj + rk가 됨을 의미합니다.\
'''

# -*- coding: utf-8 -*-
import sys
import numpy as np

input = sys.stdin.readline

def quaternion(a,b):
    a = np.array(a)
    B = np.array([
        [ b[0],  b[1],  b[2],  b[3]],
        [-b[1],  b[0], -b[3],  b[2]],
        [-b[2],  b[3],  b[0], -b[1]],
        [-b[3], -b[2],  b[1],  b[0]]
        ])
        
    answer = np.dot(a,B)
    
    return print(*answer)


a = list(map(int,input().split()))
b = list(map(int,input().split()))

quaternion(a,b)