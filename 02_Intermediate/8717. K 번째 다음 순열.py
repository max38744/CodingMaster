'''
1부터 N까지의 자연수로 이루어진 순열이 있습니다.
이 순열의 사전 순으로 가장 앞서는 순열은 오름차순으로 이루어진 순열이고,
가장 마지막에 오는 순열은 내림차순으로 이루어진 순열입니다.

예를 들어 N이 3인 경우 사전 순으로 나열하면 다음과 같습니다.

1 2 3
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1

이때 순열 (2 3 1)의 사전 순으로 다음 순열은 (3 1 2) 입니다.
또한 순열 (2 3 1)의 사전 순으로 2번째 다음 순열은 (3 2 1)입니다.

대희는 "대희식 순서"를 만들었습니다.
"대희식 순서"란 사전식 순서를 따르면서 다음 규칙 하나를 추가한 것입니다.

사전 순으로 가장 마지막 순열의 다음 순열은 사전 순으로 가장 앞서는 순열이다.

예를 들어 N이 3인 경우
순열 (3 1 2)의 대희식으로 다음 순열은 (3 2 1) 입니다.
순열 (3 1 2)의 대희식으로 2번째 다음 순열은 (1 2 3)입니다.

어떤 순열이 주어질 때 대희식으로 K번째 다음 순열을 출력하는 프로그램을 작성하세요.
------------------------------------------------------------------------
[입력값 설명]
『첫째 줄에 자연수 N과 K가 공백으로 구분되어 주어집니다.(2 ≤ N, K ≤ 1,000)
둘째 줄에 순열이 공백으로 구분되어 주어집니다.』

[출력값 설명]
『어떤 순열이 주어질 때 대희식으로 K번째 다음 순열을 공백으로 구분하여 출력합니다.』
------------------------------------------------------------------------
예제 입력1
3 1
3 2 1

예제 출력1
1 2 3

예제 입력2
4 24
1 2 3 4

예제 출력2
1 2 3 4
'''
# -*- coding: utf-8 -*-
import sys
input = sys.stdin.readline
from math import factorial

def next_permutation(lst):
    # 바꿔야하는 기준이 되는 숫자의 인덱스 flag
    flag = len(lst)-1
    for i in range(len(lst)-2, -1, -1):
        if lst[i+1] < lst[i]: flag = i
        else: break
    # 만약 flag가 가장 첫번째 번호, 즉 가장 마지막 순열이라면
    # 머희식으로 사전 순으로 가장 첫번째로 돌아간다.
    if flag == 0:
        lst.sort()
        return lst
    
    # 전체 순열을 넣어야 하는 수인지 to_visit 배열로 생성
    to_visit = [True] * N
    
    # flag 값 바로 앞의 숫자부터 하나씩 바꿔줘야하고, 그 앞은 안 바꿔도 됨
    result = lst[:flag-1]
    # result 안에 있는 건 사용한 숫자니까 to_visit 에서 False 처리
    for n in result: to_visit[n-1] = False
    
    # flag-1 번째 숫자는 기존 숫자의 +1씩 해서 앞에 없는 숫자를 넣어줘야함
    n = lst[flag-1] # 인덱스 값으로 사용하려고 +1을 안함
    for i in range(n, N):
        # 사용한 적 없는 번호라면
        if to_visit[i]:
            result.append(i+1) # 인덱스 넘버니깐 +1
            to_visit[i] = False # 이제 사용한 번호니깐 False
            break
    
    # to_visited 에서 아직 True 인 값들 작은 숫자부터 차례대로 넣어주기
    for n, check in enumerate(to_visit):
        if check: result.append(n+1)
    
    return result

if __name__ == "__main__":
    N, K = map(int, input().split())
    answer = list(map(int, input().split()))
    
    # 전체 순열의 갯수
    all_cases = factorial(N)
    # K가 전체 순열의 갯수보다 크면, 한바퀴 돌고도 더 도는거니까 나머지만큼만 돌리자
    K %= all_cases
    for _ in range(K): answer = next_permutation(answer)
    
    print(*answer)
    
#########################################################################################

# # 왜인지 4, 5번 timeout, 이 정도면 무한루프에 한번 빠지는건지 체크해봐야 한다.
# from math import factorial

# def next_permutation(lst):
#     # 바꿔야하는 기준이 되는 숫자의 인덱스 flag
#     flag = len(lst)-1
#     for i in range(len(lst)-2, -1, -1):
#         if lst[i+1] < lst[i]: flag = i
#         else: break
#     # 만약 flag가 가장 첫번째 번호, 즉 가장 마지막 순열이라면
#     # 머희식으로 사전 순으로 가장 첫번째로 돌아간다.
#     if flag == 0:
#         lst.sort()
#         return lst
    
#     # flag 값 바로 앞의 숫자부터 하나씩 바꿔줘야하고, 그 앞은 안 바꿔도 됨
#     result = lst[:flag-1]
#     # flag-1 번째 숫자는 기존 숫자의 +1씩 해서 앞에 없는 숫자를 넣어줘야함
#     n = lst[flag-1]+1
#     if n > N: n = 1
#     while n in result:
#         n += 1
#         if n > N: n = 1
#     result.append(n)
#     # result 배열에 추가해야하는 숫자의 갯수만큼 1부터 차례차례 넣어준다.
#     for _ in range(flag, len(lst)):
#         n = 1
#         if n > N: n = 1
#         while n in result:
#             n += 1
#             if n > N: n = 1
#         result.append(n)
    
#     return result

# if __name__ == "__main__":
#     N, K = map(int, input().split())
#     answer = list(map(int, input().split()))
    
#     # 전체 순열의 갯수
#     all_cases = factorial(N)
#     # K가 전체 순열의 갯수보다 크면, 한바퀴 돌고도 더 도는거니까 나머지만큼만 돌리자
#     K %= all_cases
#     for _ in range(K): answer = next_permutation(answer)
    
#     print(*answer)

#########################################################################################

# # 예상 못한건 아니지만 4, 5번 timeout
# from itertools import permutations

# if __name__ == "__main__":
#     N, K = map(int, input().split())
#     now = tuple(map(int, input().split()))
    
#     # 순열 만들어주기
#     perm = list(permutations(range(1, N+1)))
#     # 현재 순열의 인덱스 찾기
#     now_idx = perm.index(now)
    
#     # 우리가 print 해야하는 순열의 인덱스 찾기
#     idx = now_idx + K
#     while idx >= len(perm):
#         idx -= len(perm)
    
#     print(*perm[idx])