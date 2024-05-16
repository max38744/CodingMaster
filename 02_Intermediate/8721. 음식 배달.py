'''
철수는 식당 A에서 배달 아르바이트를 시작했습니다.
식당 A는 도시에서 소문난 맛집입니다.
한 번에 한 집씩만 배달하게 되면 밀려오는 주문 속도를 감당할 수 없습니다.
따라서 철수는 한 번에 K개의 집에 음식을 배달합니다.
즉, K개의 집이 주문한 음식을 모두 들고 A에서 출발하고, 모든 음식을 배달하면 A로 돌아갑니다.

식당 A가 위치한 도시는 격자판 모양입니다.
격자판의 왼쪽에서부터 x번째, 위에서부터 y번재 칸을 (x, y)로 표현합니다.
격자판의 한 칸은 하나의 집을 의미합니다.
단, (1, 1)에는 집 대신 식당 A가 위치합니다.

철수는 현재 위치한 칸에서 상하좌우로 인접한 칸으로 이동할 수 있습니다.
단, 격자판의 밖으로 벗어날 수 없습니다.
철수가 한 칸 이동할 때마다 1분이 소요됩니다.

예를 들어 철수가 현재 위치한 칸이 (2, 3)이라고 가정하겠습니다.
철수는 (1, 3), (2, 2), (2, 4), (3, 3) 중 하나의 칸으로 이동할 수 있습니다.

음식을 주문한 집의 좌표 N개가 주어졌을 때,
철수가 A에서 출발해 K개의 집에 음식을 배달하고 다시 A로 돌아오는 데 걸리는 최소 시간을 구하는 프로그램을 작성하세요.
------------------------------------------------------------------------
[입력값 설명]
『첫째 줄에 음식을 주문한 집의 개수 N과 철수가 한 번에 배달하는 집의 개수 K가 공백으로 구분되어 주어집니다. (1 ≤ K ≤ N ≤ 8)
이어서 N개의 줄에 걸쳐 음식을 주문한 집의 좌표가 주어집니다.
각 줄에는 양의 정수 x, y가 공백으로 구분되어 주어집니다.
이는 집의 좌표가 (x, y)임을 의미합니다. (1 ≤ x, y ≤ 10,000)』

[출력값 설명]
『첫째 줄에 철수가 A에서 출발해 K개의 집에 음식을 모두 배달하고 다시 A로 돌아오는 데 걸리는 최소 시간을 출력합니다.』
------------------------------------------------------------------------
예제 입력1
3 2
2 2
3 3
9 9

예제 출력1
8

예제 입력2
2 1
47 64
96 38

예제 출력2
218

예제 입력3
5 3
126 53
38 72
62 18
5 134
24 13

예제 출력3

'''
# -*- coding: utf-8 -*-
import sys
input = sys.stdin.readline

# 방문배열, 현재 위치, 현재까지 걸린 시간
def back_tracking(visit, now, time):
    global answer
    # 현재 집에서 다른 집 방문하는데 걸리는 시간을 저장
    deliTime = [-1] * N
    for i in range(N):
        # 이미 방문한 집은 계산 안 함
        if not visit[i]:
            deliTime[i] = abs(house[i][0]-house[now][0])+abs(house[i][1]-house[now][1])
    # 이제 deliTime을 돌면서 모든 집을 다음에 방문할 집이라 가정(visit==False일 때만)
    for i in range(N):
        if not visit[i]:
            # 시간 계산 먼저 하고
            t = time + deliTime[i]
            # 현재까지 구한 답보다 많이 걸리면 넘김
            if t >= answer: continue
            # 방문 처리를 해주고, 재귀함수로 넘겨준다.
            visit[i] = True
            back_tracking(visit, i, t)
            # 다음 집 방문체크해보려면 현재 방문 체크 했던 위치는 다시 방문 안한걸로 바꿔줌
            visit[i] = False
    # 이미 K 만큼 방문했다면 되돌아가는 것까지 합쳐서 시간 비교
    if sum(visit) == K: answer = min(answer, (time + house[now][2]))

if __name__ == '__main__':
    N, K = map(int, input().split())
    house = []
    for _ in range(N):
        x, y = map(int, input().split())
        # 식당(1, 1)이라 -1씩 해줌
        x, y = x-1, y-1
        # 식당에서 가는데 걸리는 시간
        t = x + y
        house.append([x, y, t])
    # 식당에서 걸리는 시간 순서대로 재배열
    house.sort(key=lambda x: x[2])
    answer = float('inf')
    
    # 백트래킹으로 계산하는게 좋을 듯
    for start in range(N):
        # 우선 방문 여부 작성
        visited = [False] * N
        # 먼저 방문하려는 집은 True
        visited[start] = True
        # 모든 집을 스타트 위치라 생각하고 진행
        back_tracking(visited, start, house[start][2])
    print(answer)

######################################################################

# # 1, 2, 6 제외 전부 Failed

# def deliTime(start):
#     # start 위치 저장
#     now_x, now_y = house[start][0], house[start][1]
#     # start에서 다른 집 이동하는데 걸리는 시간 저장할 배열
#     times = [float('inf')] * N
#     # 다른 집 이동하는데 걸리는 시간 계산
#     for i in range(N):
#         # 이미 방문한 집은 체크 안 함
#         if not visited[i]:
#             times[i] = abs(house[i][0]-now_x)+abs(house[i][1]-now_y)
#     # 최소시간과 해당 집 위치 반환
#     return min(times), times.index(min(times))

# if __name__ == '__main__':
#     N, K = map(int, input().split())
#     house = []
#     for _ in range(N):
#         x, y = map(int, input().split())
#         # 식당(1, 1)이라 -1씩 해줌
#         x, y = x-1, y-1
#         # 식당에서 가는데 걸리는 시간
#         t = x + y
#         house.append([x, y, t])
#     # 식당에서 걸리는 시간 순서대로 재배열
#     house.sort(key=lambda x: x[2])

#     answer = float('inf')
#     for start in range(N-K):
#         # 처음 방문하는 집까지 걸리는 시간
#         time = house[start][2]
#         # 방문한 집을 제외하려는 배열
#         visited = [False] * N
#         visited[start] = True
#         # start 집 방문했으니 K-1 만큼만 돌면 됨
#         for _ in range(K-1):
#             # 계산 하려는데 이미 걸리는 시간이 최대 시간이라면 break
#             if time > answer: break
#             t, start = deliTime(start)
#             # 시간 더하고 방문 체크
#             time += t
#             visited[start] = True
#         # 마지막에 돌아오긴 해야지
#         time += house[start][2]
#         # 걸리는 시간이 이미 오버라면 break
#         if time >= answer: break
#         answer = min(answer, time)
#     print(answer)