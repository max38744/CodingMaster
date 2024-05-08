'''
그래프 이론 수업을 듣는 영식은 무향 그래프에 대해 배우고 있습니다.
모든 간선이 방향성을 가지지 않는 그래프를 무향 그래프라고 합니다.
다시 말해, 무향 그래프의 모든 간선은 두 정점을 양방향으로 연결하고 있습니다.

영식의 교수님께서 정점의 수와 간선의 수,
그리고 각 간선이 어떤 두 정점을 잇는지 알려주시곤,
주어진 정보를 바탕으로 그래프를 그림으로 그리는 과제를 내셨습니다. 

모든 일에 계획적으로 임하는 영식은, 
그래프를 무작정 그리지 않고 각 정점이 어떤 정점들과 연결되어 있는지 목록을 작성해보려고 합니다. 
과제로 주어진 무향 그래프의 정보가 주어지면, 각 정점과 연결되어 있는 정점을 모두 출력하는 프로그램을 작성하세요.

예제 입력1

5 5
1 2
2 3
3 4
4 1
5 3
예제 출력1

2 4
1 3
2 4 5
1 3
3
예제 입력2

5 2
2 3
3 5
예제 출력2

no
3
2 5
no
3

입력값 설명

첫 번째 줄에 정점의 개수 N과 간선의 개수 M이 공백을 구분으로 주어집니다. (1 ≤ N, M ≤ 1,000)
두 번째 줄부터 M개의 줄에 각 간선이 연결하는 서로 다른 두 정점의 번호가 공백을 구분으로 주어집니다.
연결하는 두 정점이 같은 간선은 여러번 주어지지 않습니다.
출력값 설명

총 N개의 줄을 출력합니다. i(1 ≤ i ≤ N)번째 줄에는 i번 정점과 간선으로 직접 연결된 정점들의 번호를 오름차순으로 공백으로 구분해 출력합니다. 만약 직접 연결된 정점이 하나도 없다면 대신 no를 출력합니다.
'''

import sys
import numpy as np

def graph(N, data):
    # 1. 간선이 없을 때
    if len(data) == 0: 
        for i in range(N):
            print('no')
        return 
    
    # 2. 간선이 있을 때
    answer = ['no'] * N # 기본 값 no
    
    data.sort() # 정점번호가 작은 정점부터 수행위하여 sort
    for start,end in data:
        if answer[start-1] == 'no':
            answer[start-1] = []
        if answer[end-1] == 'no':
            answer[end-1] = []
        answer[start-1].append(end)
        answer[end-1].append(start)

    for i in range(N):
        if answer[i] != 'no':
            answer[i].sort()
            print(*answer[i])
        else: print(answer[i][:])
        
    return 

N, M = map(int,sys.stdin.readline().split())
data = [list(map(int,sys.stdin.readline().rsplit())) for i in range(M)]

graph(N,data)