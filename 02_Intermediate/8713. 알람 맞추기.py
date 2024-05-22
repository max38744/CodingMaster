'''준하는 아침에 일어나기가 힘듭니다. 

그래서 알람을 맞춰 놓아도 바로 일어나지 못해서 알람이 여러번 울리도록 설정해 놓았습니다. 



처음 알람이 울린 다음, 두 번째 알람은 1분 후, 세 번째 알람은 두 번째 알람이 울린 다음 2분후, ..., K번째 알람은 K-1번째 알람이 울린 다음 K-1분 후에 울립니다.



준하가 알람을 맞춘 시각이 주어질 때,

N번째 알람이 울리는 시각을 출력하는 프로그램을 작성하세요.


예제 입력1

00:00
5

예제 출력1

00:10

예제 입력2

13:49
50

예제 출력2

10:14


입력값 설명

첫째 줄에 알람을 맞춘 시각이 "HH:MM"형태로 주어집니다.
둘째 줄에 N이 주어집니다. (1 ≤ N ≤ 1,000,000,000)

출력값 설명

N번째 알람이 울리는 시각을 "HH:MM"형태로 출력합니다.
HH는 00, 01, 02, ..., 23 중에 하나이며, MM은 00, 01, 02, ..., 59 중 하나입니다.'''

def alarm(time, N):
    hour, minute = map(int, time.split(':'))

    add_minute = (N - 1) * N // 2

    init_minute = hour * 60 + minute
    
    final_minutes = init_minute + add_minute

    final_hour = (final_minutes // 60) % 24
    final_minute = final_minutes % 60
    
    return f"{final_hour:02}:{final_minute:02}"

time = input().strip()
N = int(input().strip())


print(alarm(time, N))
