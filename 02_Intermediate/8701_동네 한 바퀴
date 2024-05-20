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
