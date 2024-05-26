'''
직각삼각형의 둘레가 120일 때, 세 변의 길이가 모두 양의 정수인 직각삼각형은 다음과 같이 3가지입니다.
(20, 48, 52), (24, 45, 51), (30, 40, 50)

1 이상 N 이하의 둘레 중에서, 세 변의 길이가 모두 양의 정수인 직각삼각형을 가장 많이 만들 수 있는 둘레와 그때 만들어지는 직각삼각형의 개수를 구하는 프로그램을 작성하세요.

예제 입력1
120
예제 출력1
120 3

예제 입력2
1000
예제 출력2
840 8

입력값 설명
첫째 줄에 양의 정수 N이 주어집니다. (12 ≤ N ≤ 2,400)
단, 세 변의 길이가 모두 양의 정수인 직각삼각형을 최소 1개 이상 만들 수 있는 입력만 주어집니다.

출력값 설명
첫째 줄에 정답을 출력합니다.
단, 조건을 만족하는 둘레가 여러 개인 경우 그 중에서 가장 작은 둘레를 출력합니다.
'''

def count_right_triangles_optimized(N):
    max_triangles = 0
    best_perimeter = 0
    
    for P in range(12, N + 1):
        count = 0
        # a의 최대 범위는 P/3
        for a in range(1, P // 3 + 1):
            # 전체 둘레를 아니까 b 값을 파악하는 반복문 하나를 줄일 수 있음.
            b = (P**2 - 2*P*a) / (2*(P - a))
            # 피타고라스 정리를 만족하는 경우 검사, 또한 중복을 막기 위해 b >= a
            if b.is_integer() and b >= a:
                b = int(b)
                c = P - a - b
                if c > b and a**2 + b**2 == c**2:  # 피타고라스 정리를 만족하고 c > b 조건 검사
                    count += 1
        
        if count > max_triangles:
            max_triangles = count
            best_perimeter = P

    return best_perimeter, max_triangles


N = int(input())  
best_perimeter, triangles_count = count_right_triangles_optimized(N)
print(best_perimeter, triangles_count) 
