'''
준하는 10 x 10 크기의 격자를 가지고 있습니다. 이 격자에는 0부터 9까지의 정수가 하나 씩 쓰여져 있습니다.
이 격자에서 하나의 정육면체를 만들 수 있는 전개도를 잘라내려고 합니다. 만들어진 정육면체에 쓰인 수의 합이 최대가 되도록 전개도를 잘라내려고 할 때, 그 수들의 합을 출력하는 프로그램을 작성하세요.
정육면체 전개도는 아래와 같이 다양한 모양으로 나타날 수 있습니다.

예제 입력1
0 0 0 0 0 0 0 0 0 0
0 0 0 1 0 0 0 0 0 0
0 0 1 1 1 0 0 0 0 0
0 0 0 1 0 0 0 0 0 0
0 0 0 1 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0

예제 출력1
6

예제 입력2
8 5 8 4 7 4 5 3 2 0
8 1 8 8 2 3 5 1 2 8
5 7 7 6 1 1 6 1 0 3
5 7 8 8 8 7 2 4 1 0
9 8 7 7 5 1 2 2 1 1
4 6 2 0 3 5 7 6 7 7
5 0 5 7 8 5 0 5 0 6
5 0 6 9 9 9 4 4 6 1
6 6 7 9 4 5 3 7 5 0
9 9 7 2 5 7 4 7 7 4

예제 출력2
51

입력값 설명
10줄에 걸쳐 격자에 쓰인 수가 줄당 10개씩 주어집니다.
격자에 쓰인 수는 모두 0 이상 9 이하의 정수입니다.

출력값 설명
격자에서 전개도를 적절히 잘라내어 그 전개도로 정육면체를 만들었을 때, 정육면체에 쓰인 수의 합의 최대값을 출력합니다.
'''
# -*- coding: utf-8 -*-
import sys


def main():
    grid = [[] for _ in range(10)]
    for i in range(10):
        grid[i] = list(map(int, input().split()))
    
    casing(grid)
    
def casing(grid):
    
    c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    c12, c13, c14, c15, c16, c17 = 0, 0, 0, 0, 0, 0
    for i in range(10):
        for j in range(10):
            c1 = max(c1, case1(grid, i, j))
            c2 = max(c2, case2(grid, i, j))
            c3 = max(c3, case3(grid, i, j))
            c4 = max(c4, case4(grid, i, j))
            c5 = max(c5, case5(grid, i, j))
            c6 = max(c6, case6(grid, i, j))
            c7 = max(c7, case7(grid, i, j))
            c8 = max(c8, case8(grid, i, j))
            c9 = max(c9, case9(grid, i, j))
            c10 = max(c10, case10(grid, i, j))
            c11 = max(c11, case11(grid, i, j))
            c12 = max(c12, case12(grid, i, j))
            c13 = max(c13, case13(grid, i, j))
            c14 = max(c14, case14(grid, i, j))
            c15 = max(c15, case15(grid, i, j))
            c16 = max(c16, case16(grid, i, j))
            c17 = max(c17, case17(grid, i, j))

            
    # print(c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17)
    print(max(c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17))
    
def case1(grid, i, j): # 누운 십자모양(첫째줄)
    result = 0
    alpha = 0
    if i > 7 or j > 6:
        return result
    else:
        result += sum(grid[i+1][j:j+4])
        for x in range(4):
            for y in range(4):
                tmp = (grid[i][j+x] + grid[i+2][j+y])
                alpha = max(alpha, tmp)
    return result + alpha

def case2(grid, i, j): # 선 십자모양
    result = 0
    alpha = 0
    if i > 6 or j > 7:
        return result
    else:
##        result += sum(grid[i:i+4][j+1]) 요래 안되네
        result += (grid[i][j+1]+ grid[i+1][j+1] + grid[i+2][j+1]+ grid[i+3][j+1])
        for x in range(4):
            for y in range(4):
                tmp = (grid[i+x][j] + grid[i+y][j+2])
                alpha = max(alpha, tmp)
    return result + alpha

def case3(grid, i, j): # 가장 긴 줄이 3개(누움, 2개짜리 블럭 우하단)
    result = 0
    alpha = 0
    if i > 7 or j > 6:
        return result
    else:
        result += (sum(grid[i+1][j:j+3]) + grid[i+2][j+2] + grid[i+2][j+3])
        for x in range(3):
            alpha = max(alpha, grid[i][j+x])
    return result + alpha

def case4(grid, i, j): # 가장 긴 줄이 3개(누움, 2개짜리 블럭 우상단)
    result = 0
    alpha = 0
    if i > 7 or j > 6:
        return result
    else:
        result += (sum(grid[i+1][j:j+3]) + grid[i][j+2] + grid[i][j+3])
        for x in range(3):
            alpha = max(alpha, grid[i+2][j+x])
    return result + alpha

def case5(grid, i, j): # 가장 긴 줄이 3개(누움, 2개짜리 블럭 좌하단)
    result = 0
    alpha = 0
    if i > 7 or j > 6:
        return result
    else:
        result += (sum(grid[i+1][j+1:j+4]) + grid[i+2][j] + grid[i+2][j+1])
        for x in range(3):
            alpha = max(alpha, grid[i][j+1+x])
    return result + alpha

