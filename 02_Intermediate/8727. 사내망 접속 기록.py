'''
가영은 어떤 회사의 정보보안을 담당하는 부서에서 근무하고 있습니다. 
가영이 맡은 일은 회사의 사내망 접속 기록을 확인하여 직원들이 올바른 방식으로 사내망을 이용한 것이 맞는지를 점검하는 일입니다.

가영의 회사의 사내망은 다음과 같은 형태로 이루어져 있습니다. 
먼저 1차 허브 역할을 하는 중앙 컴퓨터 1대에 N개의 2차 허브 컴퓨터가 연결되어 있습니다. 
그리고 각 2차 허브 컴퓨터마다 2차 허브 컴퓨터를 포함한 M대의 컴퓨터가 모든 쌍에 대해 연결되어 있습니다. 

여기서 중앙 컴퓨터는 항상 0번이고 N개의 2차 허브 컴퓨터의 번호는 1번, M+1번, M×2+1번, ... , M×(N-1)+1번입니다. 
1번과 연결된 컴퓨터는 2번부터 M번, M+1번은 M+2번부터 M×2번 , ... , M×(N-1)+1번은 M×(N-1)+2번부터 M×N번 컴퓨터입니다. 
어떤 컴퓨터에서 다른 컴퓨터로 접속을 할 때는 반드시 연결된 컴퓨터끼리만 이동할 수 있습니다.

그러므로 사내망으로 서로 연결된 컴퓨터를 통해서 접속이 이루어진 경우에 대한 접속 기록을 올바른 접속 기록이라고 할 수 있습니다.

예를 들어, N = 3, M = 5인 경우를 생각해보겠습니다.

2번 컴퓨터에서 바로 0번 컴퓨터를 가는 것은 안되지만, 
2차 허브 컴퓨터인 1번 컴퓨터를 거쳐서 0번 컴퓨터에 접근하는 것은 가능합니다.
물론 같은 2차 허브 컴퓨터와 연결된 1번, 2번, 3번, 4번, 5번 컴퓨터는 서로 직접 바로 접근할 수 있습니다.

어느 날 가영이 점검한 사내망 접속 기록이 입력으로 주어집니다. 
주어진 입력이 올바른 접속 기록인지 판단하는 프로그램을 작성하세요. 


예제 입력1

3 5
2
2 0

예제 출력1

NO

예제 입력2

3 5
3
2 1 0

예제 출력2

YES


입력값 설명

첫 번째 줄에 문제에서 설명한 N과 M이 공백으로 구분되어 주어집니다. (3 ≤ N, M ≤ 1,000)
두 번째 줄에 가영이가 점검한 사내망 접속 기록의 길이 K가 주어집니다. (1 ≤ K ≤ 50)
세 번째 줄에 사내망 접속 기록을 의미하는 K개의 정수가 공백으로 구분되어 주어집니다.
여기서 주어지는 정수는 N×M 이하의 음이 아닌 정수입니다.

출력값 설명

첫 번째 줄에 입력된 접속 기록에 이상이 없다면 "YES", 그렇지 않다면 "NO"를 출력합니다.
'''
import sys
input = sys.stdin.readline

n, m = map(int, input().split()) 

computer = {0:[]}
for i in range(n):
    computer[0].append(m*i+1)
# print(computer)

k = int(input())
record = list(map(int, input().split())) 
for i in range(k-1):
    A = record[i]
    B = record[i+1]
    
    # A가 중앙 컴퓨터일 때 B는 허브 컴퓨터이어야 함
    if A == 0: 
        if B in computer[A]:
            continue
        else:
            print('NO')
            break
    # B가 중앙 컴퓨터일 때
    elif B == 0: 
        if A in computer[B]:
            continue
        else:
            print('NO')
            break
    # A가 허브 컴퓨터일 때
    elif A % m == 1:
        if B in range(A, (A//m+1)*m + 1):
            continue
        else:
            print('NO')
            break
    # B가 허브 컴퓨터일 때
    elif B % m == 1:
        if A in range(B, (B//m+1) *m + 1):
            continue
        else:
            print('NO')
            break
    # m의 배수인 자식 컴퓨터일 때
    elif A % m == 0:
        if A // m -1 == B // m:
            continue
        else:
            print('NO')
            break
    elif B % m == 0:
        if B // m -1 == A // m:
            continue   
        else:
            print('NO')
            break
    # 그냥 자식 컴퓨터 일 때
    elif A // m == B // m:
        continue
    else:
        print('NO')
        break

else:
    print('YES')