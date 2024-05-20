"""
치훈은 팔찌를 여러 개 가지고 있습니다.
팔찌는 1개 이상의 보석들이 원형으로 배열되어 있는 형태입니다. 

팔찌 2개의 보석 배열 상태가 주어졌을 때,
두 팔찌가 같은 팔찌인지 판별하는 프로그램을 작성하세요.

두 팔찌가 같다는 것은, 팔찌를 회전하여 같은 형태로 만들 수 있다는 것을 말합니다.
단, 팔찌를 뒤집을 수는 없습니다.

예제 입력1
ABCDE
CDEAB

예제 출력1
YES

예제 입력2
AAAAA
AAAAB

예제 출력2
NO

입력값 설명
팔찌 2개가 두 줄에 걸쳐 주어집니다.
각 팔찌는 알파벳 대문자로 이루어진 문자열의 형태로 주어집니다.
같은 문자는 같은 보석을 뜻합니다.
문자열의 길이는 1000 이하입니다.

출력값 설명
두 팔찌가 같으면 YES, 다르면 NO를 출력합니다.
"""

# -*- coding: utf-8 -*-
import sys

bracelet1 = list(input())
bracelet2 = list(input())

flag = 0
for i in range(len(bracelet2)):
    bracelet = bracelet2[i:]+bracelet2[:i]
    if bracelet1 == bracelet:
        flag = 1
        break
        
if flag==1:
    print("YES")
else:
    print("NO")

