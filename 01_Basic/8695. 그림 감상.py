'''
하준은 그림 감상이 취미입니다.
하준은 독특한 취향을 가지고 있기 때문에,
그림들 중에서도 4 × 4 크기의 O, X 문자로만 이루어진 그림만을 감상합니다.

하준은 그림을 감상할 때, 
그림에 2 × 2 크기의 X로만 이루어진 영역이 있는지를 중점적으로 봅니다. 
그런데, 하준은 딱 한 번 그림의 O 하나를 X로 바꿀 수 있는 마법의 붓을 얻었습니다.

하준은 이 붓을 최대 한 번 이용한 후 주어진 그림에 2 × 2 크기의 X로만 이루어진 영역이 있을 수 있는지 궁금해졌습니다.
이를 구해주는 프로그램을 작성하세요.

예제 입력1
OXOO
XXXX
OOOX
OOOO
예제 출력1
yes

예제 입력2
OXOO
XOXX
OOOO
XXXX
예제 출력2
no


입력값 설명
4 × 4 그림이 4줄에 걸쳐서 주어집니다.
그림은 항상 대문자 O와 대문자 X로만 이루어져 있습니다.
출력값 설명
하준이가 마법의 붓을 최대 한 번 이용한 후 주어진 그림에 2 × 2 크기의 X로만 이루어진 영역이 있을 수 있다면 yes, 아니면 no를 출력합니다. 답은 무조건 소문자로만 출력해야 함에 유의하세요.
'''

# -*- coding: utf-8 -*-
import sys

input = sys.stdin.readline

def o2x(draw):
    
    # X가 3개 있으면 yes return or no
    # 행(0,1,2) / 열(0,1,2) 축을 돌면서 9번만 확인하면 끝
    for i in range(3):
        for j in range(3):
            cnt = 0 #X의 개수
            if draw[i][j] == 'X': cnt += 1
            if draw[i][j+1] == 'X': cnt += 1
            if draw[i+1][j] == 'X': cnt += 1
            if draw[i+1][j+1] == 'X': cnt += 1
            if cnt >= 3: # cnt가 3이상일 경우 yes 반환
                return print('yes')
               
    return print('no') # for문이 끝났지만 반환이 안됐으면 no 반환

draw = [input().rstrip() for i in range(4)]

o2x(draw)
