'''맥시마는 자연수를 관장하는 신입니다. 

맥시마는 자연수를 만들었지만, 자연수를 재미없게 크기 순으로 1, 2, 3, …처럼 배열한 것을 후회하고 있습니다. 

따라서 맥시마는 자연수를 배열하는 방식을 바꾸려고 합니다.



자연수를 배열하는 방식을 바꾸기 앞서 자연수가 너무 많이 존재하기 때문에, 

1부터 N까지의 자연수 N개만 사용하려고 합니다.

 

자연수 N개를 배열할 때는 먼저 홀수를 증가하는 순으로, 그 다음에는 짝수를 증가하는 순으로 배열합니다.



예를 들어, N = 11인 경우 자연수의 배열은 아래와 같습니다.



1 3 5 7 9 11 2 4 6 8 10



맥시마는 아주 많은 자연수를 배열하고, 당신에게 배열된 자연수 중 K번째 자연수가 무엇인지 물어보려고 합니다. 

자연수의 개수가 최대 10^12개로 너무 많기 때문에, 직접 배열하면 너무 오래 걸릴 것입니다. 

따라서, 당신은 K번째 자연수를 효율적으로 찾을 수 있는 프로그램을 작성해야 합니다. 



맥시마가 배열한 N개의 자연수 중 K번째 자연수가 무슨 수인지 출력하는 프로그램을 작성하세요.


예제 입력1

11 6

예제 출력1

11

예제 입력2

11 7

예제 출력2

2


입력값 설명

입력의 첫째 줄에는 사용할 자연수의 개수 N과 본문에서 설명된 자연수 K가 주어집니다. (1 ≤ K ≤ N ≤ 10¹²)

출력값 설명

맥시마가 배열한 N개의 자연수 중 K번째 자연수가 무슨 수인지 출력합니다.
'''

# -*- coding: utf-8 -*-
import sys
input = sys.stdin.readline
a,b = map(int,input().split())
hol = (a + 1) // 2

if b <= hol:  
    print(2 * b - 1)
else:  
    print(2 * (b - hol))
