'''
N장의 카드를 섞어주는 기계가 있습니다.
이 기계는 N장의 카드를 섞으면,
i번째 카드를 A_i번째로 옮기는 방법으로 카드를 섞습니다.

A_i는 모두 다르므로,
섞은 다음 같은 위치에 2장 이상의 카드가 있을 수는 없습니다.

초기에 카드는 1부터 N까지 차례대로 배열되어 있습니다.

A_i가 주어질 때, 카드를 K번 섞은 후 카드의 배치를 출력하는 프로그램을 작성하세요.
------------------------------------------------------------------------
[입력값 설명]
『첫째 줄에 N과 K가 공백으로 구분되어 주어집니다. (1 ≤ N ≤ 1,000, 1 ≤ K ≤ 1,000,000,000)
둘째 줄에, A_i가 공백으로 구분되어 주어집니다. (1 ≤ A_i ≤ N, A는 순열)』

[출력값 설명]
『첫째 줄에 카드를 K번 섞은 후 카드의 배치를 공백으로 구분하여 출력합니다.』
------------------------------------------------------------------------
예제 입력1
5 3
2 1 4 5 3

예제 출력1
2 1 3 4 5

예제 입력2
8 20
7 4 6 3 5 1 2 8

예제 출력2
3 1 2 7 5 4 6 8
'''
# -*- coding: utf-8 -*-
import sys
input = sys.stdin.readline
import numpy as np

if __name__ == "__main__":
    N, K = map(int, input().split())
    A = np.array(list(map(int, input(). split()))) - 1

    answer = np.zeros(N)
    for k in range(N):
        visited = [-1]*N
        i = k
        c = 0
        for _ in range(K):
            if visited[i] == 0:
                i = visited.index(K%c)
                break
            visited[i] = c
            i, c = A[i], c + 1
        answer[i] = k
    answer = (answer + 1).astype(int)
    print(*answer)

###############################################################
# # 3~6 timeout
# import numpy as np

# if __name__ == "__main__":
#     N, K = map(int, input().split())
#     A = np.array(list(map(int, input(). split()))) - 1

#     answer = np.zeros(N)
#     for k in range(N):
#         i = k
#         for _ in range(K):
#             i = A[i]
#         answer[i] = k
#     answer += 1
#     answer = answer.astype(int)
#     print(*answer)
