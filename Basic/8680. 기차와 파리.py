'''
X킬로미터 떨어진 철로에 양쪽 끝에 두 대의 기차가 시속 Y킬로미터의 속도로 서로를 향해 출발했습니다.
이 기차 사이에는 시속 Z킬로미터의 속도로 기차 사이를 왔다 갔다 하는 파리가 한 마리 있는데,
둘 중 한 기차의 방향으로 날다가 기차와 부딪히면 즉시 반대 방향으로 날기 시작합니다.
두 기차가 충돌할 때까지 파리가 이동한 거리를 출력하는 프로그램을 작성하세요.
------------------------------------------------------------------------
[입력값 설명]
『첫째 줄에 X, Y, Z가 공백으로 구분되어 주어집니다. (1 ≤ X, Y, Z ≤ 1,000)』

[출력값 설명]
『기차가 충돌할 때까지 파리가 이동한 거리를 킬로미터 단위로 출력합니다. 소수점은 버립니다.』
------------------------------------------------------------------------
예제 입력1
200 50 75

예제 출력1
150

예제 입력2
123 2 10

예제 출력2
307
'''
# -*- coding: utf-8 -*-
import sys
input = sys.stdin.readline
# 기차가 충돌사고날 것 같다면 선로 변경을 해주세요~
if __name__ == "__main__":
    # X : 현재 떨어져있는 거리 / Y : 두 기차의 속도 / Z : 파리의 속도
    X, Y, Z = map(int, input().split())
    # 파리가 총 이동한 거리
    answer = 0
    # 파리가 방향 틀기 전에 이동한 거리
    distance = 0
    
    # 기차 2대가 Y의 속도로 이동 -> 거리는 Y*2 만큼 줄어듦
    # 거리가 1 줄어들 때 파리 이동 거리 : Z/(Y*2)
    fly = Z/(Y*2)
    
    # 파리가 날 수 있는 시간 => X만큼이니깐 fly*X
    print(int(fly*X))