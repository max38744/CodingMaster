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
