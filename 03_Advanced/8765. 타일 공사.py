'''
길동은 자신의 집의 M x 1 크기의 복도를 1 x 1 크기의 타일로 채우려고 합니다.
각 타일의 색은 1 이상 N 이하의 번호가 매겨져 있습니다. 현재 길동은 i색의 타일을 a_i개 가지고 있습니다.
길동은 인접한 타일의 색의 차이가 1이면 타일의 색의 조화가 맞지 않는다고 생각합니다.
따라서 인접한 타일의 색의 차이가 1이 되지 않도록 타일을 채우려고 합니다.
또한, 길동은 좋아하는 색 k가 있는데 이 색의 타일을 p개 이상은 꼭 넣으려고 합니다.

예를 들어, 복도의 크기가 3이고, 길동이 색 1, 색 2, 색 3의 타일을 각각 3개씩 가지고 있다고 합시다.
그리고 길동이 좋아하는 타일 색은 1이고 개수는 2개 이상 넣고 싶어한다고 합시다.
만약 복도를 "1 2 2" 로 채우게 된다면 첫번째 타일과 두번째 타일의 색의 차가 1이기 때문에 이 경우는 불가능한 경우입니다.
만약 "1 3 3" 으로 채운다면 인접한 타일의 색의 차이가 1이 나는 경우는 없지만,
길동이 좋아하는 색이 1인 타일의 개수가 2개 이상 사용되지 않았기 때문에 이 경우도 불가능한 경우입니다.
만약 "1 1 3" 으로 채운다면 모든 조건을 만족하면서 타일을 채울 수 있기 때문에 이 경우는 가능한 경우입니다.

길동은 타일을 채우기 전에 먼저 타일이 채워질 수 있는 경우를 모두 따져보고 제일 마음에 드는 것으로 선택하려 합니다.
하지만 경우의 수가 너무 많기 때문에, 길동을 위해 타일이 채워질 수 있는 방법의 수를 계산하여 알려주어야 합니다.
타일이 적절하게 채워질 수 있는 방법의 수를 출력하는 프로그램을 작성하세요.
------------------------------------------------------------------------
[입력값 설명]
『입력은 3줄로 주어집니다.

첫 번째 줄에는 타일의 색의 수 N(1 ≤ N ≤ 3)과 복도의 크기 M(1 ≤ M ≤ 10)이 주어집니다.
두 번째 줄에는 1번 색 타일부터 N번 색 타일까지 타일의 개수 a_i(1 ≤ a_i ≤ 10)가 차례대로 주어집니다.
세 번째 줄에는 길동이가 좋아하는 타일의 색 k(1 ≤ k ≤ N)와 개수 p(0 ≤ p ≤ M)가 주어집니다.』

[출력값 설명]
『복도를 채울 수 있는 타일의 경우의 수를 출력합니다. (길동이의 조건을 만족시키지 못하면 경우의 수가 0이므로 0을 출력합니다.)』
------------------------------------------------------------------------
예제 입력1
3 3
2 2 2
2 0

예제 출력1
6

예제 입력2
3 10
10 10 10
3 5

예제 출력2
638
'''
# -*- coding: utf-8 -*-
import sys
input = sys.stdin.readline
from math import factorial

if __name__ == "__main__":
    N, M = map(int, input().split())
    tiles = list(map(int, input().split()))
    fav, num = map(int, input().split())
    fav -= 1 # index 넘버로 쓰려고
    
    answer = 0
    # N이 2 이하라면,
    if N <= 2:
        # 좋아하는 타일이 있다
        if num > 0:
            # 그 타일로만 채울 수 있으면 1
            if tiles[fav] >= M: answer = 1
            else: answer = 0 # 안되면 0
        # 좋아하는 타일이 없다 (num=0)
        else:
            # 보유 타일 수가 M보다 크면 1씩 더해주기
            for t in tiles:
                if t >= M: answer += 1
    else:
        # 색차이 생각하면 2로 채워넣는건 단 한가지 경우 뿐이다.
        if (fav == 1) and (num > 0):
            if tiles[fav] >= M: answer = 1
        # 색 상관 없이 num이 0이라면, (테케 1,3,5,7이 여기 해당)
        elif num == 0:
            # 일단 2로 채우는 1가지 더해주자
            if tiles[1] >= M: answer += 1
            # 1이랑 3으로 타일 까는 경우의 수
            if (tiles[0]+tiles[2]) >= M:
                # 1번 색타일 최대 갯수에서 1개씩 줄여보고
                for one in range(min(tiles[0], M), max(M-tiles[2]-1, -1), -1):
                    three = M-one
                    answer += factorial(M)//(factorial(one)*factorial(three))
        # 남은 경우는 num이 0이 아니면서, fav가 1, 3 둘 중 하나 (테케 2가 여기 해당)
        else:
            if (tiles[0]+tiles[2]) >= M:
                # 좋아하는게 1이면 다른 타일은 3이 되고,
                if fav == 0: an = 2
                # 반대면 그 반대로 설정
                elif fav == 2: an = 0
                # 좋아하는거 기준으로 세어보자
                for f in range(min(tiles[fav], M), max(M-tiles[an]-1, num-1), -1):
                    a = M-f
                    answer += factorial(M)//(factorial(f)*factorial(a))
    print(answer)
    
######################################################################################

# # permutations 쓰는 경우 2, 3 timeout 남
# # 2번 테케는 마지막 경우(1, 3 으로만 만들어서 체크하기)
# # 3번 테케는 바로 위의 num==0 인 경우
# from itertools import permutations

# if __name__ == "__main__":
#     N, M = map(int, input().split())
#     tiles = list(map(int, input().split()))
#     fav, num = map(int, input().split())
#     fav -= 1 # index 넘버로 쓰려고
    
#     answer = 0
#     # N이 2 이하라면,
#     if N <= 2:
#         # 좋아하는 타일이 있다
#         if num > 0:
#             # 그 타일로만 채울 수 있으면 1
#             if tiles[fav] >= M: answer = 1
#             else: answer = 0 # 안되면 0
#         # 좋아하는 타일이 없다 (num=0)
#         else:
#             # 보유 타일 수가 M보다 크면 1씩 더해주기
#             for t in tiles:
#                 if t >= M: answer += 1
#     else:
#         # 색차이 생각하면 2로 채워넣는건 단 한가지 경우 뿐이다.
#         if (fav == 1) and (num > 0):
#             if tiles[fav] >= M: answer = 1
#         # 색 상관 없이 num이 0이라면,
#         elif num == 0:
#             # 일단 2로 채우는 1가지 더해주자
#             if tiles[1] >= M: answer += 1
#             # 1이랑 3으로 타일 까는 경우의 수
#             t = [0]*tiles[0] + [2]*tiles[2]
#             if len(t) >= M:
#                 answer += len(set(permutations(t, M)))
#         # 남은 경우는 num이 0이 아니면서, fav가 1, 3 둘 중 하나
#         else:
#             t = [0]*tiles[0] + [2]*tiles[2]
#             if len(t) >= M:
#                 for tile in set(permutations(t, M)):
#                     # 만들어진 경우의 수에서, 좋아하는 타일 수가 num보다 많으면 +1
#                     if tile.count(fav) >= num: answer +=1
#     print(answer)
