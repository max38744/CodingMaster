'''
철수의 마을에는 총 N명의 사람이 존재하고, 각 사람에게는 1번부터 N번까지 번호가 붙어있습니다.
철수는 마을 사람들의 친구 관계를 그래프로 모델링했습니다. 그래프의 정점은 N개이고, 간선은 M개입니다. 각 정점에는 1번부터 N번까지 번호가 붙어있습니다. i번 사람은 i번 정점에 대응합니다. 간선은 양방향입니다.
u번 정점과 v번 정점을 잇는 간선이 존재하는 경우, u번 사람과 v번 사람이 친구임을 의미합니다.

마을의 각 사람은 정확히 하나의 그룹에 속합니다.
u번 정점에서 v번 정점으로 가는 경로가 존재하는 경우, u번 사람과 v번 사람이 같은 그룹에 속함을 의미합니다.
그룹의 ID는 해당 그룹에 포함된 사람들의 번호 중 가장 작은 번호입니다.
마을에 존재하는 그룹 중 가장 많은 사람이 포함된 그룹의 ID를 구하는 프로그램을 작성하세요.

예제 입력1
4 4
1 2
2 3
3 4
4 1

예제 출력1
1

예제 입력2
5 3
2 3
3 4
4 2

예제 출력2
2

입력값 설명
첫째 줄에 N과 M이 공백으로 구분되어 주어집니다. (2 ≤ N ≤ 100, 1 ≤ M ≤ 500)
이어서 M개의 줄에 거쳐 마을 사람들의 친구 관계가 주어집니다. 각 줄에는 양의 정수 u, v가 공백으로 구분되어 주어집니다. 이는 u번 정점과 v번 정점을 잇는 간선이 존재함을 의미합니다. (1 ≤ u, v ≤ N, u ≠ v)
출력값 설명
첫째 줄에 가장 많은 사람이 포함된 그룹의 ID를 출력합니다. 단, 조건을 만족하는 그룹이 여러 개인 경우 그 중 가장 작은 ID를 출력합니다.
'''
'''
# 1st try
# -*- coding: utf-8 -*-
import sys

input = sys.stdin.readline

def gpID(M,data):
    
    group = [set(data[0])]
    
    for u,v in data:
        for j in range(len(group)):
            if (u or v) in group[j]: # 현재 그룹에 속한 것
                group[j].add(u) # 그룹에 추가 (그룹은 set 형식)
                group[j].add(v) # 그룹에 추가
            else: # 또 다른 그룹이 생기는 것
                group.append(set([u, v])) # group(list) 새로운 행 추가(set 형식)

    min_gp = []
    for i in range(len(group)):
        min_gp.append(min(group[i]))
    
    return print(min(min_gp))


# N, M = map(int, input().split())
# data = [list(map(int,input().rsplit())) for _ in range(M)]

# gpID(N,M,data)

N = 5
M = 3
data =  [[1, 2], [2, 3], [4, 5]]
gpID(N,M,data)
'''
'''
# 2nd try
# -*- coding: utf-8 -*-
import sys

input = sys.stdin.readline

def gpID(N,M,data):
    
    E_f = []
    E_n = []
    for u,v in data:
        E_f.append(u)
        E_n.append(v)

    group=[]
    cnt = 0
    while len(E_n) != 0:
        u = E_f[0]
        v = E_n[0]
        
        while (u or v) in (E_f or E_n):
            group[cnt].add(u)
            group[cnt].add(v)
            temp_u = u
            temp_v = v
            
        
        
        while c in E_f:
            group[cnt].add(c)
            temp = c
            c = E_n[E_f.index(temp)]
            E_f.remove(E_f[E_n.index(temp)])
            E_n.remove(temp)
            
        group[cnt].add(c)
        E_f.remove(E_f[E_n.index(c)])
        E_n.remove(c)
        cnt += 1
        
    
    check_gp=[]
    for i in range(len(group)):
        check_gp.append([len(group[i]),min(group[i])])

    check_gp.sort(key=lambda x: (-x[0], x[1]))
    
    return print(check_gp[0][1])


N, M = map(int, input().split())
data = [list(map(int,input().rsplit())) for _ in range(M)]
gpID(N,M,data)
'''
# N = 10
# M = 3
# data =  [[1, 2], [1, 3], [3, 5]]
# gpID(N,M,data)

'''
# 3rd try
# -*- coding: utf-8 -*-
import sys

input = sys.stdin.readline

def gpID(N, M, data):
    parents = [i for i in range(1,N+1)]
    group = [set(data[0])]
    
    for u,v in data:
        for j in range(len(group)):
            if (u or v) in group[j]: # 현재 그룹에 속한 것
                group[j].add(u) # 그룹에 추가 (그룹은 set 형식)
                group[j].add(v) # 그룹에 추가
            else: # 또 다른 그룹이 생기는 것
                group.append(set([u, v])) # group(list) 새로운 행 추가(set 형식)

    min_gp = []
    for i in range(len(group)):
        min_gp.append(min(group[i]))
    
    return print(min(min_gp))


# N, M = map(int, input().split())
# data = [list(map(int,input().rsplit())) for _ in range(M)]

# gpID(N,M,data)

N = 5
M = 3
data =  [[1, 2], [2, 3], [4, 5]]
gpID(N,M,data)
'''


# 4th-try
# -*- coding: utf-8 -*-
import sys

input = sys.stdin.readline


def find(parent, x):
    if parent[x] == x:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, x, y):
    x = find(parent, x)
    y = find(parent, y)

    if x != y:
        parent[max(x, y)] = min(x, y)
    return


def gpID(N, data):
    parent = [i for i in range(N+1)]

    for u, v in data:
        union(parent, u, v)

    max_cnt = 0
    answer = 1
    for i in range(N, 0, -1):
        if parent.count(i) >= max_cnt:
            max_cnt = parent.count(i)
            answer = i

    return answer


N, M = map(int, input().split())
data = [list(map(int, input().rsplit())) for _ in range(M)]

print(gpID(N, data))

# N = 5
# M = 3
# data = [[2, 3], [3, 4], [4, 2]]

# print(gpID(N, data))
