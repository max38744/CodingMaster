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
input = sys.stdin.readline
from collections import deque
# git민혁
def bfs(k, x):
    INF = int(1e9)
    visited = [INF]*100001
    # 모든 visited 선언 후 최대거리로 넣어두기    
    
    q = deque([(k, 0)]) # 현재 위치, 워프 횟수
    
    # 값 비교하면서 visited가 작을 경우 탐색하는 bfs
    while q:
        now, warp = q.popleft()
        for i in (now+3, now-1, now*2):
            if 0<=i<=100000 and visited[i] > warp+1:
                visited[i] = warp+1
                q.append([i, warp+1])
    
    return visited[x]

if __name__ == "__main__":
    k, x = map(int, input().split())
    print(bfs(k, x))

#######################################################
    
# 병준
# -*- coding: utf-8 -*-
import sys
input = sys.stdin.readline
from collections import deque

def check_warp(K, N):
    if K >= N:
        return K-N
    else:
        DP = [float('inf')] * (N+5)
        Q = deque()
        Q.append((N, 0))
        while Q:
            now, cnt = Q.popleft()
            if now%2 == 1:
                for n in (now+1, now-3):
                    if (0<=n<=(N+5)) and DP[n] > cnt+1:
                        DP[n] = cnt+1
                        Q.append((n, cnt+1))
            else:
                for n in (now//2, now-3):
                    if (0<=n<=(N+5)) and DP[n] > cnt+1:
                        DP[n] = cnt+1
                        Q.append((n, cnt+1))
            if DP[K] != float('inf'): return DP[K]
        
if __name__ == "__main__":
    K, N = map(int, input().split())
    
    print(check_warp(K, N))
    
#######################################################
    
# # 6, 7 timeout / 근데 그냥 값에다가 넣는거랑 DP 배열 해서 넣는거랑 왜이렇게 시간차 많이나는지 설명점..
# from collections import deque

# if __name__ == "__main__":
#     K, N = map(int, input().split())
#     answer = float('inf')
    
#     Q = deque()
#     Q.append((N, 0))
#     while Q:
#         N, cnt = Q.popleft()
#         if N == K:
#             answer = min(answer, cnt)
#             break
#         elif N < K:
#             answer = min(answer, cnt+(K-N))
#         elif N%2 == 1:
#             Q.append((N+1, cnt+1))
#             Q.append((N-3, cnt+1))
#         else:
#             Q.append((N-3, cnt+1))
#             Q.append((N//2, cnt+1))
    
#     print(answer)
