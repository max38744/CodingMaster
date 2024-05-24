'''

동근은 정사면체 주사위를 가지고 놀고 있습니다. 
주사위의 각 면에는 1부터 4까지의 숫자가 하나씩 적혀있습니다. 
동근은 문득 정사면체 주사위를 한 번 이상 던져 나온 눈금의 합이 N이 되는 경우의 수가 궁금해졌습니다.

동근을 위해 자연수 N이 주어졌을 때, 주사위의 눈금의 합이 N이 되는 경우의 수를 1,000,000,007로 나눈 나머지를 출력하는 프로그램을 작성하세요.

예를 들어 눈금의 합이 N=3인 경우의 수는 다음과 같이 4개입니다.

1 + 1 + 1
1 + 2
2 + 1
3

------------------------------------------------------------------------
[입력값 설명]
첫째 줄에 자연수 N이 주어집니다. (1 ≤ N ≤ 10¹²)

[출력값 설명]
주사위의 눈금의 합이 N이 되는 경우의 수를 1,000,000,007로 나눈 나머지를 출력합니다.
------------------------------------------------------------------------
예제 입력1
3

예제 출력1
4

예제 입력2
10000000

예제 출력2
511752262

[설명]
행렬 제곱법(Matrix Exponentiation)으로 풀기 
DP로 풀면 메모리, 시간 문제 발생 

주사위의 각 면이 1부터 4까지 숫자를 가질 수 있음 
점화식 
f(N) = f(N-1)+f(N-2)+f(N-3)+f(N-4)
f(0)=1
f(1)=1
f(2)=2
f(3)=4

여기서 
f(0)인 이유는 주사위를 한 번도 던지지 않은 경우도 포함되기 때문

이런 점화식을 DP로 풀면 안풀림 -> 형렬 제곱법으로 풀면 
[   
    f(N),
    f(N-1),
    f(N-2),
    f(N-3)
] = 

[
    [1,1,1,1],
    [1,0,0,0],
    [0,1,0,0],
    [0,0,1,0]
] * 
[
    f(N-1),
    f(N-2),
    f(N-3),
    f(N-4)
]

말도 안되게 어려워~ 이걸 어떻게 풀어 
'''

# -*- coding: utf-8 -*-
import sys
import numpy as np 

input = sys.stdin.readline

MOD = 1_000_000_007

def matrix_mult(A, B):
    # 행렬 곱셈
    return np.dot(A, B) % MOD

def matrix_pow(mat, exp):
    # 행렬 거듭제곱
    res = [[1 if i == j else 0 for j in range(4)] for i in range(4)]
    base = mat
    while exp:
        if exp % 2 == 1:
            res = matrix_mult(res, base)
        base = matrix_mult(base, base)
        exp //= 2
    return res

def solution(N):
    if N == 1:
        return 1
    if N == 2:
        return 2
    if N == 3:
        return 4
    
    T = [
        [1, 1, 1, 1],
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0]
    ]
    
    T_n_minus_3 = matrix_pow(T, N-3)
    
    F = [4, 2, 1, 1]
    
    result = 0
    for i in range(4):
        result = (result + T_n_minus_3[0][i] * F[i]) % MOD
    
    return result

if __name__ == "__main__":
    N = int(input())
    
    res = solution(N)
    print(res)

# DP로 풀때
# # -*- coding: utf-8 -*-
# import sys
# import numpy as np 

# input = sys.stdin.readline

# MOD = 1_000_000_007

# def matrix_mult(A, B):
#     # 행렬 곱셈
#     return np.dot(A, B) % MOD

# def matrix_pow(mat, exp):
#     # 행렬 거듭제곱
#     res = [[1 if i == j else 0 for j in range(4)] for i in range(4)]
#     base = mat
#     while exp:
#         if exp % 2 == 1:
#             res = matrix_mult(res, base)
#         base = matrix_mult(base, base)
#         exp //= 2
#     return res

# def solution(N):
#     # 초기 조건
#     if N == 1:
#         return 1
#     if N == 2:
#         return 2
#     if N == 3:
#         return 4
#     if N == 4:
#         return 8
    
#     # DP 배열 초기화
#     dp = [0] * (N + 1)
#     dp[0] = 1
#     dp[1] = 1
#     dp[2] = 2
#     dp[3] = 4
#     dp[4] = 8
    
#     # DP 점화식에 따라 배열 채우기
#     for i in range(5, N + 1):
#         dp[i] = (dp[i-1] + dp[i-2] + dp[i-3] + dp[i-4]) % MOD
    
#     return dp[N]

# if __name__ == "__main__":
#     # N = int(input())
#     N = 10000000
#     res = solution(N)
#     print(res)

