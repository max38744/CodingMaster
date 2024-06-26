'''
철수는 아이들에게 선물을 나눠주려고 합니다.

철수는 N 종류의 선물을 갖고 있으며, 각 종류에는 1번부터 N번까지 번호가 붙어있습니다.
i번 종류 선물의 개수는 a_i로 표기합니다.

선물을 무작위로 나눠주면 아이들 사이에 다툼이 발생합니다.
모든 종류의 선물에 대해 개수를 공평하게 나눠줘야 합니다.

예를 들어 3명의 아이들에게 선물을 나눠준다고 가정하겠습니다.
이 경우 아이 1명 당 1번 종류의 선물 a_1 / 3개, 2번 종류의 선물 a_2 / 3개, …, N번 종류의 선물 a_N / 3개를 받습니다.

철수는 선물을 남기지 않고 최대한 많은 아이들에게 나눠주려고 합니다.
선물을 받게 되는 아이들의 최대 명수를 구하는 프로그램을 작성하세요.
------------------------------------------------------------------------
[입력값 설명]
『첫째 줄에 양의 정수 N이 주어집니다. (1 ≤ N ≤ 100)
둘째 줄에 양의 정수 a_i가 공백으로 구분되어 주어집니다. (1 ≤ a_i ≤ 10,000)』

[출력값 설명]
『첫째 줄에 선물을 받게 되는 아이들의 최대 명수를 출력합니다.』
------------------------------------------------------------------------
예제 입력1
3
3 9 6

예제 출력1
3

예제 입력2
5
2 1 4 8 10

예제 출력2
1
'''
# -*- coding: utf-8 -*-
import sys
input = sys.stdin.readline

def list_gcd(lst):
    # 최대공약수 찾기니까 최대값부터 -1로 진행
    for c in range(min(lst), 0, -1):
        chk = True # 플래그변수 : c가 최대공약수면 True
        for num in lst:
            # 한번이라도 나머지가 0이 아니면, 공약수가 아니면 break
            if num % c != 0:
                chk = False
                break
        # 최대공약수면 c를 return
        if chk: return c

if __name__ == "__main__":
    N = int(input())
    a = list(map(int, input().split()))
    
    print(list_gcd(a))