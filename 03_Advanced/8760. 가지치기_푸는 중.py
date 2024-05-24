'''
가영은 에이블 저택의 정원사입니다. 

가영의 역할은 저택 벽을 장식하고 있는 덩굴나무를 트리모양으로 아름답게 유지하는 것입니다.



어느 날 장기휴가에서 돌아온 가영은 덩굴나무가 양분을 가득 먹고 가지가 늘어나 더 이상 트리 모양이 아니게 된 것을 보았습니다. 



덩굴나무는 정점이 N개이고 간선이 M개인 그래프로 모델링할 수 있습니다. 각 정점에는 아름다운 정도인 w_i가 매겨져 있습니다. 

덩굴나무의 아름다움은 덩굴나무에 있는 간선의 양 끝 정점의 아름다운 정도를 합한 것의 총합에 해당합니다. 



가영은 덩굴나무의 간선을 몇 개 잘라내어 이 그래프를 트리로 만들려고 합니다. 



가영이 만든 트리의 아름다운 정도의 최댓값은 얼마가 될 지 구하는 프로그램을 작성하세요.


예제 입력1

3 3
1 2 3
1 2
2 3
3 1

예제 출력1

9

예제 입력2

5 10
1 2 3 4 5
1 2
2 3
3 4
4 5
1 3
2 4
3 5
1 4
2 5
1 5

예제 출력2

30


입력값 설명

첫 번째 줄에 정점의 개수 N과 간선의 개수 M이 공백으로 구분되어 주어집니다.
(2 ≤ N ≤ 100, N-1 ≤ M ≤ min(N(N-1)/2, 200))
두 번째 줄에 각 정점의 아름다운 정도인 w_i가 공백으로 구분되어 N개가 주어집니다.
i번째 정수는 i번 정점의 아름다움을 의미합니다. (1 ≤ w_i ≤ 1,000)
이후 M개의 줄에 걸쳐 자연수 a_i, b_i가 공백으로 구분되어 주어집니다.
이는 a_i와 b_i를 잇는 간선이 존재함을 의미합니다. (1 ≤ a_i, b_i ≤ N, a_i ≠ b_i)
여기서 동일한 간선이 두 번 이상 주어지지 않음이 보장됩니다.

출력값 설명

첫 번째 줄에 덩굴나무의 간선을 잘라내어 트리 모양으로 만들었을 때 아름다운 정도의 최댓값을 출력합니다.
'''
import sys 

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

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

def kruskal_max_spanning_tree(n, edges):
    # 간선을 가중치 기준으로 내림차순 정렬
    edges.sort(key=lambda x: x[2], reverse=True)
    uf = UnionFind(n)
    max_beauty = 0

    for u, v, weight in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            max_beauty += weight

    return max_beauty

def main():
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    M = int(data[1])
    
    beauty = list(map(int, data[2:N+2]))
    edges = []
    
    index = N+2
    for _ in range(M):
        u = int(data[index]) - 1
        v = int(data[index+1]) - 1
        weight = beauty[u] + beauty[v]
        edges.append((u, v, weight))
        index += 2
    
    result = kruskal_max_spanning_tree(N, edges)
    print(result)

if __name__ == "__main__":
    main()
