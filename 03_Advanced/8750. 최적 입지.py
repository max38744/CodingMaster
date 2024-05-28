'''
동근은 N×N 격자판 마을에 하나의 마을회관을 만들려고 합니다.
그러기 위해 회관과 마을의 모든 주택까지의 거리 합이 최소가 되는 지점인 최적 위치를 찾으려고 합니다.
최적 위치에 이미 주택이 존재한다면 그 주택을 마을회관으로 만들고 없다면 새로운 건물을 짓습니다.

격자판에서 어떤 주택과 회관까지의 거리는 그 주택에서 한 칸씩 상하좌우로 이동할 때 회관으로 가기 위한 최소 이동 횟수로 정의됩니다.

HHRR
RRRG
RRRR
RRRR

R: 도로
H: 주택
G: 회관

예를 들어 1행 1열과 1행 2열에만 주택이 있는 4×4 격자 마을을 생각해 봅시다.
만약 위와 같이 2행 4열에 회관 G를 지었다면 회관까지의 거리는 왼쪽 주택부터 4, 3입니다.
한편 1행 1열의 주택을 마을회관으로 만든다면 회관과 마을의 모든 주택까지의 거리 합이 최소가 됩니다.

격자 마을의 정보가 주어질 때, 최적 위치의 행과 열을 출력하는 프로그램을 작성하세요.
최적 위치가 여러 개일 경우 행이 가장 작은 위치를 출력해주세요.
행이 같은 최적 위치가 여러개일 경우 열이 가장 작은 최적 위치를 출력해 주세요.
------------------------------------------------------------------------
[입력값 설명]
『첫째 줄에 자연수 N이 주어집니다.(2 ≤ N ≤ 100)
둘째 줄부터 N개의 줄에 걸쳐 N×N 크기의 격자 마을의 정보가 주어집니다.
마을의 정보는 R, H 로만 구성되며 각 문자의 의미는 다음과 같습니다.
R: 도로
H: 주택
입력으로 주어지는 격자 마을에는 적어도 2개의 주택이 존재함이 보장됩니다.』

[출력값 설명]
『최적 위치의 행과 열을 공백으로 구분하여 순서대로 출력합니다.
최적 위치가 여러 개일 경우 행이 가장 작은 위치를 출력해 주세요.
행이 같은 최적 위치가 여러 개일 경우 열이 가장 작은 최적 위치를 출력해 주세요.』
------------------------------------------------------------------------
예제 입력1
4
HHRR
RRRR
RRRR
RRRR

예제 출력1
1 1

예제 입력2
4
HRRR
RRRR
RRRR
RRRH

예제 출력2
1 1
'''
# -*- coding: utf-8 -*-
import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    HY = []
    HX = []
    for y in range(N):
        line = input().rstrip()
        if 'H' in line:
            l, i = line, 0
            while True:
                try:
                  n = l.index('H')
                  HX.append(n+i)
                  HY.append(y)
                  i = n+i+1
                  l = line[i:]
                except:
                    break
    HX.sort()
    
    if len(HY)%2==0: ansY = HY[len(HY)//2-1]
    else: ansY = HY[len(HY)//2]
    if len(HX)%2==0: ansX = HX[len(HX)//2-1]
    else: ansX = HX[len(HX)//2]
    
    print(ansY+1, ansX+1)

#################################################################

# # GPT 식 풀이 - 통과됨
# def find_optimal_point(grid):
#     H_positions = []

#     # H의 위치 수집
#     for i in range(N):
#         for j in range(N):
#             if grid[i][j] == 'H':
#                 H_positions.append((i, j))

#     if not H_positions:
#         return None  # H가 없는 경우

#     # x 좌표 중앙값 계산
#     H_positions.sort(key=lambda x: x[0])
#     median_x_indices = [H_positions[len(H_positions) // 2][0]]
#     if len(H_positions) % 2 == 0:
#         median_x_indices.append(H_positions[len(H_positions) // 2 - 1][0])

#     # y 좌표 중앙값 계산
#     H_positions.sort(key=lambda x: x[1])
#     median_y_indices = [H_positions[len(H_positions) // 2][1]]
#     if len(H_positions) % 2 == 0:
#         median_y_indices.append(H_positions[len(H_positions) // 2 - 1][1])

#     # 가능한 중앙값 조합 중에서 가장 작은 좌표 선택
#     possible_points = [(x, y) for x in median_x_indices for y in median_y_indices]
#     y, x = min(possible_points)

#     return y+1, x+1

# if __name__ == "__main__":
#     N = int(input())
#     board = [list(input().rstrip()) for _ in range(N)]
    
#     print(*find_optimal_point(board))

#################################################################

# # 2, 5, 7 안됨 / 마지막에 +1 안하면 2는 통과됨 (5, 7은 안됨)
# if __name__ == "__main__":
#     N = int(input())
#     HY = []
#     HX = []
#     for y in range(N):
#         line = input().rstrip()
#         if 'H' in line:
#             l, i = line, 0
#             while True:
#                 try:
#                   n = l.index('H')
#                   HX.append(n+i)
#                   HY.append(y)
#                   i = n+i+1
#                   l = line[i:]
#                 except:
#                     break
#     print((max(HY)+min(HY))//2+1,(max(HX)+min(HX))//2+1)
#     위와 동일한 결과
#     print(sum(HY)//len(HY)+1, sum(HX)//len(HX)+1)