def case6(grid, i, j): # 가장 긴 줄이 3개(누움, 2개짜리 블럭 좌상단)
    result = 0
    alpha = 0
    if i > 7 or j > 6:
        return result
    else:
        result += (sum(grid[i+1][j+1:j+4]) + grid[i][j] + grid[i][j+1])
        for x in range(3):
            alpha = max(alpha, grid[i+2][j+1+x])
    return result + alpha

def case7(grid, i, j): # 가장 긴 줄이 3개(섬, 2개짜리 블럭 좌상단)
    result = 0
    alpha = 0
    if i > 6 or j > 7:
        return result
    else:
        result += (grid[i+1][j+1] + grid[i+2][j+1] + grid[i+3][j+1])
        result += (grid[i][j] + grid[i+1][j])
        for x in range(3):
            alpha = max(alpha, grid[i+1+x][j+2])
    return result + alpha

def case8(grid, i, j): # 가장 긴 줄이 3개(섬, 2개짜리 블럭 좌하단)
    result = 0
    alpha = 0
    if i > 6 or j > 7:
        return result
    else:
        result += (grid[i][j+1] + grid[i+1][j+1] + grid[i+2][j+1])
        result += (grid[i+2][j] + grid[i+3][j])
        for x in range(3):
            alpha = max(alpha, grid[i+x][j+2])
    return result + alpha

def case9(grid, i, j): # 가장 긴 줄이 3개(섬, 2개짜리 블럭 우상단)
    result = 0
    alpha = 0
    if i > 6 or j > 7:
        return result
    else:
        result += (grid[i+1][j+1] + grid[i+2][j+1] + grid[i+3][j+1])
        result += (grid[i][j+2] + grid[i+1][j+2])
        for x in range(3):
            alpha = max(alpha, grid[i+1+x][j])
    return result + alpha

def case10(grid, i, j): # 가장 긴 줄이 3개(섬, 2개짜리 블럭 우하단)
    result = 0
    alpha = 0
    if i > 6 or j > 7:
        return result
    else:
        result += (grid[i][j+1] + grid[i+1][j+1] + grid[i+2][j+1])
        result += (grid[i+2][j+2] + grid[i+3][j+2])
        for x in range(3):
            alpha = max(alpha, grid[i+x][j])
    return result + alpha

def case11(grid, i, j): # 전개도 좌하단 지렁이모양(누움, 왼쪽 보는 중)
    result = 0
    alpha = 0
    if i > 8 or j > 5:
        return result
    else:
        result += (grid[i][j] + grid[i][j+1]+ grid[i][j+2])
        result += (grid[i+1][j+2] + grid[i][j+3]+ grid[i][j+4])
    return result

def case12(grid, i, j): # 전개도 좌하단 지렁이모양(누움, 오른쪽 보는 중)
    result = 0
    alpha = 0
    if i > 8 or j > 5:
        return result
    else:
        result += (grid[i][j+2] + grid[i][j+3]+ grid[i][j+4])
        result += (grid[i+1][j] + grid[i+1][j+1]+ grid[i+1][j+2])
    return result

def case13(grid, i, j): # 전개도 좌하단 지렁이모양(섬, 왼쪽 보는 중)
    result = 0
    alpha = 0
    if i > 5 or j > 8:
        return result
    else:
        result += (grid[i][j] + grid[i+1][j]+ grid[i+2][j])
        result += (grid[i+2][j+1] + grid[i+3][j+1]+ grid[i+4][j+1])
    return result

def case14(grid, i, j): # 전개도 좌하단 지렁이모양(섬, 오른쪽 보는 중)
    result = 0
    alpha = 0
    if i > 5 or j > 8:
        return result
    else:
        result += (grid[i][j+1] + grid[i+1][j+1]+ grid[i+2][j+1])
        result += (grid[i+2][j] + grid[i+3][j]+ grid[i+4][j])
##        if i == 0 and j == 3:
##            print('asd')
##            print(grid[i][j+1], grid[i+1][j+1], grid[i+2][j+1])
##            print(grid[i+2][j], grid[i+3][j], grid[i+4][j])
    return result

def case15(grid, i, j): # 전개도 마지막
    result = 0
    alpha = 0
    if i > 7 or j > 6:
        return result
    else:
        result += (grid[i][j] + grid[i][j+1])
        result += (grid[i+1][j+1] + grid[i+1][j+2])
        result += (grid[i+2][j+2] + grid[i+2][j+3])
    return result

def case16(grid, i, j): # 전개도 마지막 좌우 반전
    result = 0
    alpha = 0
    if i > 7 or j > 6:
        return result
    else:
        result += (grid[i+2][j] + grid[i+2][j+1])
        result += (grid[i+1][j+1] + grid[i+1][j+2])
        result += (grid[i][j+2] + grid[i][j+3])
    return result

def case17(grid, i, j): # 전개도 마지막 섬
    result = 0
    alpha = 0
    if i > 6 or j > 7:
        return result
    else:
        result += (grid[i][j] + grid[i+1][j])
        result += (grid[i+1][j+1] + grid[i+2][j+1])
        result += (grid[i+2][j+2] + grid[i+3][j+2])
    return result

def case17(grid, i, j): # 전개도 마지막 섬 좌우 반전
    result = 0
    alpha = 0
    if i > 6 or j > 7:
        return result
    else:
        result += (grid[i+2][j] + grid[i+3][j])
        result += (grid[i+1][j+1] + grid[i+2][j+1])
        result += (grid[i][j+2] + grid[i+1][j+2])
    return result

    
if __name__ == "__main__":
    main()

