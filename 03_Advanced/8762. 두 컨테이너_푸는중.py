'''
물류회사 에이블은 전국 곳곳에 여러개의 창고를 운영하고 있습니다. 이 창고들에는 각각 1부터 N까지 번호가 매겨져 있으며, 이 창고들을 M개의 양방향으로 통행이 가능한 도로가 각각 2개의 창고를 잇고 있습니다.
이런 물류회사 에이블의 촘촘한 전국 창고망을 눈여겨본 어떤 회사에서 에이블에게 일거리를 주었습니다.

"저희 회사에서 컨테이너 2개를 다른 곳에서 수입해 왔는데, 이 컨테이너가 너무 커서 저희들이 옮기는건 불가능한 것 같습니다. 두 컨테이너는 현재 서로 다른 위치에 있고, 두 컨테이너의 목적지도 서로 다릅니다. 이 두 컨테이너를 대신 이동시켜주세요."
물류회사 에이블은 의뢰를 수행하기 위해 두 컨테이너에 각각 1, 2번 번호를 매겼습니다. 1, 2번 컨테이너의 처음 위치는 S_1, S_2이며, 1, 2번 컨테이너를 각각 D_1, D_2로 옮겨야 합니다.

컨테이너를 다른 창고로 한번 이동시킬 때, 한번에 두 컨테이너 중 하나의 컨테이너만 이동시킬 수 있으며, 현재 이동시킬 컨테이너가 있는 창고에서 직접 도로로 연결된 창고로만 옮길 수 있습니다.
또한 컨테이너는 부피가 매우 크기 때문에, 한 창고에는 하나의 컨테이너만 존재할 수 있습니다. 따라서, 이미 컨테이너가 존재하는 창고에 다른 컨테이너를 이동시킬 수 없습니다.

물류회사 에이블에서는 컨테이너를 다른 창고로 한번 이동시킬 때 비용이 많이 소모되기 때문에, 두 컨테이너를 최소한의 이동 횟수로 목적지까지 이동시키려고 합니다. 두 컨테이너를 각각 원하는 목표 창고까지 이동시키는데 필요한 최소한의 이동 횟수를 구하는 프로그램을 작성하세요.

예제 입력1
5 4
1 5 5 1
1 2
2 3
3 4
3 5
예제 출력1
8

예제 입력2
4 3
1 4 2 3
1 2
2 3
3 4

예제 출력2
-1

입력값 설명
첫 번째 줄에 컨테이너 창고의 수 N, 창고 사이를 잇는 도로의 개수 M이 주어집니다. (2 ≤ N ≤ 200, 0 ≤ M ≤ min(n×(n-1)/2, 5,000))
두 번째 줄에 1번 컨테이너가 처음 위치한 창고의 번호 S_1와 옮겨야 하는 창고의 번호 D_1, 2번 컨테이너가 처음 위치한 창고의 번호 S_2와 옮겨야 하는 창고의 번호 D_2이 주어집니다. (1 ≤ S_1, D_1, S_2, D_2 ≤ N, S_1 ≠ S_2, D_1 ≠ D_2) 컨테이너가 이미 주어진 위치로 옮겨져 있을 수도 있습니다.
세 번째 줄부터 M개의 줄에 걸쳐 각 도로가 잇는 두 창고의 번호 u_i, v_i가 주어집니다. (1 ≤ u_i, v_i ≤ N, u_i ≠ v_i) 서로 다른 도로가 같은 두 창고를 잇는 경우는 존재하지 않습니다.

출력값 설명
두 컨테이너를 주어진 위치로 재배치하는데 필요한 컨테이너 이동 횟수의 최솟값을 출력합니다. 만약 두 컨테이너를 주어진 위치로 재배치시킬 수 없다면 -1을 출력합니다.
'''

from collections import deque

def bfs(start, goal, graph, n):
    distances = [-1] * (n + 1)
    distances[start] = 0
    queue = deque([start])
    
    while queue:
        current = queue.popleft()
        if current == goal:
            return distances[current]
        
        for neighbor in graph[current]:
            if distances[neighbor] == -1:
                distances[neighbor] = distances[current] + 1
                queue.append(neighbor)
    
    return -1

def min_moves_to_relocate_containers(n, m, s1, d1, s2, d2, roads):
    graph = [[] for _ in range(n + 1)]
    for u, v in roads:
        graph[u].append(v)
        graph[v].append(u)
    
    dist1 = bfs(s1, d1, graph, n)
    dist2 = bfs(s2, d2, graph, n)
    
    if dist1 == -1 or dist2 == -1:
        return -1
    
    return dist1 + dist2

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    M = int(data[1])
    
    S1 = int(data[2])
    D1 = int(data[3])
    S2 = int(data[4])
    D2 = int(data[5])
    
    roads = []
    index = 6
    for _ in range(M):
        u = int(data[index])
        v = int(data[index + 1])
        roads.append((u, v))
        index += 2
    
    result = min_moves_to_relocate_containers(N, M, S1, D1, S2, D2, roads)
    print(result)