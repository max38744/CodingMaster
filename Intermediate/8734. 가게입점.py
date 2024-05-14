'''
시은은 가게를 입점시키는 관리자입니다. 

시은은 3개의 가게를 에이블시에 입점시키려고 합니다. 

에이블시는 1번지부터 1,000,000번지까지 존재하며, 각 번지에는 하나의 건물이 있습니다.



시은은 이번에 A 가게, B 가게, C 가게가 입점할 건물을 정해달라고 의뢰를 받았습니다. 

이때, 시은이 결정할 수 있는 건물의 번지 수의 범위가 한정되어 있습니다. 

구체적으로, 시은이 입점시킬 건물은 모두 L번지 이상 R번지 이하여야 합니다.



시은은 여러 가지 경우의 수를 시도해보다가, 

A 가게 건물의 번지 수가 B 가게 건물과 C 가게 건물의 번지 수를 합친 것과 같을 때가 

장사가 잘 될 가게 배치라고 느꼈습니다. 



L과 R이 주어졌을 때, 가능한 모든 장사가 잘 될 가게 배치 쌍의 수를 구하는 프로그램을 작성하세요. 



이때, 하나의 건물에 여러 개의 가게를 입점시킬 수 있음에 유의하세요.


예제 입력1

2 5

예제 출력1

3

예제 입력2

1 1000000

예제 출력2

499999500000


입력값 설명

건물의 번지 수가 될 수 있는 범위 L과 R이 공백으로 구분되어 주어집니다. (1 ≤ L ≤ R ≤ 1,000,000)

출력값 설명

가능한 모든 장사가 잘 될 가게 배치 쌍의 수를 출력합니다.
'''

# -*- coding: utf-8 -*-
import sys
input = sys.stdin.readline
a ,b = map(int,input().split()) 
count = 0
for x in range(a,b+1):
    count += max(min(b,x-a)-max(a,x-b)+1,0)
print(count)
