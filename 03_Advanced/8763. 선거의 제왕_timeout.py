'''초등학교 반장선거 때부터 선거를 했다 하면 언제나 당선되는 선거의 제왕이 있습니다. 



선거의 제왕이 언제나 선거에서 승리할 수 있었던 이유는 바로 자신을 포함한 후보의 지지자 수가 얼마나 많은지 정확히 헤아리고 자신을 제외한 다른 각 후보 별로 원하는 지지자 수 만큼 자신을 뽑도록 설득시킬 수 있는 능력이 있기 때문입니다.



이제 선거의 제왕은 또 다른 선거에 1번 후보자로 참여하여 자신의 능력을 살려 당선되려고 합니다. 



하지만 이번에 치르는 선거는 전국 단위로 이루어지기 때문에, 평소처럼 자신을 지지하지 않는 다른 사람들 모두에게 자신을 뽑으라고 설득시키려 하면 선거활동 비용이 천정부지로 치솟아 곤란해질 것입니다.



따라서 선거의 제왕은 자신이 선거에서 승리하기 위해 설득해야 하는 타 후보의 지지자 수의 최솟값을 찾아 그 사람 수만큼 설득하여 최소한의 선거 비용으로 당선되려고 합니다.



현재 선거의 제왕이 치르는 선거에는 무효표가 존재하지 않고, 당선 기준이 다른 모든 각 후보자들의 지지자 수보다 자신의 지지자 수가 더 많아야 한다는 것입니다. 선거의 제왕이 당선되기 위해 설득해야 하는 다른 후보의 지지자 수의 최솟값을 출력하는 프로그램을 작성하세요.


예제 입력1

2
3 5

예제 출력1

2

예제 입력2

5
1 4 5 2 3

예제 출력2

3


입력값 설명

첫 번째 줄에 선거 후보자의 수 N이 주어집니다. (2 ≤ N ≤ 4,000)

두 번째 줄에 각 후보자의 지지자 수 a_1, a_2, ..., a_N이 주어집니다. (1 ≤ a_i ≤ 10⁹)

출력값 설명

선거의 제왕이 당선을 위해 설득해야 하는 다른 후보의 지지자 수의 최솟값을 출력합니다.'''
'''# -*- coding: utf-8 -*-
import sys
input = sys.stdin.readline

def king(N, support):
    king = support[0]
    count = 0
    supporter = support[1:]
    
    while True:
        max_supporter = max(supporter)  
        if king > max_supporter:
            break  
        max_index = supporter.index(max_supporter)
        supporter[max_index] -= 1  
        king += 1
        count += 1
        
    return count

N = int(input())
support = list(map(int, input().split()))
print(king(N, support))
========================================================timeout

import sys
import heapq

input = sys.stdin.readline

def king(N, support):
    king = support[0]
    count = 0
    supporter = [-x for x in support[1:]]  
    heapq.heapify(supporter)  

    while supporter and king <= -supporter[0]:
        max_supporter = -heapq.heappop(supporter)
        max_supporter -= 1
        king += 1
        count += 1
        heapq.heappush(supporter, -max_supporter)
    
    return count

N = int(input())
support = list(map(int, input().split()))
print(king(N, support))
=======================================================timeout''' 
