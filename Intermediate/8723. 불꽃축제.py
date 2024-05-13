'''
철수가 사는 마을에서 불꽃 축제가 열립니다.
불꽃 축제는 N일 동안 연속으로 진행됩니다. 
수많은 관광객들이 불꽃 축제를 보러 철수네 마을을 방문합니다. 

철수는 마을을 방문한 관광객들을 상대로 푸드트럭을 운영하기로 했습니다. 
철수는 축제의 i번째 날에 푸드트럭을 운영했을 때 발생하는 이익 a_i를 정확하게 예측할 수 있습니다. 
여기서 이익이란 매출에서 비용을 차감한 값을 의미합니다. a_i는 음수가 될 수 있습니다.

철수는 푸드트럭이 없으므로 필요한 날만큼 푸드트럭을 대여해야 합니다. 
푸드트럭은 한 번 대여하면 연속한 날동안 사용 후 반납합니다. 
푸드트럭을 대여하고 반납하는 과정이 번거롭기 때문에 철수는 푸드트럭을 단 한 번만 대여할 예정입니다.

예를 들어 철수가 축제의 두 번째 날에 트럭을 대여하고 다섯 번째 날에 반납한다고 가정하겠습니다. 
이 경우 철수가 얻는 이익의 총합은 a_2 + a_3 + a_4 + a_5입니다.

철수가 예측한 이익이 주어질 때, 
철수가 푸드트럭을 한번만 대여하여 반납해서 얻을 수 있는 이익의 총합의 최댓값을 구하는 프로그램을 작성하세요.


예제 입력1

5
23 -10 3 4 5

예제 출력1

25

예제 입력2

3
-1 -2 -3

예제 출력2

-1


입력값 설명

첫째 줄에 축제 기간을 의미하는 양의 정수 N이 주어집니다. (1 ≤ N ≤ 5,000)
둘째 줄에 철수가 예측한 이익 a_i가 공백으로 구분되어 주어집니다.
a_i는 정수입니다. (-10,000 ≤ a_i ≤ 10,000)

출력값 설명

첫째 줄에 철수가 얻을 수 있는 이익의 총합의 최댓값을 출력합니다.
'''
# -*- coding: utf-8 -*-
import sys

input = sys.stdin.readline

n = int(input())
a_i = list(map(int, input().split()))

tmp_sum = a_i[0]
answer = a_i[0]
        
for i in range(1, n):
    tmp_sum = max(tmp_sum + a_i[i], a_i[i])
    answer = max(tmp_sum, answer)

print(answer)