'''
[문제]

친구들과 술을 거나 하게 마신 한울은 정신을 차리고 보니 밤중에 혼자 길거리에 누워있었습니다.
내일 토익시험을 봐야 하기 때문에 꼭 집에 들어가서 눈을 붙여야 하는 한울은 
이미 시간이 늦었기 때문에 심야 버스를 타고 집에 가야하는 상황입니다.

그 와중에 심야 버스 노선이 궁금해진 한울은 서울 시내의 어느 동네에서 어느 동네까지 노선이 존재하는지 알아보고 싶습니다.

서울의 각 동네를 정점(i, j)로 보았을 때, i에서 j로 가는 버스 노선이 존재하는지 알아보는 프로그램을 작성하세요.

------------------------------------------------------------------------
[입력값 설명]
첫째 줄에 동네의 개수 N (1 ≤ N ≤ 100)이 주어집니다.
둘째 줄부터 N개 줄에는 그래프의 인접 행렬이 주어집니다.
i번째 줄의 j번째 숫자가 1인 경우에는 i에서 j로 가는 버스 노선이 존재한다는 뜻이고, 0인 경우는 없다는 뜻입니다.
i번째 줄의 i번째 숫자는 항상 0입니다.


[출력값 설명]
총 N개의 줄에 걸쳐서 정답을 인접 행렬 형식으로 출력합니다. 
i에서 j로 가는 노선이 있으면 i번째 줄의 j번째 숫자를 1로, 없으면 0으로 출력해야 합니다.

------------------------------------------------------------------------
예제 입력1
4
0 1 0 0
0 0 1 0
0 0 0 1
0 0 0 0

예제 출력1
0 1 1 1
0 0 1 1
0 0 0 1
0 0 0 0

예제 입력2
7
0 1 0 0 0 0 0
1 0 0 0 0 0 0
0 0 0 1 0 0 0
0 0 1 0 1 0 0
0 0 0 1 0 1 0
0 0 0 0 1 0 1
0 0 0 0 0 1 0

예제 출력2
1 1 0 0 0 0 0
1 1 0 0 0 0 0
0 0 1 1 1 1 1
0 0 1 1 1 1 1
0 0 1 1 1 1 1
0 0 1 1 1 1 1
0 0 1 1 1 1 1

'''

# -*- coding: utf-8 -*-
import sys
input = sys.stdin.readline

def floyd_warshall(n, graph):
    # Initialize the reachability matrix with the given graph adjacency matrix
    reach = [[0] * n for _ in range(n)]
    
    # Set the reachability based on the input graph
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                reach[i][j] = 1
    
    # Floyd-Warshall algorithm to update reachability
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if reach[i][k] == 1 and reach[k][j] == 1:
                    reach[i][j] = 1
    
    return reach

if __name__ == "__main__":
    # 입력값 받기
    n = int(input())
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))

    # 경로 계산
    result = floyd_warshall(n, graph)

    # 결과 출력
    for row in result:
        print(' '.join(map(str, row)))
