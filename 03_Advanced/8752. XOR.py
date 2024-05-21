'''
두 수 A, B를 bitwise-XOR 연산한 결과 A⊕B의 값은 다음과 같이 계산됩니다.
- A의 i번째 비트와 B의 i번째 비트가 같으면 A⊕B의 i번째 비트는 0이 됩니다.
- A의 i번째 비트와 B의 i번째 비트가 다르면 A⊕B의 i번째 비트는 1이 됩니다.

예를 들어 A = 6, B = 10이라고 가정하겠습니다.
A를 네 자릿수 이진수로 나타내면 0110이 됩니다.
B를 네 자릿수 이진수로 나타내면 1010이 됩니다.

A⊕B의 값은 다음 과정에 의해 12가 됩니다.
1) A의 첫번째 비트는 0, B의 첫번째 비트는 1이므로 A⊕B의 첫번째 비트는 1입니다.
2) A의 두번째 비트는 1, B의 두번째 비트는 0이므로 A⊕B의 두번째 비트는 1입니다.
3) A의 세번째 비트는 1, B의 세번째 비트는 1이므로 A⊕B의 세번째 비트는 0입니다.
4) A의 네번째 비트는 0, B의 네번째 비트는 0이므로 A⊕B의 네번째 비트는 0입니다.

N개의 양의 정수 중에서 두 개 이상의 양의 정수를 선택하였을 때, 선택된 수들의 XOR 값이 0이 되는 경우의 수를 구하는 프로그램을 작성하세요.

값이 3개 이상인 경우 앞의 과정을 진행한 결과 값을 다시 XOR계산을 합니다.
위의 예시에서 C=3인경우
[6, 10, 3] 를 계산하면 3의 비트는 0011, 이전의 A,B를 계산한 결과는 1100으로
1100과 0011을 한번 더 비교하면 1111로 15가 됩니다.

예를 들어 N = 4이고 주어진 양의 정수들이 [1, 3, 2, 3]이라고 가정하겠습니다. 선택할 수 있는 모든 경우는 아래와 같이 총 11개입니다.
[1, 3], [1, 2], [1, 3], [3, 2], [3, 3], [2, 3], [1, 3, 2], [1, 3, 3], [1, 2, 3], [3, 2, 3], [1, 3, 2, 3]

이 중에서 XOR 값이 0이 되는 경우는 아래와 같이 총 3개입니다.
[3, 3], [1, 3, 2], [1, 2, 3]
------------------------------------------------------------------------
[입력값 설명]
『첫째 줄에 양의 정수의 개수 N이 주어집니다. (2 ≤ N ≤ 30)
둘째 줄에 N개의 양의 정수가 공백으로 구분되어 주어집니다. 입력으로 주어지는 모든 양의 정수는 1 이상 100,000 이하입니다.』

[출력값 설명]
『첫째 줄에 조건을 만족하는 경우의 수를 출력합니다.』
------------------------------------------------------------------------
예제 입력1
4
1 3 2 3

예제 출력1
3

예제 입력2
3
10 10 10

예제 출력2
3
'''
# format(n, p) : n은 10진수 정수, p는 표현하고자 하는 진수
# p의 종류 : 'b' 2진수, 'o' 8진수, 'x' 16진수 소문자, 'X' 16진수 대문자, 'd' 10진수
# XOR 연산은 결합법칙, 교환법칙이 성립한다.
# 일단 combination을 이용하는건 안됨 -> 자바로 돌려봐도 조합 구한 후 여부 구하기보다 dfs가 더 빨랐다.
# xor 연산은 둘 다 같은 수일 때만 0이 된다 -> 2개의 값만 가질 때는 둘 다 동일한 수여야 한다

# -*- coding: utf-8 -*-
import sys
input = sys.stdin.readline
from collections import defaultdict

def count_xor_zero_subsets(nums):    
    dp = defaultdict(int)
    dp[0] = 1
    
    for num in nums:
        new_dp = dp.copy()
        for xor_sum in dp:
            new_dp[xor_sum ^ num] += dp[xor_sum]
        dp = new_dp
    
    return dp[0] - 1  # 공집합 제외

if __name__ == "__main__":
    N = int(input())
    dNum = list(map(int, input().split()))
    
    # 결과 계산 및 출력
    result = count_xor_zero_subsets(dNum)
    print(result)

###########################################################

# # 4,5,6 timeout
# # GPT한테 자바 코드로 변환 요청할 경우, 6번만 timeout(4번 13s, 5번 20s 정도 걸림)

