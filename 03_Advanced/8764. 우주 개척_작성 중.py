'''
20XX년, 인류는 워프 항해를 발명하고 여러 나라들이 지구와 멀리 떨어져 있는 행성들을 개척해 나가기 시작했습니다.
우리나라에서 보낸 탐사대 역시 사람이 살 수 있는 행성 여러 개를 찾아내 지구로 돌아왔습니다.

이제 여러분이 할 일은 이 행성들에 정착한 사람들이 원활한 통신이 가능하도록 탐사대가 찾은 모든 행성들을 연결하는 통신망을 건설하는 것입니다.
하지만 우주 시대에도 비용 문제는 여전했기 때문에, 최소한의 비용을 사용해 모든 행성을 잇는 통신망을 건설해야 합니다.

만약 행성 사이에 알려진 경로가 존재하는 경우 그 경로를 따라 두 행성을 잇는 통신망을 건설할 수 있습니다. 이때 통신망을 건설하는 비용은 경로에 따라 다릅니다.

또한, 아무 두 행성을 골라 워프 항해 기술을 이용한 통신망을 건설하여 두 행성을 연결할 수 있습니다.
이때의 건설 비용은 어떤 두 행성을 고르냐에 관계 없이 동일하며, 고른 두 행성이 알려진 경로를 따라 연결되지 않은 상태여도 통신망을 건설하는 것이 가능합니다.
------------------------------------------------------------------------
[입력값 설명]
『첫 번째 줄에 통신망을 연결할 행성의 개수 N, 알려진 행성 간의 경로의 개수 M, 워프 차원을 통과하는 통신망을 건설할 때 필요한 비용 K가 주어진다.
(2 ≤ N ≤ 100,000, 1 ≤ M ≤ 2,000, 1 ≤ K ≤ 10,000)

두 번째 줄부터 M개의 줄에 걸쳐 알려진 행성 간의 경로의 정보 u_i, v_i, w_i가 주어진다.
u_i와 v_i는 경로가 잇는 행성의 번호, w_i는 이 경로에 통신망을 건설하기 위해 필요한 비용이다. (1 ≤ u_i, v_i ≤ N, u_i ≠ v_i, 1 ≤ w_i ≤ 10,000)』

[출력값 설명]
『주어진 모든 행성을 연결하는 통신망을 만들기 위해 필요한 최소 비용을 출력합니다.』
------------------------------------------------------------------------
예제 입력1
3 3 5
1 2 1
2 3 2
1 3 3

예제 출력1
3

예제 입력2
8 6 7
1 2 3
3 4 2
5 6 2
6 7 10
7 8 5
5 8 8

예제 출력2
33
'''
# -*- coding: utf-8 -*-
import sys
input = sys.stdin.readline
# 3,4,5 Timeout -> 유니온 파인드를 GPT가 작성해줌
# 유니온 파인드 해결하거나 Edge를 바꾸기
# merge_sets 역할 : 집합들 중 합칠 수 있는 집합은 합쳐서 반환하기
import numpy as np
INF = 10001

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

def merge_sets(sets):
    n = len(sets)
    uf = UnionFind(n)

    # 집합들의 교집합 여부를 확인하여 유니온 연산 수행
    for i in range(n):
        for j in range(i + 1, n):
            if sets[i] & sets[j]:
                uf.union(i, j)

    # 유니온 파인드 결과를 바탕으로 새로운 집합들 생성
    merged_sets = {}
    for i in range(n):
        root = uf.find(i)
        if root not in merged_sets:
            merged_sets[root] = set()
        merged_sets[root] |= sets[i]

    return list(merged_sets.values())

if __name__ == "__main__":
    N, M, K = map(int, input().split())
    # 간선 비용 초기화 (자기 자리는 최댓값으로 설정)
    Edge = np.array([[INF] * N for _ in range(N)])
    for _ in range(M):
        u, v, w = map(int, input().split())
        Edge[u-1][v-1] = w
        Edge[v-1][u-1] = w

    # 만들어진 통신망 묶음을 저장할 공간
    maked_set = []
    # 통신망 개통된 행성은 True
    visited = [False] * N
    
    answer = 0
    while False in visited:
        # 일단 최소 비용 가진 경로 찾기
        k = np.min(Edge)
        # k 가 신설 가능한 비용 K보다 싸면
        if k < K:
            # k 값으로 행성들 합치기
            us = np.where(Edge == k)[0]
            vs = np.where(Edge == k)[1]

            # 최소 비용 행성들끼리 묶어주기
            for u, v in zip(us, vs):
                chk = False
                for s in maked_set:
                    # u나 v가 이미 있는 집합이라면 추가만 해주자
                    if (u in s) or (v in s):
                        s.add(v)
                        s.add(u)
                        chk = True
                # 만약 기존 집합에 행성 추가를 못했다면 새로 추가
                if not chk: maked_set.append(set([u, v]))
                # 통신망 개설했으니 개설 비용을 추가
                answer += Edge[u][v]
                # 방문 체크
                visited[u] = True
                visited[v] = True
                # 개설완료한 부분은 INF 로 바꾸자
                Edge[u][v] = INF

            # 만들어진 집합들 끼리 합칠 수 있으면 합치기
            maked_set = merge_sets(maked_set)
        # k가 신설 비용 K와 같거나 비싸면 일단 탈출
        else: break
    # 일단 양방향 간선이니까, answer를 2로 나눠주자
    answer //= 2
    # 만들어진 집합 수와, 외딴 행성(False인 행성) 간 신설할 통신망 비용 더하기
    answer += (len(maked_set) + visited.count(False) - 1) * K
    print(answer)
        
#############################################################################

# # 최소 비용 행성에서 다른 행성으로 연결되는 경로가 없으면(모든 행성이 동일 값을 갖게되면) 값이 이상해짐
# import numpy as np
# INF = 10001

# if __name__ == "__main__":
#     N, M, K = map(int, input().split())
#     # 간선 비용 초기화 (자기 자리는 최댓값으로 설정)
#     Edge = np.where(np.eye(N), INF, K).astype(int)
#     for _ in range(M):
#         u, v, w = map(int, input().split())
#         Edge[u-1][v-1] = w
#         Edge[v-1][u-1] = w
        
#     # 통신망 건설 완료됐으면 True
#     visited = np.array([False] * N)
#     # 탐색 시작할 행성 정하기 : 최소간선 있는 곳
#     s = np.where(Edge == np.min(Edge))[0][0]
#     # 시작 행성은 방문한걸로 설정
#     visited[s] = True
#     # 시작 위치에서 다른 행성까지 드는 통신망 비용
#     dist = Edge[s]
    
#     answer = 0
#     while False in visited:
#         # 현재 최소 비용으로 방문 가능한 행성 목록을 찾자
#         uvs = np.where(visited == False)[0]
#         uvs = np.where(dist == min(dist[uvs]))[0]
#         # 해당 행성들에 통신망 건설 시 드는 비용 +
#         answer += dist[uvs[0]]*len(uvs)
#         # 해당 행성들은 전부 방문처리
#         visited[uvs] = True
#         # 해당 행성들까지 고려했을 때, 들어가는 통신망 비용 갱신
#         for uv in uvs:
#             dist = np.where(dist <= Edge[uv], dist, Edge[uv])
    
#     print(answer)
