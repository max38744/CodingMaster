'''군조는 이사를 하려고 짐을 정리하고 있었습니다. 

군조는 대부분의 짐을 정리하는 것을 마무리하였고, 이제 단 3개의 짐만을 남겨두고 있습니다. 

군조는 짐을 깔끔하게 정리하는 것을 좋아하기 때문에, 짐을 짐의 색과 같은 색의 박스에 넣으려고 합니다. 

하지만, 성격이 급한 정인이 이미 이 3개의 짐을 상자에 넣어버렸다는 사실을 알았습니다.



짐은 총 3개로, 각각 빨간색, 초록색, 파란색입니다. 

상자도 총 3개로, 각각 빨간색, 초록색, 파란색입니다. 

정인은 3개의 짐을 무작위로 각각 한 상자에 하나씩 넣었습니다. 



정인의 이러한 짐 정리 방식에 화가 난 군조는, 정인에게 하나의 명령을 내렸습니다. 

이 명령의 내용은 "어떤 두 상자를 골라서 각 상자에 들어있는 짐의 위치를 바꾸는 행동"을 

정확히 10^18번 하는 것으로, 정인이 이 행동을 하고 난 후에 모든 짐이 같은 색의 상자에 들어있다면 

군조는 정인을 용서해주고, 아니라면 정인에게 벌을 내리려고 합니다.



정인이 처음에 넣은 짐과 상자의 색이 주어질 때, 

정인이 군조의 명령을 이행한 뒤 군조에게 용서받을 수 있을지 구하는 프로그램을 작성하세요.


예제 입력1

R G B

예제 출력1

possible

예제 입력2

B G R

예제 출력2

impossible


입력값 설명

정인이 빨간색 상자, 초록색 상자, 파란색 상자에 넣은 짐의 색이 하나씩 순서대로 공백으로 구분되어 주어집니다.

빨간색 짐은 R, 초록색 짐은 G, 파란색 짐은 B로 주어집니다.

출력값 설명

정인이 용서받을 수 있으면 possible, 용서받을 수 없으면 impossible을 출력합니다.
알파벳 소문자로만 출력해야 함에 유의해주세요.'''
# -*- coding: utf-8 -*-
import sys
input = sys.stdin.readline

if __name__ == "__main__":
    Rbox, Gbox, Bbox = map(str, input().rstrip().split())
    
    cnt = 0
    if Rbox == 'R': cnt+=1
    if Gbox == 'G': cnt+=1
    if Bbox == 'B': cnt+=1
    
    if (cnt == 3) or (cnt == 0): print('possible')
    else: print('impossible')
