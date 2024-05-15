'''
깊이 우선 탐색이란 그래프를 탐색(또는 순회)하는 방법 중 하나입니다. 

깊이 우선 탐색은 다음과 같은 방식으로 이루어집니다. 

1. 정점을 하나 정하여 방문하였다고 표시합니다. 
2. 이 정점과 간선으로 연결된 다른 정점에 대하여, 
2-1. 이미 방문했던 정점이라면 무시합니다. 
2-2. 아직 방문하지 않은 정점이라면 그 정점부터 다시 1을 적용합니다. 

이를 의사코드로 작성하면 다음과 같게 됩니다. 

function DFS(V, E, C) {  // V : 정점의 집합, E : 간선의 집합, C : 현재 방문할 정점
  visited[C] = true  // 현재 정점을 방문하였다고 표시
  for each x in E(C) {   // E(C) : C와 인접한 정점
    if (!visited[x]) DFS(V, E, x)  // 아직 방문하지 않은 정점이면 해당 정점부터 깊이 우선 탐색
  }
}

방향성과 가중치가 없는 그래프가 주어졌을 때 정점 1에서부터 깊이 우선 탐색을 수행하는 프로그램을 작성하세요. 

탐색은 인접한 정점 중에서 정점번호가 작은 정점부터 수행합니다. 
정점의 개수가 N개일 때 각 정점의 번호는 1부터 N까지입니다.

예제 입력1
3 0
예제 출력1
1

예제 입력2
5 3
1 4
2 3
4 5
예제 출력2
1 4 5

입력값 설명
첫째 줄에 정점의 개수 N과 간선의 개수 M이 입력됩니다. (1≤N, 0≤M≤1,000)
둘째 줄부터 M + 1번째 줄까지 정수 A와 B가 입력됩니다. (1 ≤ A, B ≤ 1,000) 이 때 각 줄은 A와 B가 서로 연결되었음을 의미합니다.

출력값 설명
정점 1에서 깊이 우선 탐색을 수행한 결과, 거쳐간 노드를 공백으로 구분하여 출력합니다.(1도 출력합니다.)

function DFS(V, E, C) {  // V : 정점의 집합, E : 간선의 집합, C : 현재 방문할 정점

  visited[C] = true  // 현재 정점을 방문하였다고 표시

  for each x in E(C) {   // E(C) : C와 인접한 정점

    if (!visited[x]) DFS(V, E, x)  // 아직 방문하지 않은 정점이면 해당 정점부터 깊이 우선 탐색

  }

}
'''


# 1-try
'''
# -*- coding: utf-8 -*-
import sys
import pandas as pd

def DFS(data):
    print(data)
    answer = []
    C = 1
    
    if len(data)==0:
        answer.append(C)
        return print(answer[0])
    
    while(True):
        answer.append(C)
        C = data.loc[data['start']==C,'end'].item()
        print(C)

        if answer.count(C) != 0:
            break

    return print(answer)

N, M = map(int, sys.stdin.readline().split())
data = pd.DataFrame([list(map(int,sys.stdin.readline().split())) for i in range(M)], columns=['start','end'])
    
DFS(data)
'''

# 2-try
'''
# -*- coding: utf-8 -*-
import sys

def DFS(data):
    if len(data) == 0:
        return print('1')
    
    answer = ''
    C = 1 # 현재 위치한 정점
    V = [] # 출발 정점의 집합
    E = [] # 도착 정점의 집합
    
    data.sort()
    for v,e in data:
        V.append(v) 
        E.append(e) 
    
    while(True): 
        answer += str(C) + ' '
        temp = C
        C = E[V.index(C)]
        del(E[V.index(temp)])
        del(V[V.index(temp)])
        
        if V.count(C) == 0:
            answer += str(C)
            break

    return print(answer)

N, M = map(int, sys.stdin.readline().split())
data = [list(map(int,sys.stdin.readline().split())) for i in range(M)]
    
DFS(data)
'''

# 3-try
# -*- coding: utf-8 -*-
import sys
import numpy as np

def DFS(N, data):
    if len(data) == 0:
        return print('1')
    
    answer = ''
    C = 1 # 현재 위치한 정점
    V = []
    for i in range(N):
        V.append(False) # 방문한 정점
    E_s = [] # 출발 정점의 집합
    E_e = [] # 도착 정점의 집합
    
    data.sort() # 정점번호가 작은 정점부터 수행위하여 sort
    for start,end in data:
        E_s.append(start) 
        E_e.append(end) 
    
    while(True): 
        answer += str(C) + ' '
        V[C-1] = True # 현재 정점을 방문하였다고 표시
        C = E_e[E_s.index(C)]
        if V[C-1] == True: # 방문한 정점이면 끝
            break
        if E_s.count(C) == 0: # 이어진 간선 없으면 끝
            answer += str(C)
            break

    return print(answer)

N, M = map(int, sys.stdin.readline().split())
data = [list(map(int,sys.stdin.readline().split())) for i in range(M)]
    
DFS(N, data)