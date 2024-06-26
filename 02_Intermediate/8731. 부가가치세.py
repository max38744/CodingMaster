'''
부가가치세란 상품의 거래나 서비스의 제공과정에서 얻어지는 부가가치에 대하여 과세하는 세금입니다. 
사전적 정의는 이러하지만 컴퓨터공학을 전공한 가영은 위 문장을 봐도 무슨 소리인지 이해하지 못했습니다. 
중요한 것은 이 부가가치세를 최종소비자인 우리가 부담한다는 사실이죠. 

아무튼 영수증에 찍힌 부가가치세를 보던 가영은 신기한 사실을 알아냈습니다. 
바로 공급가액에서 10으로 나누기를 하고 소숫점이하를 버린 결과가 부가세가 된다는 점이었죠. 

예를 들어 물건의 공급가액은 27182원이고, 부가세는 2718원이면 물건의 총액이 29900원임을 알 수 있습니다. 
가영은 다른 자연수도 이렇게 나눌 수 있는지 궁금했지만 사칙연산에 약한 가영은 도저히 할 수 없었습니다. 

가영을 위해 주어진 자연수를 위와 같은 방법으로 나누는 프로그램을 작성하세요.

예제 입력1
29900
예제 출력1
27182 2718
예제 입력2
10
예제 출력2
-1

입력값 설명
첫 번째 줄에 10 이상 10¹⁰ 이하의 자연수가 물건의 총액으로서 주어집니다.
출력값 설명
첫 번째 줄에 물건의 공급가액과 부가가치세를 공백으로 구분하여 출력합니다.
만약 문제와 같은 방법으로 나눌 수 없는 경우에는 -1을 대신 출력합니다.
'''

# -*- coding: utf-8 -*-
import sys

input = sys.stdin.readline

def tax(price):
    tax = int(0.1 * price/(1.1))
    p_price = price - tax
    
    if int(p_price * 0.1) != tax:
        return print(-1)
    
    return print(p_price, tax)

price = int(input())

tax(price)