'''
치훈은 생일 선물로 배열 A를 받았습니다.

배열 A의 서로 다른 네 인덱스 i, j, k, l에 대하여,
A_i * A_j = A_k * A_l를 만족하는 i, j, k, l가 존재하는지 출력하는 프로그램을 작성하세요.

A_i는 배열 A의 i번째 원소를 뜻합니다.

예제 입력1
4
1 2 3 6

예제 출력1
YES

예제 입력2
6
56 23 79 81 27 29

예제 출력2
NO

입력값 설명
첫 줄에 N이 주어집니다. (4 ≤ N ≤ 50)
두번째 줄에 길이 N의 배열 A가 공백으로 구분되어 주어집니다. (1 ≤ A_i ≤ 1000)

출력값 설명
존재하면 YES, 아니면 NO를 출력합니다.
'''

# -*- coding: utf-8 -*-
import sys
from itertools import permutations

if __name__ == "__main__":
    
    n = int(input())
    
    arr = list(map(int, input().split()))
    
    p_list = list(permutations(arr, 4))
    
    flag = 0
    for p in p_list:
        i, j, k, l = p
        if i*j == k*l:
            flag = 1
            break
    
    if flag == 1:
        print('YES')
    else:
        print('NO')
    