'''
N명의 사람들이 강연을 듣기 위해 강당에 모였습니다. 
그리고 다섯 시간에 걸친 열띤 강의의 1부가 끝나고 지친 사람들은 심신을 달래기 위해 일제히 일어나서 화장실로 달려갔습니다. 
화장실 줄이 복도 저 끝까지 길게 늘어선 것을 본 가영은 절망했습니다. 
'이렇게 사람이 많아서야 강당에 시간내로 다시 들어가는 것은 요원해보이는걸...'
'이 사람들이 다시 자리에 돌아가면 다들 자기 자리를 찾아갈 수 있을까...?'
'한 명도 원래 자리로 돌아가지 못할 수도 있겠는데...'
가영은 요의를 잊기 위해 N명의 사람들이 다시 원래 자리로 돌아오지 않는 경우의 수를 구하기 시작했습니다. 
화장실을 다녀온 뒤 모든 사람들이 원래의 자기 자리에 앉지 않게 될 경우의 수를 구하는 프로그램을 작성하세요. 

예제 입력1
5
예제 출력1
44

예제 입력2
100
예제 출력2
221210562

입력값 설명
첫 번째 줄에 강당에 모인 사람의 수 N이 입력됩니다. (1 ≤ N ≤ 10,000)
출력값 설명
첫 번째 줄에 모든 사람들이 원래의 자기 자리에 앉지 않는 경우의 수를 출력합니다.
단, 답이 매우 커질 수 있으므로 998,244,353으로 나눈 나머지를 출력합니다.
'''

'''
# 1st-try
# -*- coding: utf-8 -*-
import sys

input = sys.stdin.readline

def factorial(num):
    n = 1
    for i in range(2, num+1):
        n = i * n
    return n

def combination(n,r):
    return factorial(n)/(factorial(r)*factorial(n-r))

# 공식 a_n(n명의 사람이 모두 자기 자리에 앉지 않게 될 경우의 수)
# a_n = n! - (nC0 + nC1*a_1 + nC2*a_2 + nC3*a_3 + ... + nCn-1 * a_n-1)
# 여집합의 개념으로 일반화
def rest_time(N):
    if N == 0: return 1
    elif N == 1: return 0
    elif N == 2: return 1
    else:
        answer = int(factorial(N) - sum([combination(N,i)*rest_time(i) for i in range(N)]))
        return answer%998244353

# N = int(input())
print(rest_time(100))
'''
'''
#GPT 1st try
# -*- coding: utf-8 -*-
import sys
input = sys.stdin.readline

MOD = 998244353

def factorial(n, fact):
    if fact[n] != 0:
        return fact[n]
    fact[0] = 1
    for i in range(1, n + 1):
        fact[i] = fact[i-1] * i
    return fact[n]

def combination(n, r, fact):
    if r > n or r < 0:
        return 0
    return fact[n] // (fact[r] * fact[n - r])

def precompute_factorials(N):
    fact = [0] * (N + 1)
    factorial(N, fact)
    return fact

def rest_time(N, fact, memo):
    if N == 0: return 1
    if N == 1: return 0
    if N == 2: return 1
    if memo[N] != -1:
        return memo[N]

    # 공식 a_n(n명의 사람이 모두 자기 자리에 앉지 않게 될 경우의 수)
    # a_n = n! - (nC0 + nC1*a_1 + nC2*a_2 + nC3*a_3 + ... + nCn-1 * a_n-1)
    # 여집합의 개념으로 일반화
    total = factorial(N, fact)
    for i in range(N):
        total -= combination(N, i, fact) * rest_time(i, fact, memo)
    memo[N] = total
    return total % MOD

# N = int(input())
N = 10000
fact = precompute_factorials(N)
memo = [-1] * (N + 1)
print(rest_time(N, fact, memo))
'''
'''
# gpt 2nd try
# cause timeout

import sys
input = sys.stdin.readline
MOD = 998244353

def factorial(n, fact):
    if fact[n] != 0:
        return fact[n]
    fact[0] = 1
    for i in range(1, n + 1):
        fact[i] = fact[i-1] * i
    return fact[n]

def combination(n, r, fact):
    if r > n or r < 0:
        return 0
    return fact[n] // (fact[r] * fact[n - r])

def precompute_factorials(N):
    fact = [0] * (N + 1)
    factorial(N, fact)
    return fact

def rest_time(N, fact, memo):
    if N == 0: return 1
    if N == 1: return 0
    if N == 2: return 1
    if memo[N] != -1:
        return memo[N]

    total = factorial(N, fact)
    for i in range(N):
        total -= combination(N, i, fact) * rest_time(i, fact, memo)
    memo[N] = total
    return total % MOD

N = int(input().strip())
fact = precompute_factorials(N)
memo = [-1] * (N + 1)
print(rest_time(N, fact, memo))
'''
'''
# gpt 3rd try
# for timeout

import sys
input = sys.stdin.readline

MOD = 998244353

def precompute_factorials_and_inverses(N):
    fact = [1] * (N + 1)
    inv_fact = [1] * (N + 1)
    
    for i in range(2, N + 1):
        fact[i] = fact[i-1] * i % MOD
    
    inv_fact[N] = pow(fact[N], MOD - 2, MOD)
    for i in range(N - 1, 0, -1):
        inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD
    
    return fact, inv_fact

def derangements(N, fact, inv_fact):
    dp = [0] * (N + 1)
    dp[0] = 1
    if N > 0:
        dp[1] = 0
    if N > 1:
        dp[2] = 1

    for n in range(3, N + 1):
        total = fact[n]
        for i in range(n):
            total = (total - combination(n, i, fact, inv_fact) * dp[i] % MOD) % MOD
        dp[n] = total
    
    return dp[N]

def combination(n, r, fact, inv_fact):
    if r > n or r < 0:
        return 0
    return fact[n] * inv_fact[r] % MOD * inv_fact[n - r] % MOD

N = int(input().strip())
fact, inv_fact = precompute_factorials_and_inverses(N)
print(derangements(N, fact, inv_fact))
'''

