"""
현민은 재수 끝에 우주경찰대학교에 입학하였고, 마침내 졸업하게 되었습니다.
결과적으로 발령을 받게 되어 첫 번째 임무를 맡게 되었습니다. 
그 임무란 바로 세기의 도둑 재우를 포획하는 임무입니다.

재우는 일직선 상의 우주 공간에 숨어 있습니다. 
일직선 상의 우주 공간은 위치 N으로 표시할 수 있으며 현민은 현재 K 위치에 있습니다. 
현민은 워프 기술을 이용해 재우를 가장 빠르게 포획하고자 합니다.

현민의 위치를 X라고 했을 때, 
현민은 워프 기술을 이용해서 (X + 3), (X - 1), (X * 2)의 위치 중 한 곳으로 이동할 수 있습니다. 
이 때 재우를 잡기 위한 최소 워프 횟수를 구하는 프로그램을 작성하세요.

예를 들어 현민의 위치가 20이고, 재우의 위치가 89라고 했을 때 최소 워프 횟수는 (20, 40, 43, 86, 89)로 4번이 될 것입니다.

예제 입력1
20 89

예제 출력1
4

예제 입력2
47898 5783

예제 출력2
42115

입력값 설명
첫 번째 줄에 현민이 있는 위치 K와 재우가 있는 위치 N이 주어집니다. (0 <= K, N <= 100,000)

출력값 설명
현민이 재우를 포획하기 위한 최소 워프 횟수를 구합니다.

"""

# -*- coding: utf-8 -*-
import sys
sys.setrecursionlimit(10**7)
import math


def dfs(visited, k, x, cnt): 
    visited[k] = cnt
    # print(k)
    # 종료 조건
    # 앞섰을 경우 거리만큼 빼서 넣고 종료
    # 같을 경우 바로 종료료
    if cnt > visited[x]:
        return
    if k == x:
        if visited[x] > cnt:
            visited[k] = cnt
    elif k > x:
        # print(k-x+cnt)
        if visited[x] > k-x+cnt:
            visited[x] = k-x+cnt
    else: # 작을 경우 미리 값 비교해서 visited보다 작을 경우에 다시 dfs
        if k*2 < 100001 and visited[k*2] > cnt+1:
            # print(k*2)
            dfs(visited, k*2, x, cnt+1)
        if k > 0 and visited[k-1] > cnt+1:
            dfs(visited, k-1, x, cnt+1)
        if k+3 < 100000 and visited[k+3] > cnt+1:
            dfs(visited, k+3, x, cnt+1)


if __name__ == "__main__":
    k, x = map(int, input().split())
    INF = int(1e9)
    visited = [INF]*100001
    # 모든 visited 선언 후 최대거리로 넣어두기
    # 값 비교하면서 visited가 작을 경우 탐색하는 dfs
    dfs(visited, k, x, 0)
    
    print(visited[x])