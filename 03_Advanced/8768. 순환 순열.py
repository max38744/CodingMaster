'''
미래는 길이가 N인 순열을 하나 가지고 있습니다.
길이가 N인 순열이란, 1부터 N까지 서로 다른 정수 N개를 임의의 순서로 섞은 것을 말합니다.
예를 들어, {2, 3, 1, 4}는 1부터 4까지의 수가 한 번씩 등장하므로 길이가 4인 순열에 해당합니다.
하지만 {2, 1, 1}은 3이 존재하지 않으므로 순열이 아니고, {1, 2, 4}는 3이 존재하지 않으므로 순열이 아닙니다.

미래는 가지고 있는 길이가 N인 순열을 P라고 부릅니다. 
P_i는 순열의 i번째 수를 말합니다. 
미래는 순열 P를 바탕으로 다음과 같은 규칙으로 노드가 N개며 각 노드의 번호가 1부터 N까지인 그래프를 만들었습니다.

1. 모든 1 ≤ i ≤ N인 i에 대해서 1 ≤ j < i이면서 P_j > P_i인 가장 큰 j를 찾고, 노드 번호가 i인 노드와 j인 노드를 양방향 간선으로 잇는다.

2. 모든 1 ≤ i ≤ N인 i에 대해서 i < j ≤ N이면서 P_j > P_i인 가장 작은 j를 찾고, 노드 번호가 i인 노드와 j인 노드를 양방향 간선으로 잇는다.

예를 들어, N = 4이고 P = {3, 1, 4, 2}인 경우 만들어지는 그래프의 간선은 (1, 3), (2, 1), (2, 3), (4, 3)입니다.

만약 만들어진 그래프에 단순 사이클이 존재한다면, 이 순열을 순환 순열이라고 부릅니다.

순열의 길이 N이 주어질 때, 
길이가 N인 순환 순열의 개수를 출력하는 프로그램을 작성하세요. 

다만 개수가 너무 클 수 있으므로, 1,000,000,007로 나눈 나머지를 대신 출력합니다.
------------------------------------------------------------------------
[입력값 설명]
『순열의 길이 N이 주어집니다. (3 ≤ N ≤ 1,000,000)』

[출력값 설명]
『길이가 N인 순환 순열의 개수를 1,000,000,007로 나눈 나머지를 출력합니다.』
------------------------------------------------------------------------
예제 입력1
3

예제 출력1
2 (전체 : 6 / 제외 : 4=2^2)

예제 입력2
4

예제 출력2
16 (전체 : 24 / 제외 : 8=2^3)

예제 입력3
5

예제 출력3
104 (전체 : 120 / 제외 : 16=2^4)

예제 입력4
6

예제 출력4
688 (전체 : 720 / 제외 : 32=2^5)

예제 입력5
7

예제 출력5
4976 (전체 : 5040 / 제외 : 64=2^6)
'''
# -*- coding: utf-8 -*-
import sys
input = sys.stdin.readline
M = 1000000007

def mod_fact(n, mod):
    result = 1
    for i in range(2, n+1):
        result = (result * i) % mod
    return result

def mod_exp(base, exp, mod):
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result

if __name__ == "__main__":
    N = int(input())
    if N == 1:
        print(0)
    else:
        fact_n = mod_fact(N, M)
        power_of_two = mod_exp(2, N-1, M)
        result = (fact_n - power_of_two) % M
        print(result)

#################################################################
    
# import sys
# input = sys.stdin.readline
# M = 1000000007 # 10**9 + 7

# def fact(n):
#     r = 2
#     for i in range(3, n+1):
#         r *= i
#         if r > M: r -= M
#     return r

# if __name__ == "__main__":
#     N = int(input())
#     print(fact(N) - ((2**(N-1))%M))

#################################################################

# # 역시 permutations를 사용하면 무조건 3~7 tiemout 뜨는듯?
# from itertools import permutations
# M = 1000000007

# def is_cycle_P(p, v, visit, P):
#     visit[v] = True
    
#     big_j = -1
#     for j in range(v):
#         if (j != p) and (P[j] > P[v]): big_j = max(big_j, j)
#     if big_j != -1:
#         if visit[big_j] == True: return True
#         if is_cycle_P(v, big_j, visit, P): return True
    
#     small_j = float('inf')
#     for j in range(v+1, N):
#         if (j != p) and (P[j] > P[v]): small_j = min(small_j, j)
#     if small_j != float('inf'):
#         if visit[small_j] == True: return True
#         if is_cycle_P(v, small_j, visit, P): return True
        
#     return False

# if __name__ == "__main__":
#     N = int(input())
#     answer = 0
    
#     for P in permutations(range(N)):
#         chk = False
#         for i in range(N):
#             visited = [False] * N
#             if is_cycle_P(-1, i, visited, P):
#                 chk = True
#                 break
#         if chk: answer += 1
    
#     print(answer)

#################################################################
# from functools import reduce
# M = 1000000007

# # reduce로 팩토리얼 계산 시, 5, 7번 타임아웃 (6은 아슬아슬)
# def fact_reduce(n):
#     return reduce(lambda x, y: x*y, range(2, n+1))

