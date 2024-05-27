'''
기성과 기승은 쌍둥이 수학 영재입니다.
부모님은 그런 아이들이 기특하여 어린이날 선물로 다양한 수열들을 선물해 주셨습니다.
쌍둥이가 가장 마음에 들어한 선물은 양의 정수로 구성된 길이가 N인 수열입니다.
둘은 이 수열로 재미있는 놀이를 하려고 합니다.

우선 수열의 i번째 수를 A[i]로 표현하기로 약속합시다.
자신의 차례가 되면 두 정수 i와 j(1 ≤ i ≤ j ≤ N)를 고르고,
A[i] × A[i+1] × A[i+2] × … × A[j-1] × A[j]를 양의 정수 M으로 나눈 나머지를 점수로 얻습니다.

단, 한번 고른 (i, j)쌍은 누구도 더 이상 고를 수 없습니다.
게임은 두 명 모두 0점인 채로 시작하며, 기성이 먼저 시작해 번갈아가며 진행합니다. 
N × (N + 1) ÷ 2번의 차례가 지나면 더 이상 두 정수를 고를 수 없으므로 게임이 종료됩니다.

둘의 목표는 (자신의 점수) - (상대방의 점수)를 최대화 하는 것으로, 반드시 목표를 달성하기 위한 최선의 선택을 합니다. 

예를 들어 수열이 [3, 4]이고 M이 10인 경우를 살펴봅시다.

기성은 (2, 2)를 골라 4점을 얻고,
다음으로 기승이 (1, 1)을 골라 3점을 얻고,
마지막으로 기성이 (1, 2)를 골라 2점을 얻으며 게임이 끝납니다. 
기성의 점수는 4 + 2 = 6점, 기승의 점수는 3점입니다.

수열과 정수 M이 주어지면, 게임이 끝났을 때 기성의 점수에서 기승의 점수를 뺀 값을 출력하는 프로그램을 작성하세요.

예제 입력1
2
3 4
10
예제 출력1
3

예제 입력2
4
3 6 2 1
21
예제 출력2
14


입력값 설명
첫째 줄에 수열의 길이 N이 주어집니다. (2 ≤ N ≤ 2,000)
둘째 줄에 수열의 원소가 공백을 구분으로 주어집니다. (1 ≤ 수열의 모든 원소 ≤ 1,000,000)
셋째 줄에 정수 M이 주어집니다. (2 ≤ M ≤ 1,000,000)

출력값 설명
게임이 끝났을 때 기성의 점수에서 기승의 점수를 뺀 값을 출력합니다.
'''

# -*- coding: utf-8 -*-
import sys

input = sys.stdin.readline

def get_score(n, sequence, m):
    
    score = [0] * (int(n*(n+1)/2)+1)
    ind = 0
    for i in range(len(sequence)):
        for j in range(i, len(sequence)):
            ind += 1
            if j == i:
                score[ind] = sequence[j] % m
            else:
                score[ind] = score[ind-1] * sequence[j] % m
    
    score = sorted(score, reverse=True)
    return score

def seq_figth(n,sequence,m):
    score = get_score(n,sequence,m)

    sum = 0
    for i in range(len(score)):
        if i % 2 == 0:
            sum += score[i]
        else: sum -= score[i]
    
    return sum
    

N = int(input())
sequence = list(map(int,input().split()))
M = int(input())

# N = 2
# sequence = [3, 4]
# M = 10

print(seq_figth(N,sequence,M))