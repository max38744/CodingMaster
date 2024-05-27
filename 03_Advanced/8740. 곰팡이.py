'''

[문제]

준하는 번식력이 아주 뛰어난 곰팡이를 배양하는데 성공했습니다.
이 곰팡이는 포자 상태에서 1분이 지나면 번식 가능한 상태가 됩니다.
번식 가능한 곰팡이는 그 이후 매 1분마다 1개의 포자를 만들어 냅니다.

예를 들어, 
0분 시점에 곰팡이 포자 1개가 있다고 할 때, 3분까지의 곰팡이 수는 다음과 같습니다.

0분 : 곰팡이 포자 1개
1분 : 번식 가능한 곰팡이 1개
2분 : 번식 가능한 곰팡이 1개, 곰팡이 포자 1개
3분 : 번식 가능한 곰팡이 2개, 곰팡이 포자 1개

0분 시점에 곰팡이 포자 1개가 있을 때, 
N분 후에 곰팡이 포자와 번식 가능한 곰팡이를 합친 총 곰팡이 수를 계산하는 프로그램을 작성하세요.

------------------------------------------------------------------------
[입력값 설명]
첫째 줄에 N이 주어집니다. (1 ≤ N ≤ 1,000,000,000,000)

[출력값 설명]
N분 후에 총 곰팡이 수를 출력합니다.
곰팡이가 너무 많아질 수 있으므로, 1,000,000,007로 나눈 나머지를 출력합니다.

------------------------------------------------------------------------
예제 입력1
3

예제 출력1
3

예제 입력2
6

예제 출력2
13

'''
# -*- coding: utf-8 -*-
import sys
input = sys.stdin.readline
import numpy as np

MOD = 1_000_000_007

def matrix_power(matrix, power, mod=MOD):
    result = np.eye(2, dtype=np.int64)
    base = np.array(matrix, dtype=np.int64)
    
    while power > 0:
        if power % 2 == 1:
            result = np.dot(result, base) % mod
        base = np.dot(base, base) % mod
        power //= 2
    
    return result

def count_molds(N):
    if N == 0:
        return 1  # Initially, there is one spore
    transition_matrix = [[0, 1], [1, 1]]
    result_matrix = matrix_power(transition_matrix, N, MOD)
    
    # Initial state [spores, reproducible]
    initial_state = np.array([1, 0], dtype=np.int64)
    
    # Calculate the final state
    final_state = np.dot(result_matrix, initial_state) % MOD
    
    return (final_state[0] + final_state[1]) % MOD

if __name__ == "__main__":
    # 입력값 받기
    N = int(input())
    # 결과 출력
    print(count_molds(N))
