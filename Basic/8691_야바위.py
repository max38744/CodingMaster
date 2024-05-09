N, K = map(int, input().split(" "))

#컵 개수만큼 생성
cup_positions = [i for i in range(N+1)]

# 컵 이동 처리
for _ in range(0,K) :

    a, b = map(int, input().split())
    cup_positions[a], cup_positions[b] = cup_positions[b], cup_positions[a]
    #print(cup_positions)

print(cup_positions.index(int(input())))
        
# 탁구공의 위치는 볼 수 있으나 기억력이 낮음

# N개의 컵 중 한 개의 컵에 탁구공

# 컵의 이동번호가 주어짐

# 마지막에 숫자 하나가 나오면 최초 위치였던 거임 ㅋㅋ
