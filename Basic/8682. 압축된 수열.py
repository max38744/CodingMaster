'''
기성은 코딩 테스트 출제를 전문으로 하는 기업에서 일하고 있습니다. 
고객마다 서로 다른 요구사항이 있기 때문에 문제의 난이도, 입출력 등을 잘 관리해야 합니다. 
오늘은 A 기업에서 주문한 문제를 만들고 있습니다. 
A 기업의 요구사항 중 하나는 다음과 같습니다 : 
"입력 파일의 크기가 M보다 크지 않게 해주세요."

기성이 만든 문제의 입력 파일에는 공백으로 구분된 정수 N개가 저장되어 있습니다. 
i번째 정수가 L[i]자리 수라면, 
입력 파일의 크기는 L[1] + L[2] + … + L[N-1] + L[N] + (N - 1)입니다. 
N - 1은 공백이 차지하는 크기입니다. 
예를 들어 입력 파일 "1 2 30 123"의 크기는 10입니다.

그런데, 입력 파일의 크기가 M보다 큰 것 이였습니다. 
기성은 이 문제를 해결하기 위해 정수를 10진법 대신 다른 진법으로 표기하기로 했습니다. 
10진법 정수 123(= 1 × 10² + 2 × 10¹ + 3 × 10⁰)은 12진법으로 A3(= A × 12¹ + 3 × 12⁰)으로 표기하고, 40진법으로 33(= 3 × 40¹ + 3 × 40⁰)으로 표기합니다. 
10진법 0부터 9까지는 똑같이 0부터 9로, 10부터 35까지는 A부터 Z까지의 대문자 알파벳으로, 36부터 61까지는 a부터 z까지의 소문자 알파벳을 사용합니다.

예를 들어 입력 파일 "1 2 30 123"을 12진법으로 표기하면 "1 2 26 A3"이 되어 파일의 크기가 9로 줄어듭니다. 
입력 파일의 크기가 M 이하가 되는 10 이상의 가장 작은 진법을 출력하는 프로그램을 작성하세요.


예제 입력1

4 9
1 2 30 123

예제 출력1

12

예제 입력2

4 18
100000 100000 100000 100000

예제 출력2

47


입력값 설명

첫째 줄에 두 정수 N과 M이 공백으로 구분되어 주어집니다. (1 ≤ N ≤ 100, 1 ≤ M ≤ 1,000)
둘째 줄에 기성이의 입력 파일이 주어집니다. (1 ≤ 입력 파일의 모든 정수 ≤ 100,000)
기성의 입력 파일의 정수는 모두 10진법으로 작성되어 있습니다.

출력값 설명

입력 파일의 크기가 M 이하가 되는 10 이상의 가장 작은 진법을 출력합니다.
만약 62진법으로 표기해도 입력 파일의 크기가 M보다 크다면 대신 -1을 출력합니다.
'''
# -*- coding: utf-8 -*-
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
numbers = list(map(int,input().split()))
answer = -1

# 10진수 -> n진수 변환 함수
def trans_jinsu(number, base):
    result = ''
    while number > 0:
        remain = number % base
        if 10 <= remain < 36:      # 대문자
            result = chr(remain + 55) + result
        elif 36 <= remain < 62:    # 소문자 
            result = chr(remain + 61) + result
        else:                       # 0~9
            result = str(remain) + result
        number = number // base
    return result
        
# 11~62진법 돌리기
for i in range(10, 63):
    trans_numbers = ''
    # 변환 파일 길이 구하기
    for number in numbers:
        trans_numbers = trans_numbers + trans_jinsu(number,i) + ' '
        trans_len = len(trans_numbers) - 1    
        
    # 변환한 파일크기가 m보다 작아지면 그만
    if trans_len <= m:
        answer = i
        break

print(answer)