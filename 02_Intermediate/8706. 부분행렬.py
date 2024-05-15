'''
부분 행렬이란 주어진 행렬의 일부 열과 일부 행을 지워서 만들어 낸 더 작은 행렬을 말합니다. 
정수로만 이루어진 행렬과 정수 X가 주어졌을 때, 성분의 합이 X와 같은 부분행렬이 존재하는지 알아내는 프로그램을 작성하세요.

예제 입력1
2 2 5
7 -2
1 0

예제 출력1
YES

예제 입력2
3 3 2
-5 4 1
3 4 -3
5 -1 6

예제 출력2
NO

입력값 설명
첫째 줄에 행렬의 크기 행과 열의 개수를 나타내는 N, M과 X가 공백으로 구분되어 주어집니다. (1 ≤ N, M ≤ 4, -1000 ≤ X ≤ 1000)
둘째 줄부터 N줄에 걸쳐, 행렬이 주어집니다. 행렬의 각 원소는 절대값이 1000이하인 정수입니다.

출력값 설명
성분의 합이 X와 같은 부분행렬이 존재하면 YES, 그렇지 않으면 NO를 출력합니다.
'''

# -*- coding: utf-8 -*-
import sys

    
def div(matrix, x, y): # 매트릭스 쪼개기
    # -5 4 1        -5        -5 4         -5 4 1        (0, 0) 인덱스 기준
    # 3 4 -3  ->         ->          ->              
    # 5 -1 6
    #                |  
    #                v
    #             -5         -5 4           -5 4 1
    #              3      ->   3 4     ->     3 4 -3    
    # 
    
    results = []
    for i in range(y, len(matrix)): # 2 3 4
        for j in range(x, len(matrix[0])):
            result = []
            for ii in range(y, i+1):
                for jj in range(x, j+1):
                    # print(matrix[ii][jj], end=' ')
                    result.append(matrix[ii][jj])
            results.append(sum(result))
    return results
        
if __name__ == "__main__":

    # 조건으로 매트릭스 구성
    n, m, x = map(int, input().split())
    
    matrix = []
    for i in range(n):
        r = list(map(int, input().split()))
        matrix.append(r)
        
    
    results = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
        
            # 정답 배열에 저장
            result = div(matrix, i, j) # matrix의 시작 인덱스를 기준으로 매트릭스 쪼개서 더하기
            for r in result: 
                results.append(r)
                
    # print(results)
    
    if x in results:
        print('YES')
    else:
        print('NO')
    