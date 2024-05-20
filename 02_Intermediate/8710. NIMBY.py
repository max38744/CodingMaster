"""
님비 현상은 "Not In My BackYard"의 약자로, 공공의 이익에는 부합하지만, 자신이 속한 지역에는 이롭지 아니한 일을 반대하는 행동을 뜻합니다.

수직선 위에 N개의 집이 있습니다. 
그 중 한곳을 골라 쓰레기 소각장을 지으려고 합니다. 
공공의 이익이 되는 시설이므로 가까울수록 주민의 만족도가 늘어나지만, 
너무 가까우면 오히려 만족도가 줄어듭니다. 

이를 명확하게 정의하면 다음과 같습니다. 
쓰레기 소각장과 집까지의 거리를 d라고 할 때, 
쓰레기 소각장과 거리가 K이하인 집은 d만큼의 만족도를, 
K초과인 집은 -d만큼의 만족도를 갖게 됩니다.

모든 집의 만족도의 합을 최대화 하기 위한 쓰레기장의 위치를 출력하는 프로그램을 작성하세요.

예제 입력1
5 2
1 3 5 7 8

예제 출력1
5

예제 입력2
5 5
1 3 5 7 8

예제 출력2
3

입력값 설명
첫째 줄에 N과 K가 공백으로 구분되어 주어집니다. (1 ≤ N ≤ 100, 1 ≤ K ≤ 100,000)
이어서 다음 줄에, 수직선 위의 집의 좌표 A_i, N개가 공백으로 구분되어 주어집니다. (1 ≤ A_i ≤ 100,000)

출력값 설명
모든 집의 만족도의 합을 최대화 하기 위한 쓰레기장의 위치를 출력합니다.
만약 그런 위치가 여러개라면, 가장 좌표가 작은 곳을 출력합니다.

"""

# -*- coding: utf-8 -*-
import sys

def nimby(arr, trash, k): # trash 위치를 받아 만족도 합 구하기
    result = 0
    for i in range(len(arr)):
        d = abs(arr[i] - trash)
        if d <= k:
            result += d
        else:
            result -= d
    return result

def main():
    n, k = map(int, input().split())
    
    arr = list(map(int, input().split()))
    result = nimby(arr, arr[0], k)
    idx = arr[0]
    # init
    
    for i in arr: # 모든 trash 위치에 대해 만족도 합 구해서 값 비교
        # print(nimby(arr, i, k), i)
        if result < nimby(arr, i, k):
            result = nimby(arr, i, k)
            idx = i
            
    print(idx)
    
if __name__ == "__main__":
    main()
