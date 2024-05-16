'''
민규는 화장실 바닥을 바라보고 있었습니다. 
바닥은 격자판 모양이었고, 계속해서 바라보다 보니 이런 생각이 들었습니다.

세로 크기가 N이고, 가로 크기가 M인 격자판을 이웃한 격자는 같은 색으로 칠하지 않으면서 서로 다른 세 가지 색으로 칠하면 칠할 수 있는 경우의 수는 몇 개가 될까?

이때 이웃한 격자란 한 변을 공유하는 두 격자를 의미합니다.

격자의 크기가 주어질 때, 
이웃한 격자는 같은 색으로 칠하지 않으면서 격자를 서로 다른 세 가지 색으로 칠할 수 있는 경우의 수를 출력하는 프로그램을 작성하세요.
------------------------------------------------------------------------
[입력값 설명]
『첫째 줄에 자연수 N, M이 공백으로 구분되어 주어집니다.(1 ≤ N, M ≤ 5)』

[출력값 설명]
『이웃한 격자는 같은 색으로 칠하지 않으면서 격자를 서로 다른 네 가지 색으로 칠할 수 있는 경우의 수를 출력합니다.』
------------------------------------------------------------------------
예제 입력1
2 2

예제 출력1
18

예제 입력2
2 3

예제 출력2
54
'''
# -*- coding: utf-8 -*-
import sys
input = sys.stdin.readline

# 현재 칸 색칠하고 다음 칸 반환하기
def painting(y, x, c):
    board[y][x] = c # c로 채워준다(c 색으로 칠해준다)
    # 다음 칸으로 이동해줘야 함 (x+1, 만약 M까지 갔으면 다음 줄로)
    ny, nx = y, x+1
    if nx == M:
        nx = 0
        ny += 1
    return ny, nx

def dfs(y, x):
    global answer
    # 1~3까지 색 순차적으로 칠하기
    for c in range(1, 4):
        if (y == 0) and (x == 0): # 0, 0 좌표라면
            ny, nx = painting(y, x, c)
            # 만약 마지막 줄을 넘기면 board 다 채운거니까 answer를 더해주자
            if ny == N: answer += 1
            # 그거 아니면 걍 dfs 계속 돌리기
            else: dfs(ny, nx)
        elif (y == 0): # y = 0 이라면 
            if (board[y][x-1] != c): # 좌의 값만 체크하기
                ny, nx = painting(y, x, c)
                # 만약 마지막 줄을 넘기면 board 다 채운거니까 answer를 더해주자
                if ny == N: answer += 1
                # 그거 아니면 걍 dfs 계속 돌리기
                else: dfs(ny, nx)
        elif (x == 0): # x = 0 이라면 
            if (board[y-1][x] != c): # 상의 값만 체크하기
                ny, nx = painting(y, x, c)
                # 만약 마지막 줄을 넘기면 board 다 채운거니까 answer를 더해주자
                if ny == N: answer += 1
                # 그거 아니면 걍 dfs 계속 돌리기
                else: dfs(ny, nx)
        # y도 0이 아니고, x도 0이 아니면 그냥 상, 좌 전부 체크 바로 가자
        elif (board[y-1][x] != c) and (board[y][x-1] != c): # 상, 좌 가 전부 현재 값이랑 다를 때
            ny, nx = painting(y, x, c)
            # 만약 마지막 줄을 넘기면 board 다 채운거니까 answer를 더해주자
            if ny == N: answer += 1
            # 그거 아니면 걍 dfs 계속 돌리기
            else: dfs(ny, nx)

if __name__ == "__main__":
    N, M = map(int, input().split())
    board = [[0] * M for _ in range(N)]
    
    answer = 0
    # y, x for문으로 모든 칸을 1부터 체크해가면서 채워넣기
    # 마지막에 채워넣은 칸부터 하나씩 다른 색으로 바꾸면서 경우의 수들 체크
    # 1~3 (3가지 색)을 순차적으로 채우면 visited를 안 써도 되고,
    # dfs 알고리즘으로 하면 마지막 부분만 바꾸고 진행하는게 가능

    dfs(0, 0)
    print(answer)