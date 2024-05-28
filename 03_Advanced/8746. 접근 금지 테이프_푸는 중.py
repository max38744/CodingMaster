'''
공무원인 동욱은 건설 공사 중 문화 유적이 발견되었다는 연락을 받았습니다.
동욱은 정밀 발굴을 위해 유적이 발굴될 만한 지점을 모두 볼록다각형 모양의 접근금지 테이프로 감쌌습니다.
그러나 동욱은 자주 덤벙 되기 때문에 모든 유적을 감쌌는지 확인할 필요가 있습니다.
이때 유적이 볼록다각형 외곽선 상에는 있지 않으면서 볼록다각형의 내부에 포함될 때 유적을 감싼 것으로 판단합니다.
볼록다각형 모양의 접근 금지 테이프가 모든 유적 발굴 예상지역을 포함하고 있는지를 출력하는 프로그램을 작성하세요.

예제 입력1
3 3
-1 -1 4 -1 -1 4
0 0 0 1 1 0

예제 출력1
YES

예제 입력2
3 1
-1 -1 4 -1 -1 4
3 0

예제 출력2
NO

입력값 설명
첫째 줄에 볼록다각형 모양의 접근 금지 테이프의 꼭짓점 수를 의미하는 자연수 N과 유적 발굴 예상 지역의 수 M이 공백으로 구분되어 주어집니다.(3 ≤ N ≤ 100, 1 ≤ K ≤ 100)
둘째 줄에는 볼록다각형을 구성하는 N 개 점의 좌표가 공백으로 구분된 2N개의 정수로 주어집니다.
각 점의 좌표는 X Y 형식으로 공백으로 구분되어 주어집니다.
각 점은 반시계 방향 순서로 주어집니다.
세 번째 줄에는 유적 발굴 예상지역 M 개 점의 좌표가 공백으로 구분된 2M개의 정수로 주어집니다.
각 점의 좌표는 X Y 형식으로 공백으로 구분되어 주어집니다.
주어지는 모든 점의 좌표는 다르며,
x좌표와 y좌표의 범위는 절댓값 10,000을 넘지 않습니다.

출력값 설명
볼록다각형 모양의 접근 금지 테이프가 모든 유적 발굴 예상지역을 포함하고 있으면 "YES", 그렇지 않으면 "NO"를 출력합니다.
'''

# -*- coding: utf-8 -*-
import numpy as np
from math import sin


def check_vector(tape_lines, historic_sites):

    tape_v1 = np.array(tape_lines[0])
    tape_v2 = np.array(tape_lines[1])
    # vector 만들기
    tape_vector  = tape_v2 - tape_v1
    hist_vector = historic_sites - tape_v1
    # 외적
    outer_product = np.cross(tape_vector,hist_vector)
    # norm 값( 벡터 거리 값 구하기)
    tape_norm = np.linalg.norm(tape_vector)
    hist_norm = np.linalg.norm(hist_vector)
    

    # sin 값 / A,B 외적의 크기 = A의 크기 * B의 크기 * sin 값
    sin_tape_hist = outer_product/(tape_norm*hist_norm)
    if round(sin_tape_hist,10) > 0:
        return 1
    else:
        return 0
    
    
def main():
    import sys
    input = sys.stdin.read
    
    data = input().split()
    
    N = int(data[0])
    M = int(data[1])
    
    tape_lines = []
    historic_sites = []
    
    index = 2
    for _ in range(N):
        u = int(data[index])
        v = int(data[index+1])
        tape_lines.append([u,v])
        index += 2 
    
    for _ in range(M):
        u = int(data[index])
        v = int(data[index+1])
        historic_sites.append([u,v])
        index += 2 
    
    # N = 3
    # M = 1
    # tape_lines = [[-1,-1], [4,-1], [-1,4]]
    # historic_sites = [[3,0]]
    
    
    for i in range(M):
        check = check_vector([tape_lines[-1],tape_lines[0]], historic_sites[i])
        if check == 0:
            return print('NO')
        for j in range(N-1):
            check = check_vector(tape_lines[j:j+2], historic_sites[i])
            if check == 0:
                return print('NO')
    
    return print('YES')
    
if __name__ == "__main__":
    main()