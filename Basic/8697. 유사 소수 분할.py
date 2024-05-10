'''1과 자기 자신으로만 나누어떨어지는 2 이상의 수를 소수라고 부른다는 사실은 널리 알려져 있습니다. 여기서 확장해서 1과 자기 자신과 서로 다른 두 개의 소수로만 나누어떨어지는 수를 유사 소수라고 부르기로 합시다. 유사 소수의 예시로는 2 × 3 = 6, 3 × 7 = 21 등이 있습니다.



유사 소수에 관련된 흥미로운 문제가 있습니다. 임의의 자연수 N에 대해서 N을 4개의 서로 다른 수의 합으로 표현할 때, 그 4개의 수 중 3개 이상이 유사 소수가 되게 할 수 있는지에 대한 문제입니다. 만약 N에 대해 이것이 가능하다면, 우리는 그 N을 유사 소수 분할이 가능하다고 표현합니다.



예를 들어, N = 62일 때는 N을 5 + 10 + 14 + 33와 같이 분할했을 때 3개의 유사 소수를 포함하게 할 수 있으므로 62는 유사 소수 분할이 가능합니다. 반면, N = 15일 때는 어떻게 해도 3개 이상의 유사 소수를 포함하도록 분할할 수 없으므로 유사 소수 분할이 불가능합니다.



N의 값이 주어졌을 때, N이 유사 소수 분할이 가능한 수인지 구하는 프로그램을 작성하세요.


예제 입력1

62

예제 출력1

possible

예제 입력2

15

예제 출력2

impossible


입력값 설명

자연수 N이 주어집니다.

출력값 설명

N이 유사 소수 분할이 가능한 수라면 possible, 아니면 impossible을 출력합니다.
답은 무조건 소문자로만 출력해야 함에 유의하세요.
'''

# -*- coding: utf-8 -*-
import sys
input = sys.stdin.readline

def yusaprime(num):
    primes = list(range(2, num))
    # num 보다 작은 소수들 에라토스테네의 체 알고리즘으로 찾기
    i, l = 0, len(primes)
    while i < l:
        for j in range(primes[i]+1, num):
            if j % primes[i] == 0:
                while j in primes:
                    primes.remove(j)
        i, l = i+1, len(primes)
    # 유사소수 판별
    for p1 in primes:
        if num%p1 == 0:
            q = num//p1
            if (q != p1) and (q in primes): return 1
    return 0
 
def forloop(N):
    for a in range(1, N):
        for b in range(a+1, N):
            for c in range(b+1, N):
                d = N - (a + b + c)
                if d >= (c+1):
                    count = yusaprime(a) + yusaprime(b) + yusaprime(c) + yusaprime(d)
                    if count >= 3: return 'possible'
    return 'impossible'

if __name__ == "__main__":
    N = int(input())
    print(forloop(N))
