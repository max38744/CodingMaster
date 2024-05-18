'''
철수는 시간이 날 때마다 친구들과 "점프 게임"을 플레이합니다.

점프 게임의 맵은 일렬로 늘어선 N개의 칸으로 구성되고, 각 칸에는 1번부터 N번까지 번호가 붙어있습니다.
게임은 1번 칸에서 시작하고, 점프를 통해 N번 칸에 도착하면 게임이 종료됩니다.

점프 게임의 구체적인 규칙은 다음과 같습니다.
- 번호가 낮은 칸에서 번호가 높은 칸으로만 점프할 수 있습니다.
- 각 칸에는 점프 제한을 의미하는 양의 정수 K가 쓰여있습니다.
  어떤 칸의 점프 제한이 K이면, 해당 칸으로부터 1칸 이상 K칸 이하만큼 떨어져있는 칸으로만 점프 가능합니다.

각 칸에서 얼마만큼 점프하느냐에 따라 점프 게임이 종료되는 방법이 달라집니다.
철수는 점프 게임이 종료되는 경우의 수가 궁금해졌습니다. 각 칸의 점프 제한이 주어졌을 때, 점프 게임이 종료되는 경우의 수를 구하는 프로그램을 작성하세요.

예를 들어 N = 3, 각 칸의 점프 제한이 2 1 2라고 가정하겠습니다. 점프 게임이 종료되는 경우는 다음 2가지입니다.
'1번 - 2번 - 3번'
'1번 - 3번'

N = 5, 점프 제한이 3 2 2 1 3일 때 점프 게임이 종료되는 경우는 다음 6가지입니다.
'1번 - 2번 - 3번 - 4번 - 5번'
'1번 - 2번 - 3번 - 5번'
'1번 - 2번 - 4번 - 5번'
'1번 - 3번 - 4번 - 5번'
'1번 - 3번 - 5번'
'1번 - 4번 - 5번'
------------------------------------------------------------------------
[입력값 설명]
『첫째 줄에 칸의 개수를 의미하는 양의 정수 N이 주어집니다. (2 ≤ N ≤ 5,000)
둘째 줄에 i번 칸의 점프 제한을 의미하는 양의 정수 a_i가 공백으로 구분되어 주어집니다. (1 ≤ a_i ≤ 5,000)』

[출력값 설명]
『첫째 줄에 점프 게임이 종료되는 경우의 수를 출력합니다. 단,출력값이 매우 커질 수 있으므로 정답을 1,000,000,007 로 나눈 나머지를 출력합니다.』
------------------------------------------------------------------------
예제 입력1
3
2 1 2

예제 출력1
2

예제 입력2
5
3 2 2 1 3

예제 출력2
6
'''
# -*- coding: utf-8 -*-
import sys
input = sys.stdin.readline

# 7 timeout 될 때도 있음(6이 왜 된건지 이해 못함)
# 7은 29s에 성공 찍혀서 가끔 timeout 뜸, 될 때까지 시도?
import numpy as np

if __name__ == "__main__":
    N = int(input())
    a = list(map(int, input().split()))

    answer = np.zeros(N)
    answer[0] = 1
    for i in range(N):
        M = (i+1)+a[i]
        if M < N:
            l = np.array([0]*(i+1) + [answer[i]]*a[i] + [0]*(N-M))
        else:
            l = np.array([0]*(i+1) + [answer[i]]*(N-(i+1)))
        answer += l
        if np.max(answer) > 1000000007: answer %= 1000000007
    print(int(answer[-1])%1000000007)

##########################################

# # 6,7 Failed (7은 24s 정도 걸림)
# import numpy as np

# if __name__ == "__main__":
#     N = int(input())
#     a = list(map(int, input().split()))

#     answer = np.zeros(N)
#     answer[0] = 1
#     for i in range(N):
#         M = (i+1)+a[i]
#         if M < N:
#             l = np.array([0]*(i+1) + [answer[i]]*a[i] + [0]*(N-M))
#         else:
#             l = np.array([0]*(i+1) + [answer[i]]*(N-(i+1)))
#         answer += l
#         if np.max(answer) > 1000000007: answer -= 1000000007
#     print(int(answer[-1])%1000000007)

##########################################

# # 5,6,7 Failed (7은 24s 정도 걸림)
# import numpy as np

# if __name__ == "__main__":
#     N = int(input())
#     a = list(map(int, input().split()))

#     answer = np.zeros(N)
#     answer[0] = 1
#     for i in range(N):
#         M = (i+1)+a[i]
#         if M < N:
#             l = np.array([0]*(i+1) + [answer[i]]*a[i] + [0]*(N-M))
#         else:
#             l = np.array([0]*(i+1) + [answer[i]]*(N-(i+1)))
#         answer += l
#     print(int(answer[-1])%1000000007)

##########################################

# # 4~7 timeout
# from collections import deque

# if __name__ == "__main__":
#     N = int(input())
#     a = list(map(int, input().split()))

#     answer = 0
#     # Q 생성하고, 스타트 위치인 0 값 넣기
#     Q = deque()
#     Q.append(0)
#     while Q:
#         now = Q.popleft()
#         # 현위치가 목적지라면 굳이 밑에 연산들 안 함
#         if now == N-1:
#             answer += 1
#             continue
#         # 최대 갈 수 있는 인덱스 값 저장
#         M = min(N, (now+1)+a[now])
#         # 현위치에서 갈 수 있는데까지 전부 저장
#         for i in range(now+1, M):
#             Q.append(i)
#     print(answer%1000000007)

##########################################

# # 4, 5 timeout / 6, 7 Failed

# # 현재 위치를 알려줄 n
# def dfs(n):
#     global answer
#     if n == N-1:
#         answer += 1
#         return
#     for i in range(n+1, n+1+a[n]):
#         dfs(i)

# if __name__ == "__main__":
#     N = int(input())
#     a = list(map(int, input().split()))

#     for i in range(N):
#         if i+a[i] >= N: a[i] = N-i-1

#     answer = 0
#     dfs(0)
#     print(answer%1000000007)

##########################################

# # 3~7 까지 Failed

# # 현재 위치를 알려줄 n
# def dfs(n):
#     global answer
#     if n == N-1:
#         answer += 1
#         return
#     for i in range(n+1, n+a[n]+1):
#         dfs(i)

# if __name__ == "__main__":
#     N = int(input())
#     a = list(map(int, input().split()))

#     answer = 0
#     dfs(0)
#     print(answer%1000000007)