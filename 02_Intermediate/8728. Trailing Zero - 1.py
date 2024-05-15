'''
수학에서 어떤 자연수의 팩토리얼이란 그 수보다 작거나 같은 모든 자연수를 곱한 것을 의미합니다. 
몇 개의 팩토리얼의 값을 표기하면 다음과 같습니다. 

10! = 3628800
20! = 2432902008176640000
30! = 265252859812191058636308480000000

여기에서 맨 뒤에 연속하는 0의 갯수는 수가 커짐에 따라 늘어나는 것을 관찰할 수 있습니다. 
이러한 맨 뒤에 연속하는 0을 Trailing Zero라고 부릅니다. 
진법 표기와는 상관없이 n이 커질수록 Trailing Zero의 갯수는 늘어나게 됩니다. 

예를 들어 위의 팩토리얼의 값을 7진법에서 써보면 다음과 같게 됩니다. 
10! = 42562410 (7)
20! = 4233013654405404511500 (7)
30! = 202013214243236331166216633513566660000 (7)

정수 p와 n이 주어졌을 때, 
p-진법 체계에서 n!의 Trailing Zero는 몇 개인지 알아내는 프로그램을 작성하세요.

예제 입력1
10 10
예제 출력1
2

예제 입력2
7 30
예제 출력2
4

입력값 설명
첫 번째 줄에 문제에서 설명한 정수 p와 n이 공백으로 구분되어 주어집니다.
(2 ≤ p ≤ 100, 1 ≤ n ≤ 1,000)

출력값 설명
첫 번째 줄에 p-진법에서 n!의 Trailing Zero의 개수를 출력합니다.
'''

# 재귀식
# def factorial(num):
#     if num == 1:
#         return 1
#     if num == 2:
#         return 2
#     fac = factorial(num-1) * num
#     return fac


# 1st - try
'''
# -*- coding: utf-8 -*-
import sys

input = sys.stdin.readline


# 반복문
def factorial(num):
    n = 1
    for i in range(2, num+1):
        n = i * n
    return n


def to_base_p(num, p):
    result = []
    while num > 0:
        remainder = num % p
        result.append(remainder)
        num //= p

    n = ''
    for i in result[::-1]:
        n += str(i)
    return n  # 역순으로 변환된 문자를 반환


def trailing_z(p, num):
    n = to_base_p(factorial(num), p)

    cnt = 0
    for i in n[::-1]:  # 맨 뒤부터 0 개수 체크
        if i == '0':
            cnt += 1
        else:
            break

    return cnt

print(trailing_z(2, 1000))

# p, num = map(int, input().split())
'''


# 2nd - try
# -*- coding: utf-8 -*-
import sys

input = sys.stdin.readline

def factorial(num):
    n = 1
    for i in range(2, num+1):
        n = i * n
    return n

def trailing_zeros_in_factorial(p, n):
    factorial_value = factorial(n)
    trailing_zeros_count = 0
    
    while factorial_value % p == 0:
        trailing_zeros_count += 1
        factorial_value //= p
    
    return trailing_zeros_count

# 입력 받기
p, n = map(int, input().split())
# 결과 출력
print(trailing_zeros_in_factorial(p, n))