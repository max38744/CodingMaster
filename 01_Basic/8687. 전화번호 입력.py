'''진익은 동아리의 게시판을 만들었습니다. 게시판에는 회원의 전화번호를 입력하는 칸이 있는데 다음과 같이 특정한 형태의 전화번호만을 입력받고자 합니다.

010-XXXX-XXXX

이때 X에는 0부터 9까지의 한자리 자연수가 올 수 있습니다.



입력이 주어질 때 유효한 입력인지 확인하는 프로그램을 작성하세요.


예제 입력1

010-1234-5678

예제 출력1

valid
예제 입력2

010-1232-12312

예제 출력2

invalid

입력값 설명

첫째 줄에 문자열 S가 주어집니다. 문자열은 하이픈 기호(-)와 0부터 9까지의 숫자로만 구성되어 있습니다. 문자열의 길이는 26보다 작거나 같습니다.

출력값 설명

유효한 입력이면 "valid", 그렇지 않으면 "invalid"를 출력합니다.'''

import sys

a = input()
def valid(a):
    if len(a) != 13:
        return False
    if a[0] != '0' or a[1] != '1' or a[2] != '0':
        return False
    if a[3] != '-' or a[8] != '-':
        return False
    for i in range(len(a)):
        if i != 3 and i != 8: 
            if not a[i].isdigit():
                return False

    return True

if valid(a):
    print('valid')
else:
    print('invalid')
