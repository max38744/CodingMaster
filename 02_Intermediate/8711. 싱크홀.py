"""
길에 N개의 싱크홀이 생겼습니다.
이 싱크홀을 그대로 놔두면 위험하기 때문에, 
준하는 가지고 있는 길이가 K인 널빤지를 이용해 임시로 보수하려고 합니다. 

싱크홀의 위치와 널빤지의 길이가 주어질 때, 
싱크홀을 모두 덮기 위한 널빤지의 최소 개수를 출력하는 프로그램을 작성하세요.

예제 입력1
5 3
5 3 8 10 1

예제 출력1
3

예제 입력2
2 1
4 5

예제 출력2
2

입력값 설명
첫째 줄에 N과 K가 공백으로 구분되어 주어집니다. (1 ≤ N ≤ 100, 1 ≤ K ≤ 100,000)
둘째 줄에 싱크홀의 위치 A_i가 공백으로 구분되어 주어집니다. (1 ≤ A_i ≤ 100,000)

출력값 설명
싱크홀을 모두 덮기 위한 널빤지의 최소 개수를 출력합니다.
"""

# -*- coding: utf-8 -*-
import sys

def main():
    pass
    
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr = sorted(arr)
    # print(arr)
    
    i = 0
    idx = 0
    cnt = 1
    # init
    
    while True: # 시작점에 널빤지를 놓고 널빤지의 마지막 위치 다음의 위치로 넘어가서 다시 놓기
        if idx+i == len(arr):
            break
        
        # print('checking', arr[idx], arr[idx+i])
        if arr[idx] + k > arr[idx+i]:
            i+=1
        else:
            idx += i
            cnt+=1
            # print(cnt, idx)
            i = 0
    
    print(cnt)
            
if __name__ == "__main__":
    main()