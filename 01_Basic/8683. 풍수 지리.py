'''
기성은 풍수지리에 심취해 있습니다. 매일 땅의 기운을 공부한 끝에 엄청난 사실을 깨닫고 말았습니다. 
땅은 N행 M열의 격자판으로 나눌 수 있고, 격자판의 각 칸은 A부터 Z까지 26종류의 기운 중 하나를 내뿜습니다. 
이 땅 위에 바닥이 직사각형 꼴인 건물을 지었을 때, 건물 바닥과 맞닿은 칸이 모두 같은 기운을 내뿜는다면 건물에서 하는 모든 사업이 바닥과 맞닿은 칸의 수만큼 축복받게 됩니다.

첫번째 예시 입력을 봅시다. 2행 1열을 왼쪽 위 꼭짓점, 3행 3열을 오른쪽 아래 꼭짓점으로 하는 영역에 건물을 지으면 B 기운으로부터 6 만큼의 축복을 받을 수 있습니다. 
하지만 1행 3열을 왼쪽 위 꼭짓점, 2행 4열을 오른쪽 아래 꼭짓점으로 하는 영역에 건물을 지으면 여러가지 기운이 섞여 있어 축복을 받을 수 없습니다.

이 놀라운 사실을 깨달은 기성은 어서 땅을 사려고 합니다. 
격자판으로 나눈 땅의 각 칸이 어떤 기운을 내뿜는지 주어지면, 최대 얼마만큼의 축복을 받을 수 있는지 출력하는 프로그램을 작성하세요.


예제 입력1

5 8
AAAAADAA
BBBDDDEE
BBBDDDEE
BBCCDDEE
BBCCCEEF

예제 출력1

8

예제 입력2

3 3
AIV
LEA
IVL

예제 출력2

1


입력값 설명

첫째 줄에 두 정수 N과 M이 공백으로 구분되어 주어집니다. (1 ≤ N ≤ 8, 1 ≤ M ≤ 8)
다음 N개의 줄에 걸쳐 각 줄에 M개의 문자가 주어집니다.
격자판 i행 j열의 칸은 i + 1번째 줄의 j번째 문자와 같은 기운을 내뿜습니다.

출력값 설명

주어진 땅에서 최대 얼마만큼의 축복을 받을 수 있는지 출력합니다.
'''
# -*- coding: utf-8 -*-
import sys
input = sys.stdin.readline

# 자꾸 테케하나 틀려서.. 추가..
# 직사각형 안에 요소들이 전부 같은지 확인 함수수
def is_same_value_area(x, y, width, height, base, ground):
    for i in range(x, x + height):
        for j in range(y, y + width):
            if ground[i][j] != base:
                return False
    return True

# 최대 축복 계산 함수
def calc_bless(x, y, base, ground):
    max_bless = 0
    
    # 현재 위치 (x,y)에서 이동가능한 최대 길이
    max_height = n - x 
    max_width = m - y  

    for height in range(1, max_height + 1):
        for width in range(1, max_width + 1):
            if not is_same_value_area(x, y, width, height, base, ground):
                break
            max_bless = max(max_bless, height * width)  # 최대 축복값 갱신

    return max_bless

n, m = map(int,sys.stdin.readline().split())
ground = [sys.stdin.readline().strip() for _ in range(n)]

max_blessing = 0 
for i in range(n):
    for j in range(m):
        max_blessing = max(max_blessing, calc_bless(i, j, ground[i][j], ground))

print(max_blessing)