'''
너비가 W, 높이가 H인 평면에 한 변의 길이가 1인 정육면체 주사위가 있습니다.
여러분은 쿼리에 따라 이 주사위를 굴려야 합니다. 

주사위가 매번 구를 때마다 주사위와 맞닿는 바닥에는 그 주사위의 바닥에 있는 숫자가 찍히게 됩니다. 
이때, 주사위를 굴리기 전에는 주사위의 바닥면이 평면에 맞닿습니다.
어떤 바닥면에 두 번 이상 지나가는 경우에는 맨 마지막으로 맞닿은 면으로 갱신됩니다. 

주사위를 굴릴 때는 한 칸씩 구르는 방향으로 이동하면서 구르게 되지만 
주어진 평면을 벗어나는 움직임일 경우 제자리에서 구르게 됩니다. 
제자리에서 구른 이후에는 바닥면과 맞닿은 주사위면으로 갱신됩니다. 

평면의 너비와 높이, 주사위의 최초 상태, 주사위를 굴린 방법이 주어졌을때,
주사위를 굴린 후 평면에 찍혀있을 숫자를 알아내는 프로그램을 작성하세요. 

예제 입력1
3 3
0 1
1 2 3 4 5 6
3
1 2 3

예제 출력1
0 0 0
6 1 0
6 2 0

예제 입력2
1 1
0 0
10 8 6 4 2 1
1
2

예제 출력2
8


입력값 설명
첫 번째 줄에 평면의 너비를 의미하는 정수 W와 높이를 의미하는 H가 주어집니다. (1 ≤ W, H ≤ 10)
두 번째 줄에 주사위의 위치를 의미하는 정수 X, Y가 주어집니다.
이는 평면의 (0, 0)으로부터 동쪽으로 X칸, 남쪽으로 Y칸 떨어져있음을 의미합니다. (0 ≤ X < W, 0 ≤ Y < H)
세 번째 줄에 100 이하의 자연수가 6개 주어집니다.
첫 번째 정수부터 차례로 주사위의 동쪽면, 남쪽면, 서쪽면, 북쪽면, 위쪽면, 바닥면에 쓰인 숫자를 의미합니다.
네 번째 줄에 주사위를 굴린 횟수 N이 주어집니다. (1 ≤ N ≤ 50)
다섯 번째 줄에 주사위를 굴린 방법을 의미하는 4 이하의 자연수가 공백으로 구분되어 N개 주어집니다.
1은 동쪽, 2는 남쪽, 3은 서쪽, 4는 북쪽을 의미합니다.

출력값 설명
N개의 줄에 걸쳐서 각각 정수 M개를 공백으로 구분하여 출력합니다.
y번째 줄, x번째 정수는 평면의 (0, 0)으로부터
남쪽으로 y칸, 동쪽으로 x칸 떨어진 위치에 쓰인 정수를 의미합니다.
만약 주사위가 가지 않아서 아무것도 쓰여있지 않은 위치에는 0을 대신 출력합니다.
'''


# -*- coding: utf-8 -*-
import sys
import numpy as np

input = sys.stdin.readline

def next_dice(dice, rule):
    new_dice = dice.copy()
    if rule == 1:
        new_dice[0] = dice[4]
        new_dice[2] = dice[5]
        new_dice[4] = dice[2]
        new_dice[5] = dice[0]
    elif rule == 2:
        new_dice[1] = dice[4]
        new_dice[3] = dice[5]
        new_dice[4] = dice[3]
        new_dice[5] = dice[1]
    elif rule == 3:
        new_dice[0] = dice[5]
        new_dice[2] = dice[4]
        new_dice[4] = dice[0]
        new_dice[5] = dice[2]
    elif rule == 4:
        new_dice[1] = dice[5]
        new_dice[3] = dice[4]
        new_dice[4] = dice[1]
        new_dice[5] = dice[3]    
    
    return new_dice

def move(answer, x, y, dice, rule):
    # dice update
    dice = next_dice(dice, rule)
    
    # x,y update
    if rule == 1:
        if x+1 != answer.shape[1]:
            x += 1
    if rule == 2:
        if y+1 != answer.shape[0]:
            y += 1
    if rule == 3:
        if x-1 != -1:
            x -= 1
    if rule == 4:
        if y-1 != -1:
            y -= 1
    
    # answer update
    answer[y][x] = dice[-1]

    return answer, x, y, dice
    

def status(W, H, x, y, dice, N, rule):
    
    answer = np.zeros(H*W, dtype=int).reshape((H,W))
    answer[y][x] = dice[-1]

    for i in range(N):
        answer, x, y, dice = move(answer, x, y, dice, rule[i])
    
    
    return answer

W, H = map(int, input().split())
x, y = map(int, input().split())
dice = list(map(int, input().split()))
N = int(input())
rule = list(map(int, input().split()))

answer = status(W, H, x, y, dice, N, rule)
for i in answer:
    print(*i)
