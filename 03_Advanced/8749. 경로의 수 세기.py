'''
[문제]

동욱은 미로에 있습니다. 
미로는 1번부터 n번까지 번호 붙여진 방들과 방들을 연결하는 통로들로 구성되어 있습니다. 
동욱은 현재 1번 방에 있으며 동욱은 통로를 따라 방을 옮겨 다니며 미로의 출구인 n번 방으로 이동합니다.

동욱이 방을 최대한 적게 거쳐가면서 미로를 탈출할 수 있는 경로의 수를 1,000,000,007로 나눈 나머지를 출력하는 프로그램을 작성하세요.

------------------------------------------------------------------------
[입력값 설명]
첫째 줄에 방의 수를 의미하는 n과 통로의 수를 의미하는 k가 공백으로 구분되어 주어집니다. (2 ≤ n, k ≤ 1,000)
둘째 줄부터 k개의 줄에 걸쳐 통로의 정보가 주어집니다.
각각의 줄은 서로 다른 두 자연수 u, v가 공백으로 구분되어 주어지며 u번 방과 v번 방을 연결하는 통로임을 의미합니다. 
이때 두 방 사이에는 많아봐야 한 개의 통로가 존재합니다. 또한 1번 방에서 다른 모든 방으로 이동할 수 있는 경우의 입력만 주어집니다.

[출력값 설명]
동욱이가 방을 최대한 적게 거쳐가면서 미로를 탈출할 수 있는 경로의 수를 1,000,000,007로 나눈 나머지를 출력합니다.

------------------------------------------------------------------------
예제 입력1
10 10
1 4
1 6
1 5
5 7
7 8
7 9
8 9
10 2
3 2
3 1

예제 출력1
1


'''

# -*- coding: utf-8 -*-
import sys
from collections import deque, defaultdict
sys.stdin=open('input.txt', 'r')

input = sys.stdin.readline

MOD = 1_000_000_007

# BFS를 통해 최단 경로와 그 경로의 수 계산
def BFS(start, end):
    dist = [-1] * (n + 1)           # 방(index) 별 거리 기록하기 위해 
    path_cnt = [0] * (n + 1)      # 경로의 수 기록 
    Q = deque([start])              # 현재 위치에서 시작 
    
    dist[start] = 0
    path_cnt[start] = 1
    
    while Q:
        x = Q.popleft()
        
        for node in graph[x]:                   # 현재 x 위치 기반 이동할 수 있는 모든 곳 
            if dist[node] == -1:                # 아직 방문하지 않은 노드
                dist[node] = dist[x] + 1        # x까지 오는데 걸린 거리 + 1 = 다음 노드까지의 거리 
                path_cnt[node] = path_cnt[x]
                Q.append(node)                  # 다음 노드로 이동 
            elif dist[node] == dist[x] + 1:     # 최단 경로에 포함되는 노드
                path_cnt[node] = (path_cnt[node] + path_cnt[x]) % MOD
    
    return path_cnt[end]    # 기록된 목표 방까지의 경로의 수 

if __name__ == "__main__":
    # 현재 1번 방에 있으며, 미로의 출구인 n번 방으로 이동하는게 목표 
    n,k = map(int, input().split())         # 방의 수를 의미하는 n과 통로의 수를 의미하는 k  (2 ≤ n, k ≤ 1,000)
    
    graph = defaultdict(list)               # 그래프 생성 
    for _ in range(k):
        u,v = map(int, input().split())     # u번 방과 v번 방을 연결하는 통로임
        graph[u].append(v)
        graph[v].append(u)
        

    res = BFS(1, n)      # 현재 위치 1 -> n번방으로 가기 
    print(res)
   