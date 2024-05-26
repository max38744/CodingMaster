'''
N개의 정점과 M개의 양방향 간선으로 이루어진 그래프가 주어집니다.

정점에는 1번부터 N번까지 번호가 붙어있습니다. 

또한, 정점마다 가중치가 부여되어 있습니다. 

어떤 정점 하나를 선택하고 해당 정점의 가중치를 1 높일 때마다 비용이 1만큼 발생합니다.



그래프의 모든 이웃한 정점 간 가중치 차이를 K 이하가 되도록 만들기 위해 필요한 최소 비용을 구하는 프로그램을 작성하세요.


예제 입력1

3 3 5
1
10
20
1 2
2 3
1 3

예제 출력1

19

예제 입력2

5 4 1
10
20
30
40
50
1 2
3 2
3 4
4 5

예제 출력2

90


입력값 설명

첫째 줄에 정점의 개수 N, 간선의 개수 M, 가중치 차이 K가 공백으로 구분되어 주어집니다. (2 ≤ N ≤ 50, 1 ≤ M ≤ 200, 1 ≤ K ≤ 100)

이어서 N개의 줄에 걸쳐 i번 정점의 가중치를 의미하는 양의 정수 s가 주어집니다. (1 ≤ s ≤ 1,000)

이어서 M개의 줄에 걸쳐 간선의 정보를 의미하는 양의 정수 u, v가 주어집니다.
이는 u번 정점과 v번 정점을 연결하는 간선이 존재함을 의미합니다.
즉, u번 정점과 v번 정점이 이웃합니다.

출력값 설명

그래프의 모든 이웃한 정점 간 가중치 차이를 K 이하가 되도록 만들기 위해 필요한 최소 비용을 출력합니다.
'''

import sys
input = sys.stdin.readline

def min_weights(N, M, K, weights, edges):
    total_cost = 0
    changes = True
    # 조정이 필요 없을 때까지 반복
    while changes:
        changes = False
        for a, b in edges:
            # 정점 a와 b 간의 가중치 차이 계산
            weight_diff = abs(weights[a-1] - weights[b-1])
            # 차이가 K 이상인 경우 조정해서 비용 계산
            if weight_diff > K:
                cost = weight_diff - K
                total_cost += cost
                changes = True
                # 두 정점의 가중치를 조정
                if weights[a-1] < weights[b-1]:
                    weights[a-1] += cost
                else:
                    weights[b-1] += cost
    return total_cost

if __name__ == "__main__":
    N, M, K = map(int, input().split())
    weights = [int(input()) for _ in range(N)]
    edges = [tuple(map(int, input().split())) for _ in range(M)]

    cost = min_weights(N, M, K, weights, edges)
    print(cost)
