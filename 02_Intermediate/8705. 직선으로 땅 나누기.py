"""
끝없이 넓은 평면의 땅이 있습니다. 
직선 울타리 만을 이용해서 N 명에게 나눠줄 땅을 구획하려면 최소 몇 개의 직선이 필요한지 알려주는 프로그램을 작성하세요.

이때 나뉜 땅을 모두 나눠 줄 필요는 없지만, 한 명에게 최소 한 구역의 땅을 나눠주어야 합니다.

예제 입력1
2

예제 출력1
1

예제 입력2
3

예제 출력2
2

입력값 설명
첫째줄에 정수 N(1 ≤ N ≤ 1000) 이 주어집니다.

출력값 설명
N 명에게 나눠주기 위한 땅을 구획하기 위한 직선 울타리의 최소 개수를 출력합니다.
"""

# -*- coding: utf-8 -*-
import sys

def main():
    n = int(input())
    
    lines = 0
    while True:
        if lands(lines) >= n:
            print(lines)
            break
        lines+=1
        
def lands(n): # n개로 만들 수 있는 최대 구역 : n*(n+1) / 2 + 1
    return n*(n+1)/2 + 1
    
if __name__ == "__main__":
    main()
