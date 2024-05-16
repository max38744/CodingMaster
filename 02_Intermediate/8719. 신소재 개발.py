'''
철수는 회사 연구실에서 근무 중입니다.
연구실에는 N개의 용액이 존재합니다.
각 용액은 A 타입, B 타입, C 타입 중 하나입니다.
현재 철수는 세 가지 타입의 용액을 섞어 신소재를 개발할 수 있는지 실험하고 있습니다.

실험 과정은 다음과 같습니다.

1. 실험 시작 시, 비커는 비어있습니다.
2. 용액 한 개를 선택해 비커에 모두 투입합니다.
3. N개의 용액을 모두 소모하면 실험이 종료됩니다.

간단한 실험이지만 주의해야 할 사항이 있습니다.
직전에 투입한 용액과 같은 타입의 용액을 연속해서 투입하면 사고가 발생합니다.

예를 들어 비커에 첫 번째로 투입한 용액이 A 타입이라고 가정하겠습니다.
두 번째로 투입하는 용액이 A 타입이라면 사고가 발생합니다.
두 번째로 투입하는 용액이 B 타입 또는 C 타입일 경우 사고가 발생하지 않습니다.

각 타입의 용액의 개수가 주어졌을 때,
철수가 사고 발생 없이 실험을 끝마칠 수 있는지 여부를 구하는 프로그램을 작성하세요.
------------------------------------------------------------------------
[입력값 설명]
『첫째 줄에 양의 정수 A, B, C가 공백으로 구분되어 주어집니다.
이는 각 타입 용액의 개수를 의미합니다. (1 ≤ A, B, C ≤ 10,000)』

[출력값 설명]
『첫째 줄에 사고 발생 없이 실험을 끝마칠 수 있으면 "YES"를, 그렇지 않으면 "NO"를 출력합니다. (큰 따옴표 제외)』
------------------------------------------------------------------------
예제 입력1
1 2 1

예제 출력1
YES

예제 입력2
2 1 5

예제 출력2
NO
'''
# -*- coding: utf-8 -*-
import sys
input = sys.stdin.readline

def is_possible(liquors):
    # 우선 가장 큰 순서대로 재배열
    liquors.sort(reverse=True)
    # A, B, C 로 분배하고, N은 전체 용액의 수
    A, B, C, N = liquors[0], liquors[1], liquors[2], sum(liquors)
    # 1차 조건 : A 가 N + 1 의 절반보다 많으면 안됨 (양끝에 넣을 수 있으니 +1)
    if A > (N + 1)/2: return "NO"
    # A 를 채워넣고 사이 빈 공간의 갯수는 최소 N//2 ~ (N//3)*2+1 개
    # N//2 개 일수록 나머지 갯수는 상관없고, (N//3)*2+1 에 가까울수록 나머지가 절반비율에 가까워져야함
    # 최대 빈칸 갯수 == 홀수 : B, C 1개 차이만 나야함 / 짝수 : 차이나면 안됨
    
    if N%3 == 2:
        # 최대 빈칸 홀수라면, 최대일 때 1칸 차이나도 되고, 그 다음 3칸씩 늘어나다가, 마지막에는 최소 빈칸 수만큼 차이나도 됨
        max_empty = (N//3)*2+1
        now_empty = N - A
        min_empty = N//2
        # 계산 편하려고 임의의 변수 하나 정의
        max_em = max_empty - 1
        # *3 을 해서 차이나도 되는 칸수를 구하려는 변수
        now_sub = max_em - now_empty
        
        # 현재 빈칸이 최소 빈칸 수와 같다면, 무조건 가능 (A가 사이에 한칸씩 막아줌)
        if now_empty == min_empty: return "YES"
        # 그 밖의 경우에는 위의 계산식으로 계산
        elif (B - C) <= (now_sub*3 + 1) : return "YES"
        else: return "NO"

    else:
        # 최대 빈칸 갯수가 짝수라면, (최대 빈칸 - 현재 빈칸)*3 만큼 B와 C가 차이나도 됨
        max_empty = (N//3)*2
        now_empty = N - A
        if (B - C) > (max_empty - now_empty)*3: return "NO"
        else: return "YES"

if __name__ == "__main__":
    liquors = list(map(int, input().split()))
    print(is_possible(liquors))

###################################################################################

# # 4번 안된다. 좀 더 생각해보자.
# def is_possible(liquors):
#     # 우선 가장 큰 순서대로 재배열
#     liquors.sort(reverse=True)
#     # A, B, C 로 분배하고, N은 전체 용액의 수
#     A, B, C, N = liquors[0], liquors[1], liquors[2], sum(liquors)
#     # 1차 조건 : A 가 N + 1 의 절반보다 많으면 안됨 (양끝에 넣을 수 있으니 +1)
#     if A > (N + 1)/2: return "NO"
#     # A 를 채워넣고 사이 빈 공간의 갯수는 최소 N//2 ~ (N//3)*2+1 개
#     # N//2 개 일수록 나머지 갯수는 상관없고, (N//3)*2+1 에 가까울수록 나머지가 절반비율에 가까워져야함
#     # N//2 와 N-A 의 차이보다 B와 C가 덜 차이나면 됨
#     sub = (N-A) - (N//2)
#     if B - C > sub: return "NO"
#     return "YES"

# if __name__ == "__main__":
#     liquors = list(map(int, input().split()))
#     print(is_possible(liquors))

###################################################################################

# # 3, 4번 안되는뎁쇼? 무슨 조건이 더 있을까
# def is_possible(liquors):
#     # 우선 가장 큰 순서대로 재배열
#     liquors.sort(reverse=True)
#     # A, B, C 로 분배하고, N은 전체 용액의 수
#     A, B, C, N = liquors[0], liquors[1], liquors[2], sum(liquors)
#     # 1차 조건 : A 가 N + 1 의 절반보다 많으면 안됨 (양끝에 넣을 수 있으니 +1)
#     if A > (N + 1)/2: return "NO"
#     # 2차 조건 : A 와 B + C 의 차이가 2 이하면 가능
#     if abs(A - (B + C)) <= 2: return "YES"
#     # 3차 조건 : A 와 B 의 차이가 2 이하면 가능
#     if A - B <= 2: return "YES"
#     # 안되면 NO
#     return "NO"

# if __name__ == "__main__":
#     liquors = list(map(int, input().split()))
#     print(is_possible(liquors))