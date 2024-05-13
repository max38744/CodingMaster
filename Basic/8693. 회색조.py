'''
컴퓨터 프로그램에서는 보통 색상을 #과 16진수 6자리로 나타내고는 합니다.
이를 헥스 코드라고 부릅니다.

헥스 코드의 구조는 #RRGGBB로, RR에는 Red의 강도, GG에는 Green의 강도, BB에는 Blue의 강도를 16진수로 표기합니다. 16진수를 표기할 때 알파벳은 대문자입니다.
최솟값은 00(0), 최댓값은 FF(255)입니다. 

여기서 Red, Green, Blue의 평균을 구하면 기본적인 회색조 변환이 됩니다.
예를 들어 #123456의 경우 Red, Green, Blue가 각각 18, 52, 86이므로, 이 값들의 평균인 52를 Red, Green, Blue에 모두 넣은 #343434가 변환 결과가 됩니다.
만약 평균값이 자연수가 아닐 때는 그 값에서 반올림해서 사용합니다. 

헥스 코드가 입력되었을 때, 이 헥스 코드에 해당하는 색을 회색조로 변환하여 다시 헥스코드로 출력하는 프로그램을 작성하세요. 

예제 입력1
#123456
예제 출력1
#343434

예제 입력2
#000101
예제 출력2
#010101

입력값 설명
첫 번째 줄의 어떤 색상의 헥스 코드가 입력됩니다.
출력값 설명
첫 번째 줄에 입력된 헥스 코드에 해당하는 색상을 회색조로 변환한 헥스 코드를 출력합니다.
'''

# -*- coding: utf-8 -*-
import sys

input = sys.stdin.readline

# 반올림 만들기
def Rounds(number):
    # 소수만 추출
    if number-int(number) < 0.5:
        return int(number)
    else: return int(number)+1

# RGB to Gray
def make_gray(color):

    # split color / change to decimal(10진수)
    red = int(color[1:3],16)
    green = int(color[3:5],16)
    blue = int(color[-2:],16)

    # make gray
    gray = Rounds((red+green+blue)/3)

    # 1의 자리 수는 숫자 하나만 나오기 때문에 10의 자리 수로 변환
    if gray < 10:
        gray = '0'+str(gray)
    else:
        gray = (hex(gray)[2:]).upper() # hex만 출력하면 앞에 2개는 16진수를 나타내는 의미도 같이 출력 후 대문자


    # return answer
    answer = '#'+gray*3 # 대문자 변경
    
    return print(answer)

color = input().rstrip()
make_gray(color)