'''
#  gpt 4th try
# for timeout

import sys
input = sys.stdin.readline

MOD = 998244353

def factorial(n, fact):
    if fact[n] != 0:
        return fact[n]
    fact[0] = 1
    for i in range(1, n + 1):
        fact[i] = (fact[i-1] * i) % MOD
    return fact[n]

def combination(n, r, fact, inv_fact):
    if r > n or r < 0:
        return 0
    return (fact[n] * inv_fact[r] % MOD) * inv_fact[n - r] % MOD

def mod_inverse(x, mod):
    return pow(x, mod - 2, mod)

def precompute_factorials_and_combinations(N):
    fact = [0] * (N + 1)
    inv_fact = [0] * (N + 1)
    
    factorial(N, fact)
    
    for i in range(N + 1):
        inv_fact[i] = mod_inverse(fact[i], MOD)
    
    return fact, inv_fact

def rest_time(N, fact, inv_fact, memo):
    if N == 0: return 1
    if N == 1: return 0
    if N == 2: return 1
    if memo[N] != -1:
        return memo[N]

    total = factorial(N, fact)
    for i in range(N):
        total = (total - combination(N, i, fact, inv_fact) * rest_time(i, fact, inv_fact, memo) % MOD) % MOD
    memo[N] = total
    return total

N = int(input().strip())
fact, inv_fact = precompute_factorials_and_combinations(N)
memo = [-1] * (N + 1)
print(rest_time(N, fact, inv_fact, memo))

'''

'''
# answer for java

# // don't place package name.
import java.io.*;
import java.util.*;

# // don't change 'Program' class name and without 'public' accessor.
class Program {
    private static final int MOD = 998244353;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        scanner.close();

        long[] fact = new long[N + 1];
        long[] invFact = new long[N + 1];

        precomputeFactorialsAndInverses(N, fact, invFact);
        System.out.println(derangements(N, fact, invFact));
    }

    private static void precomputeFactorialsAndInverses(int N, long[] fact, long[] invFact) {
        fact[0] = 1;
        for (int i = 1; i <= N; i++) {
            fact[i] = fact[i - 1] * i % MOD;
        }

        invFact[N] = modInverse(fact[N], MOD);
        for (int i = N - 1; i >= 0; i--) {
            invFact[i] = invFact[i + 1] * (i + 1) % MOD;
        }
    }

    private static long modInverse(long x, int mod) {
        return pow(x, mod - 2, mod);
    }

    private static long pow(long base, long exp, int mod) {
        long result = 1;
        while (exp > 0) {
            if ((exp & 1) == 1) {
                result = result * base % mod;
            }
            base = base * base % mod;
            exp >>= 1;
        }
        return result;
    }

    private static long derangements(int N, long[] fact, long[] invFact) {
        long[] dp = new long[N + 1];
        dp[0] = 1;
        if (N > 0) dp[1] = 0;
        if (N > 1) dp[2] = 1;

        for (int n = 3; n <= N; n++) {
            long total = fact[n];
            for (int i = 0; i < n; i++) {
                total = (total - combination(n, i, fact, invFact) * dp[i] % MOD + MOD) % MOD;
            }
            dp[n] = total;
        }

        return dp[N];
    }

    private static long combination(int n, int r, long[] fact, long[] invFact) {
        if (r > n || r < 0) {
            return 0;
        }
        return fact[n] * invFact[r] % MOD * invFact[n - r] % MOD;
    }
}
'''

import sys
import math

input = sys.stdin.readline
MOD = 998244353

def combination(n, r):
    if r > n or r < 0:
        return 0
    return math.factorial(n) // (math.factorial(r) * math.factorial(n-r))

def rest_time(N, memo):
    if N == 0: return 1
    if N == 1: return 0
    if N == 2: return 1
    if memo[N] != -1:
        return memo[N]

    total = math.factorial(N)
    for i in range(N):
        total -= combination(N, i) * rest_time(i, memo)
    memo[N] = total
    return total % MOD

N = int(input())
memo = [-1] * (N + 1)
print(rest_time(N, memo))