'''
철수가 사는 나라는 N개의 도시와 M개의 단방향 도로로 구성됩니다. 
각 도시에는 1번부터 N번까지 번호가 붙어있습니다. 
각 도로에는 가중치가 붙어있으며, 
도로를 통과하는 데 해당 도로에 붙은 가중치만큼 시간이 걸립니다.

철수는 집에서 회사로 출근하면서 자녀를 학교에 바래다줍니다. 
철수의 집은 1번 도시에 위치하고, 철수의 회사는 N번 도시에 위치합니다. 
철수의 자녀가 다니는 학교는 K번 도시에 위치합니다.

예를 들어 N = 5이고, 철수의 자녀가 3번 도시에 위치한 학교를 다닌다고 가정하겠습니다. 
철수는 1번 도시에서 출발해서 3번 도시에 들러 자녀를 내려주고 회사가 위치한 5번 도시로 향합니다.

도로의 정보가 주어졌을 때, 
철수가 집에서 출발해서 자녀를 학교에 데려다주고 회사에 출근하는 데 걸리는 최소 시간을 구하는 프로그램을 작성하세요.


예제 입력1

5 4 2
1 3 1
3 5 1
3 2 4
2 5 4

예제 출력1

9

예제 입력2

3 3 2
1 2 1
2 3 3
3 1 3

예제 출력2

4


입력값 설명

첫째 줄에 도시의 개수 N과 단방향 도로의 개수 M, 자녀의 학교가 위치한 도시의 번호 K가 공백으로 구분되어 주어집니다. (2 ≤ K < N ≤ 1,000, 1 ≤ M ≤ 3,000)
이어서 M개의 줄에 걸쳐 도로의 정보가 주어집니다.
각 줄에는 양의 정수 u, v, w가 공백으로 구분되어 주어집니다.

이는 u번 도시에서 v번 도시로 향하는 단방향 도로가 존재하고, 해당 도로의 가중치가 w임을 의미합니다.
출발 도시의 번호가 u이고 도착 도시의 번호가 v인 도로는 하나만 존재합니다. (1 ≤ u, v ≤ N, u ≠ v, 1 ≤ w ≤ 1,000)

철수가 자녀를 학교에 데려다주고 회사에 출근할 수 있는 입력만 주어집니다.

출력값 설명

첫째 줄에 철수가 집에서 출발해서 자녀를 학교에 데려다주고 회사에 출근하는 데 걸리는 최소 시간을 출력합니다.
'''
# -*- coding: utf-8 -*-
import sys
import heapq
input = sys.stdin.readline

def dijkstra(graph, start, end):
  heap = list()
  dist = [float('inf')] * (n + 1)
  dist[start] = 0
  heapq.heappush(heap, (0, start))

  while len(heap) != 0:
    cur = heapq.heappop(heap) 

    if dist[cur[1]] < cur[0]:
      continue

    for next in graph[cur[1]]:  
      cost = dist[cur[1]] + next[1]
      if cost < dist[next[0]]:
        dist[next[0]] = cost
        heapq.heappush(heap, (cost, next[0]))

  return dist[end]
    
n, m, k = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))    

print(dijkstra(graph, 1, k)+dijkstra(graph, k, n))