# # 재귀함수로 구현 시, 5 ~ 7번 그냥 틀림 (메모리 아웃을 그냥 틀린걸로 쳐버린걸까?)
# def fact_recur(n):
#     return n * fact_recur(n-1) if n > 2 else 2

# # for 문으로 팩토리얼 계산 시, 5, 7번 타임아웃 (6은 아슬아슬)
# def fact_for(n):
#     r = 2
#     for i in range(3, n+1): r *= i
#     return r

# if __name__ == "__main__":
#     N = int(input())
#     print((fact_for(N) - 2**(N-1))%M)

#################################################################

# # 응 아니야 이것도 5, 7 번 타임아웃 떠
# from math import factorial
# M = 1000000007

# if __name__ == "__main__":
#     N = int(input())
#     # 순환 순열 수 = 전체 순열 갯수 - 비순환 순열 수
#     # 전체 순열은 수학 공식으로 구하기 가능
#     # 비순환 순열의 수는 2^(N-1) 순서대로 늘어난다!
#     # 이걸 확인한 코드는 문제 그대로 작성한 것으로 그건......
#     print((factorial(N) - 2**(N-1))%M)

#################################################################

# # 이 모든 걸 그대로 연산하면 timeout이 뜬다! (3~7까지 전부)
# # 아무래도 간선을 전부 만들기 전에, 간선 체크 단계에서 다음 연결 정점을 체크하는 식으로 사이클을 찾아야할듯
# # 일단 permutations 쓰면 N이 11일 때 단순히 for 문 돌리기만 해도, 로컬환경에서도 47초 걸리는만큼 사용하면 안 됨
# from itertools import permutations
# M = 1000000007

# # 순열 p를 입력받았을 때, 만들어지는 간선 확인해서 반환
# def make_edges(p):
#     Edges = [[] for _ in range(N)]
#     # 모든 1 ≤ i ≤ N인 i에 대해서
#     for i in range(N):
#         e = -1
#         # 1 ≤ j < i이면서
#         for j in range(i):
#             # 이미 만들어진 간선이면 체크하지 말고 넘어가자!
#             if j in Edges[i]: continue
            
#             # P_j > P_i인 가장 큰 j를 찾고 -> 가장 큰 j를 e에 저장
#             if p[j] > p[i]: e = max(e, j)
#         # 노드 번호가 i인 노드와 j인 노드를 양방향 간선으로 잇는다.
#         # 그런데 가장 큰 j가 없다면 -> e가 -1 이라면 만들지 마!
#         if e != -1:
#             Edges[i].append(e)
#             Edges[e].append(i)
        
#         e = float('inf')
#         # i < j ≤ N이면서
#         for j in range(i+1, N):
#             # 이미 만들어진 간선이면 체크하지 말고 넘어가자!
#             if j in Edges[i]: continue
            
#             # P_j > P_i인 가장 작은 j를 찾고 -> 가장 작은 j를 e에 저장
#             if p[j] > p[i]: e = min(e, j)
#         # 노드 번호가 i인 노드와 j인 노드를 양방향 간선으로 잇는다.
#         # 그런데 가장 작은 j가 없다면 -> e가 무한이라면 만들지 마!
#         if e != float('inf'):
#             Edges[i].append(e)
#             Edges[e].append(i)
#     return Edges

# # 현재 정점에서 사이클 만들어지는지 체크
# def is_cycle(p, v, visited, E):
#     # 현재 정점은 방문 체크
#     visited[v] = True
#     # 현재 정점에서 연결된 정점들 체크 / e는 다음에 방문할 정점
#     for e in E[v]:
#         # 이전에 방문하고 온 정점이면 체크 안함 (양방향 그래프니까)
#         if e == p: continue
#         # 만약 다음에 가려는 정점이 이미 방문한 곳이라면? 이건 사이클이다!
#         if visited[e] == True: return True

#         # 앞에서 걸린거 없으면 현재 정점 v가 직전 정점 p, 다음 방문할 정점 e는 현재 정점 v로 넣어주기
#         if is_cycle(v, e, visited, E): return True # 앞서서 True 판정 났으면 뒤까지 안 가고 바로 True
#     # 현재 정점에서 연결된거 다 체크했는데 사이클 아니면 False 반환
#     return False

# # 간선들을 표시해둔 2차원 배열 E를 받아서 순환배열인지 체크
# def chk_cycle(E):
#     # 사이클 체크를 시작할 정점 v
#     for v in range(N):
#         # 방문 체크할 배열 visited
#         visited = [False] * N

#         # 현재 정점부터 연결된 사이클 있는지 체크
#         if is_cycle(-1, v, visited, E): return True
#     # 다 돌아봤는데도 사이클 없으면 False
#     return False

# if __name__ == "__main__":
#     N = int(input())
#     answer = 0
#     cnt = 0

#     # N 길이에서 나올 수 있는 모든 순열을 하나씩 빼오자
#     for p in permutations(range(N)):
#         edges = make_edges(p)

#         if chk_cycle(edges):
#             answer += 1
#         cnt += 1

#     print(answer%M)
#     print(cnt) # 전체 순열 갯수 알아내기
