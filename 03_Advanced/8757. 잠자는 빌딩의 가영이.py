'''
가영은 몽유병을 앓고 있습니다.
그래서 밤이면 밤마다 N층 높이의 아파트 안에서 배회하곤 합니다.

가영은 1분마다 일정한 확률로 윗층으로 올라가거나, 아랫층으로 내려가거나, 현재 있는 층에 머물게 됩니다.

단, 1층에서 내려가려고 시도하거나 맨 윗층에서 올라가려고 시도하면 가영은 꿈에서 깨게 됩니다.

꿈에서 깬 가영은 아파트 밖으로 나오게 됩니다.

구체적으로는 1분마다 p의 확률로 현재 층에서 윗층으로 올라가려고 시도하고,
q의 확률로 아랫층으로 내려가려고 시도하며,
r의 확률로 현재 층에 머무르게 됩니다.

단, p + q + r = 1이 성립합니다.

가영이 어떤 층에서 다른 층으로 이동할 확률과 어떤 층에서 시작했는지 주어집니다.
X가 주어질 때,
X분 뒤에 가영이 각 층에 있을 확률과 꿈에서 깰 확률을 구하는 프로그램을 작성하세요. 
------------------------------------------------------------------------
[입력값 설명]
『첫 번째 줄에 정수 N, K, A, B, C, X가 공백으로 구분되어 입력됩니다.
(1 ≤ N, X ≤ 8, 1 ≤ K ≤ N, 0 ≤ A, B, C ≤ 3, 1 ≤ A+C)
N은 아파트의 높이를 의미하고, K는 가영이가 어느 층에서 시작하는 지를 의미합니다.
그리고 윗층으로 올라갈 확률 p는 p = A/(A+B+C),
아랫층으로 내려갈 확률 q는 q = B/(A+B+C),
현재층에 머무를 확률 r은 r = C/(A+B+C)입니다.
마지막으로 X는 가영이 잠든지 X분이 흐른 뒤를 의미합니다.』

[출력값 설명]
『첫 번째 줄에 "p/q"꼴로 기약분수 N개를 공백으로 구분하여 출력합니다.
첫 번째 분수는 가영이 X분 뒤 1층에 있을 확률, 두 번째 분수는 2층에 있을 확률, ... , N번째 분수는 가영이 X분 뒤 N층에 있을 확률입니다.

두 번째 줄에 "p/q"꼴로 기약분수 1개를 출력합니다.
이는 X분 뒤 가영이 꿈에서 깰 확률입니다.

모든 출력에 대해서, 정수를 출력해야 할 때는 "p/1"꼴로 분모를 1로 써서 출력합니다.』
------------------------------------------------------------------------
예제 입력1
2 1 1 1 1 2

예제 출력1
2/9 2/9
5/9

예제 입력2
8 4 1 1 3 8

예제 출력2
19992/390625 46668/390625 74256/390625 86514/390625 14856/78125 46927/390625 21648/390625 278/15625
2678/78125

테스트 케이스 6
5 5 1 1 1 2

테스트 케이스 7
8 3 1 3 2 4

'''
# -*- coding: utf-8 -*-
import sys
input = sys.stdin.readline
from collections import deque
import math

# 최소공배수
def lcm(a, b):
    return a * b // math.gcd(a, b)

# 배열 형태의 분수 덧셈
def prob_sum(aP, bP):
    # aP 가 [0, 0] 이라면? 그냥 bP 그대로 보내기
    if aP == [0, 1]: return bP
    # 분모가 같다면 분자만 더해주기
    if aP[1] == bP[1]:
        return [aP[0]+bP[0], aP[1]]
    # 분모가 다르다면? 최소공배수로 통분 후 계산
    else:
        lcmP = lcm(aP[1], bP[1])
        aK, bK = lcmP//aP[1], lcmP//bP[1]
        return [(aP[0]*aK)+(bP[0]*bK), lcmP]

# 배열 형태의 분수 약분
def red_frac(p):
    if p[0]==0: return p
    k = math.gcd(p[0], p[1])
    return [p[0]//k, p[1]//k]

# 확률을 [분자, 분모] 형태로 표현한다(배열)
if __name__ == "__main__":
    N, K, A, B, C, X = map(int, input().split())
    
    # 인덱스 0은 잠에서 깰 확률, 1~N까지는 해당 층에 있을 확률
    answer = [[0, 1] for _ in range(N+1)]
    # 확률 미리 넣어두기 (0, +1, -1)
    prob = [[C, (A+B+C)], [A, (A+B+C)], [B, (A+B+C)]]
    
    Q = deque()
    # 현위치, 확률, 시간
    Q.append((K, [1, 1], 0))
    while Q:
        now, sumP, time = Q.popleft()
        # 잠에서 깨는 경우에는 0에다가 확률 더해줌
        if (now == 0) or (now == N+1):
            answer[0] = prob_sum(answer[0], sumP)
            continue
        # X분이 되면 해당 위치까지의 확률을 더해줌
        if time == X:
            answer[now] = prob_sum(answer[now], sumP)
            continue
        # -1부터 +1까지
        for i in range(-1, 2):
            # 분자끼리 곱하고 분모끼리 곱하기
            p = [prob[i][0]*sumP[0], prob[i][1]*sumP[1]]
            Q.append((now+i, p, time+1))
            
    # 답은 기약분수로
    for i in range(1, N+1):
        ans = red_frac(answer[i])
        print(f'{ans[0]}/{ans[1]}', end=' ')
    # 잠에서 깰 확률도 써주자
    ans = red_frac(answer[0])
    print('\n'+f'{ans[0]}/{ans[1]}')

#################################################################

# # 용석 코드
# 6번 : "0 0 1/9 2/9 2/9\r\n4/9\r\n"
# 7번 : "11/48 13/54 107/648 13/162 1/36 1/162 1/1296 0\r\n1/4\r\n"
# -*- coding: utf-8 -*-
# import sys
# from fractions import Fraction

# input = sys.stdin.readline

# N, K, A, B, C, X = map(int, input().split())

# p = Fraction(A,(A+B+C))
# q = Fraction(B,(A+B+C))
# r = Fraction(C,(A+B+C))
    
# prob = [Fraction(0)] * (N+1)
# prob[K] = Fraction(1)

# for _ in range(X):
#     pre_prob = prob.copy()
#     for i in range(N+1):
#         if i == 0:
#             prob[i] = pre_prob[i-1]*p + pre_prob[i] + pre_prob[i+1]*q
#         elif i == 1:
#             prob[i] = pre_prob[i]*r + pre_prob[i+1]*q
#         elif i == N:
#             prob[i] = pre_prob[i-1]*p + pre_prob[i]*r
#         else:
#             prob[i] = pre_prob[i-1]*p + pre_prob[i]*r + pre_prob[i+1]*q
        
# for i in range(1,N+1):
#     print(f'{prob[i].numerator}/{prob[i].denominator}', end =' ')
# print('\n'+f'{prob[0].numerator}/{prob[0].denominator}')