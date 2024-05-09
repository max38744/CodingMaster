# -*- coding: utf-8 -*-
import sys

# 북 동 남 서
tracer = [1, 2, 3, 4]

# 현재 위치에서 얼만큼 움직였는지 파악해 모든 방향에 대해 처리한다? 

for i in range(0, int(input())) :
    N1, N2 = map(int, input().split(" "))
    
    if i == 0 :
        now = [N1, N2]
    else :
        if N1 < now[0] :
            if N2 < now[1] :
                # 북쪽으로 이동, 서쪽으로 이동
                if abs(now[0] - N1) != 0 :
                    print(1, abs( now[0] - N1))
                else :
                    print(4, abs(now[1] - N2))
            else :
                # 남쪽으로 이동, 서쪽으로 이동
                if abs(now[0] - N1) != 0 :                
                    print(3, abs( now[0] - N1))
                else :
                    print(4, abs(now[1]-N2))
        else :
            if N2 < now[1] :
                # 북쪽으로 이동, 서쪽으로 이동
                if abs(now[0] - N1) != 0 :
                    print(1, abs( now[0] - N1))
                else :
                    print(4, abs(now[1]-N2))
            else :
                # 북쪽으로 이동, 동쪽으로 이동
                if abs(now[0] - N1) != 0 :
                    print(1, abs( now[0] - N1))
                else :
                    print(2, abs(now[1]-N2))
        now = [N1, N2]
