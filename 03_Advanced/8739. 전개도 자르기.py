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
import numpy as np

input = sys.stdin.readline


cubes = [
        [[1,0,0,0],
         [1,1,1,1],
         [1,0,0,0]],
        
        [[1,0,0,0],
         [1,1,1,1],
         [0,1,0,0]],
        
        [[1,0,0,0],
         [1,1,1,1],
         [0,0,1,0]],
        
        [[1,0,0,0],
         [1,1,1,1],
         [0,0,0,1]],
        
        [[0,1,0,0],
         [1,1,1,1],
         [0,1,0,0]],
        
        [[0,1,0,0],
         [1,1,1,1],
         [0,0,1,0]],
        
        [[1,0,0,0],
         [1,1,1,0],
         [0,0,1,1]],
        
        [[0,1,0,0],
         [1,1,1,0],
         [0,0,1,1]],
        
        [[0,0,1,0],
         [1,1,1,0],
         [0,0,1,1]],
        
        [[1,1,0,0],
         [0,1,1,0],
         [0,0,1,1]],
        
        [[1,1,1,0,0],
         [0,0,1,1,1]],
]


# Function to rotate the array by 90 degrees
def rotate_90(array):
    return np.rot90(array, k=1)

# Function to flip the array horizontally
def flip_horizontal(array):
    return np.fliplr(array)

# Function to generate all rotations of a 3D cube
def generate_rotations(cube):
    rotations = []
    
    cube_array = np.array(cube)
    rotations.append(cube_array.tolist())
    cube_array = flip_horizontal(cube_array)
    rotations.append(cube_array.tolist())
    
    for _ in range(3):
        cube_array = rotate_90(cube_array)
        rotations.append(cube_array.tolist())
        cube_array = flip_horizontal(cube_array)
        rotations.append(cube_array.tolist())

    return rotations

# Function to perform convolution
def convolve(board, cube):
    max_overlap = 0
    board_height = len(board)
    board_width = len(board[0])
    cube_height = len(cube)
    cube_width = len(cube[0])
    
    for i in range(board_height - cube_height + 1):
        for j in range(board_width - cube_width + 1):
            overlap_sum = 0
            for m in range(cube_height):
                for n in range(cube_width):
                    overlap_sum += board[i + m][j + n] * cube[m][n]
            max_overlap = max(max_overlap, overlap_sum)
    
    return max_overlap


# # Main execution
# board = [
#     [8, 5, 8, 4, 7, 4, 5, 3, 2, 0],
#     [8, 1, 8, 8, 2, 3, 5, 1, 2, 8],
#     [5, 7, 7, 6, 1, 1, 6, 1, 0, 3],
#     [5, 7, 8, 8, 8, 7, 2, 4, 1, 0],
#     [9, 8, 7, 7, 5, 1, 2, 2, 1, 1],
#     [4, 6, 2, 0, 3, 5, 7, 6, 7, 7],
#     [5, 0, 5, 7, 8, 5, 0, 5, 0, 6],
#     [5, 0, 6, 9, 9, 9, 4, 4, 6, 1],
#     [6, 6, 7, 9, 4, 5, 3, 7, 5, 0],
#     [9, 9, 7, 2, 5, 7, 4, 7, 7, 4]
# ]

# Get input
board = [list(map(int,input().split())) for _ in range(10)]

max_global_overlap = 0
for cube in cubes:
    rotated_cubes = generate_rotations(cube)
    for rotated_cube in rotated_cubes:
        max_overlap = convolve(board, rotated_cube)
        max_global_overlap = max(max_global_overlap, max_overlap)

print(max_global_overlap)

