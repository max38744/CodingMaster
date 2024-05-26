'''
철수가 사는 동네는 N개의 구역과 M개의 단방향 도로로 구성되어 있습니다. 

각 구역에는 1번부터 N번까지 번호가 붙어있고, 철수는 1번 구역에 있습니다.



철수는 소화도 시킬 겸 동네를 산책하려고 합니다. 

그런데 도로들이 모두 단방향이므로, 

처음에 출발했던 구역으로 다시 돌아오지 못할 수도 있습니다.



구역과 도로들의 정보가 주어졌을 때, 

철수가 처음 출발했던 1번 구역으로 돌아올 수 있는지 판단하는 프로그램을 작성하세요. 



단, 1번 구역 외 다른 구역을 적어도 한번은 거쳐야 산책으로 인정됩니다.


예제 입력1

3 3
1 2
2 3
3 1

예제 출력1

YES

예제 입력2

3 3
1 2
1 3
3 2

예제 출력2

NO


입력값 설명

첫째 줄에 구역의 개수와 단방향 도로의 개수를 의미하는 양의 정수 N과 M이 공백으로 구분되어 주어집니다. (2 ≤ N ≤ 100, 1 ≤ M ≤ 500)

이어서 M개의 줄에 걸쳐 단방향 도로의 시작 구역의 번호 s와 도착 구역의 번호 e가 주어집니다.
이는 해당 도로를 통해 s번 구역에서 e번 구역으로 이동할 수 있음을 의미합니다.
단, s ≠ e이며 s번 구역에서 e번 구역으로 향하는 간선은 단 하나만 존재합니다.

출력값 설명

다른 구역을 거쳐 1번 구역으로 돌아올 수 있으면 “YES”, 돌아올 수 없으면 “NO”를 출력합니다.
'''
    
# -*- coding: utf-8 -*-
import sys

# 철수가 사는 동네에 N개 구역과 M개의 단방향 도로 구성
# 1번부터 N번 번호 붙어잇음, 철수는 1번구역으로 돌아올 수 있나?

from collections import deque

def can_return(N, M, graph):
    # deque에 1을 추가
    queue = deque([1])
    while queue:
        # 가장 왼쪽을 하나 씩 빼자
        node = queue.popleft()
        # 조건이 충족할 때, 모두 방문(산책), 1로 돌아왔을 때
        if node == 1 and visited[node]:
            return "YES"
        # 아직 방문하지 않은 노드에 대해서 방문 처리
        if not visited[node]:
            visited[node] = True
            # 다음에 방문할 수 있는 노드를 queue에 추가.
            for next_node in graph[node]:
                queue.append(next_node)
    return "NO"

            

N, M = map(int, input().split(" "))
graph = [[] for _ in range(0, N + 1)]

for i in range(M) :
    node1, node2 = map(int, input().split(" "))
    graph[node1].append(node2)

visited = [False for _ in range(0, N+1)]
print(can_return(N,M, graph))
