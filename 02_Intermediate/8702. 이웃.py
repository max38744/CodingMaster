import sys
input = sys.stdin.readline

def min_weights(N, M, K, weights, edges):
    total_cost = 0
    changes = True
    # 조정이 필요 없을 때까지 반복
    while changes:
        changes = False
        for a, b in edges:
            # 정점 a와 b 간의 가중치 차이 계산
            weight_diff = abs(weights[a-1] - weights[b-1])
            # 차이가 K 이상인 경우 조정해서 비용 계산
            if weight_diff > K:
                cost = weight_diff - K
                total_cost += cost
                changes = True
                # 두 정점의 가중치를 조정
                if weights[a-1] < weights[b-1]:
                    weights[a-1] += cost
                else:
                    weights[b-1] += cost
    return total_cost

if __name__ == "__main__":
    N, M, K = map(int, input().split())
    weights = [int(input()) for _ in range(N)]
    edges = [tuple(map(int, input().split())) for _ in range(M)]

    cost = min_weights(N, M, K, weights, edges)
    print(cost)
