'''
수학에서 어떤 자연수의 팩토리얼이란 그 수보다 작거나 같은 모든 자연수를 곱한 것을 의미합니다. 
몇 개의 팩토리얼의 값을 십진법으로 표기하면 다음과 같습니다. 

10! = 3628800
20! = 2432902008176640000
30! = 265252859812191058636308480000000

여기에서 맨 뒤에 연속하는 0의 갯수는 수가 커짐에 따라 늘어나는 것을 관찰할 수 있습니다. 
이러한 맨 뒤에 연속하는 0을 Trailing Zero라고 부릅니다. 

정수 n이 주어졌을 때, 
십진법 체계에서 팩토리얼의 Trailing Zero 갯수가 n보다 작지 않게 되는 최솟값이 얼마인지 알아내는 프로그램을 작성하세요.

예제 입력1
1
예제 출력1
5

예제 입력2
6
예제 출력2
25

입력값 설명
첫 번째 줄에 문제에서 설명한 정수 n이 주어집니다.
(1 ≤ n ≤ 1,000)
출력값 설명
첫 번째 줄에 팩토리얼의 Trailing Zero 개수가 n보다 작지 않게 되는 최솟값을 출력합니다.
'''

'''
# 1st try
# -*- coding: utf-8 -*-
import sys

input = sys.stdin.readline


def factorial(num):
    n = 1
    for i in range(2, num+1):
        n = i * n
    return n


def min_trailing_zeros_in_factorial(n):
    i = 1
    while True:
        factorial_value = factorial(i)

        trailing_zeros_count = 0
        while factorial_value % 10 == 0:
            trailing_zeros_count += 1
            factorial_value //= 10

        if trailing_zeros_count == n:
            return i

        i += 1


# 입력 받기
n = int(input())
# 결과 출력
print(min_trailing_zeros_in_factorial(n))
'''

'''
# 2nd try
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

def min_zeros(n):
    i=5
    while trailing_zeros_in_factorial(10, i) < 1002:
        if trailing_zeros_in_factorial(10, i) >= n:
            return i
        i += 5
    
    
# 입력 받기 
n = int(input())
# 결과 출력
print(min_zeros(n))
'''

# 3rd try
# -*- coding: utf-8 -*-
import sys 

input = sys.stdin.readline


def min_zeros(n):

    i = 5
    while True:
        if (i // 5 + i // 25 + i // 125 + i//625 + i // 3125) >= n:

            return i
        i += 5


# 입력 받기
n = int(input())
# 결과 출력
print(min_zeros(n))