# # 몇개 더해왔는지, 현재 인덱스, 결과값
# def dfs(choice, c, n, r):
#     global answer
#     if c == choice:
#         if r == 0: answer += 1
#         return
#     for i in range(n+1, N):
#         dfs(choice, c+1, i, r ^ dNum[i])

# if __name__ == "__main__":
#     N = int(input())
#     dNum = list(map(int, input().split()))
#     answer = 0

#     for choice in range(2, N+1):
#         for i in range(N):
#             dfs(choice, 1, i, dNum[i])
#     print(answer)

###########################################################

# # 3~6 전부 timeout
# from itertools import combinations
# from collections import deque
# import numpy as np

# if __name__ == "__main__":
#     N = int(input())
#     dNum = list(map(int, input().split()))

#     # 2진수 변환한 수들 저장할 deque
#     bNum = deque()
#     for n in dNum:
#         # 2진수 변환 후 numpy.array로 저장
#         arr = np.array(list(map(int, format(n, 'b'))))
#         # 10만일 때 2진수는 17자리이므로, 여기에 맞춰서 0을 집어넣어 자릿수를 맞춘다.
#         arr = np.insert(arr, 0, np.zeros(17-len(arr)), axis=0)
#         # bNum 에 저장해주자
#         bNum.append(arr)
#     answer = 0

#     # 선택할 숫자의 갯수를 choice
#     for choice in range(2, N+1):
#         # 선택한 숫자로 나오는 조합을 전부 찾기
#         combis = list(combinations(bNum, choice))
#         # 각각의 조합을 꺼내보자
#         for combi in combis:
#             if sum(sum(combi)%2) == 0: answer += 1
#     print(answer)

###########################################################

# # 4,5,6 timeout
# from itertools import combinations
# from collections import deque

# # 현재 조합의 일부가 0 되는 조합인지 체크
# def is_include(dq):
#     # 이미 만들어진 조합들 하나씩 꺼내보며 체크해보자
#     for zero_combi in already:
#         # 이미 0 되는 조합이 dq 안에 있으면
#         if all(el in dq for el in zero_combi):
#             # dq 안에서 0이 되는 조합의 수들 제거
#             for el in zero_combi: dq.remove(el)
#             # 남은 원소들로만 xor 연산 시작
#             return dq
#     # 만약 이미 만들어진 조합 내에 없으면 그대로 반환
#     return dq

# if __name__ == "__main__":
#     N = int(input())
#     dNum = list(map(int, input().split()))
    
#     # 이미 만들어진 0 되는 조합이 있는지 넣어둘 deque
#     already = deque()
#     # 답이 될, 0 되는 조합의 수
#     answer = 0

#     # 선택할 숫자의 갯수를 choice
#     for choice in range(2, N+1):
#         # 선택한 숫자로 나오는 조합을 전부 찾기
#         combis = deque(map(deque, combinations(dNum, choice)))
#         # 각각의 조합을 꺼내보자
#         for combi in combis:
#             # 이미 연산했던 조합은 연산을 건너뛰자
#             if combi in already:
#                 # 이미 연산했던 조합도 있는 조합이니까 +1
#                 answer += 1
#             else:
#                 # 아니면 일부가 0되는 조합인지 확인
#                 chk = is_include(combi)
#                 # 한번 걸러지고 나온 조합에서 첫번째 숫자
#                 xor = chk.popleft()
#                 # 나머지 숫자들과 xor 연산 진행
#                 while chk:
#                     cb = chk.popleft()
#                     xor = (xor^cb)
#                 # xor 가 0이라면
#                 if xor == 0:
#                     # 원래 조합(combi)을 연산 했던 조합 목록에 넣고
#                     already.appendleft(combi)
#                     # 정답 갯수를 +1 해준다.
#                     answer += 1
#     print(answer)

###########################################################

# # 4,5,6 timeout
# # 챗GPT한테 자바 코드 부탁할 경우에도 동일 결과
# from itertools import combinations

# if __name__ == "__main__":
#     N = int(input())
#     dNum = list(map(int, input().split()))
#     answer = 0

#     # 선택할 숫자의 갯수를 choice
#     for choice in range(2, N+1):
#         # 선택한 숫자로 나오는 조합을 전부 찾기
#         combis = tuple(combinations(dNum, choice))
#         # 각각의 조합을 꺼내보자
#         for combi in combis:
#             # 합칠 기준이 될 첫번째 숫자
#             xor = combi[0]
#             # 그 다음 숫자부터 순차적으로 xor 연산을 시작!
#             for cb in combi[1:]:
#                 xor = (xor ^ cb)
#             # 그 결과가 0이라면 answer + 1
#             if xor == 0: answer += 1
#     print(answer)
