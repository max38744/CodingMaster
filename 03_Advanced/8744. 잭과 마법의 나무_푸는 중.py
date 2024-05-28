'''
잭은 정오(12시 0분)에 마법의 나무 묘목을 땅에 심었습니다.
땅에 심어진 마법의 나무는 매일 자정(0시 0분)에 다음과 같이 키가 바뀝니다.

1. 어제 날이 맑았다면 키가 그제의 키만큼 커집니다. 예를 들어 첫째 날 키가 1, 둘째 날 키가 2라고 합시다. 둘째 날이 맑았다면, 셋째 날 자정 나무의 키는 (둘째 날 2) + (첫째 날 1) = 3이 됩니다. 셋째 날도 맑았다면, 넷째 날 자정 나무의 키는 (셋째 날 3) + (둘째 날 2) = 5가 됩니다. 땅에 심기 이전 나무의 키는 1입니다.
2. 어제 날이 흐렸다면 키가 1 작아집니다. 나무의 키는 1 미만으로 줄어들지 않습니다.
3. 어제 폭풍우가 쳤다면 키가 (그제의 키 + 어제의 키) ÷ 2에서 소수점을 버린 값이 됩니다. 예를 들어 첫째 날 키가 1, 둘째 날 키가 2라고 합시다. 둘째 날 폭풍우가 쳤다면, ((첫째 날 1) + (둘째 날 2)) ÷ 2는 1.5 이므로 셋째 날 자정 나무의 키는 1.5에서 소수점을 버린 1이 됩니다.

마법의 나무의 키가 정확히 N이 되면, 나무를 심은 사람은 큰 횡재를 한다고 합니다. 날씨의 종류는 맑음 · 흐림 · 폭풍우 셋 뿐이고, 날씨는 매일 자정에만 바뀝니다(바뀌지 않을수도 있습니다).
마법의 나무를 심고 적어도 며칠이 지나야 마법의 나무의 키가 정확히 N이 되는지 출력하는 프로그램을 작성하세요.

예제 입력1
3
2
3
4
예제 출력1
1
2
4

예제 입력2
2
14
7

예제 출력2
6
5


입력값 설명
첫째 줄에 테스트케이스의 수 T가 주어집니다. (1 ≤ T ≤ 6)
각 케이스마다 한 개의 줄에 목표하는 마법의 나무 키 N이 주어집니다. (2 ≤ N ≤ 500)
출력값 설명
테스트 케이스마다 각 줄에 마법의 나무를 심고 적어도 며칠이 지나야 마법의 나무의 키가 정확히 N이 되는지 출력합니다.
'''

# -*- coding: utf-8 -*-
import sys

input = sys.stdin.readline

class TreeNode:
    def __init__(self, height, day):
        self.height = height
        self.day = day
        self.children = []

def bfs_to_reach_height(N):
    from collections import deque

    root = TreeNode(1, 0)
    queue = deque([root])

    visited = {1}

    while queue:
        node = queue.popleft()
        current_height = node.height
        current_day = node.day

        if current_height == N:
            return current_day

        sunny_height = current_height + current_height
        cloudy_height = max(1, current_height - 1)
        stormy_height = (current_height + current_height) // 2

        for new_height in [sunny_height, cloudy_height, stormy_height]:
            if new_height not in visited:
                visited.add(new_height)
                new_node = TreeNode(new_height, current_day + 1)
                node.children.append(new_node)
                queue.append(new_node)

def main():
    T = int(input().strip())
    results = []

    for _ in range(T):
        N = int(input().strip())
        results.append(bfs_to_reach_height(N))

    for result in results:
        print(result)

if __name__ == "__main__":
    main()






# T = int(input())
# N = [int(input()) for _ in range(T)]

# T = 2
# N = [14, 7]

###################################################################### timeout 5 6 7 ( dynamic programming ) 

# -*- coding: utf-8 -*-
import sys
from collections import deque

input = sys.stdin.readline

def bfs_to_reach_height(N):
    if N == 1:
        return 0
    
    queue = deque([(1, 1, 0)])  # (current_height, previous_height, days_passed)
    visited = {(1, 1)}
    
    while queue:
        current_height, previous_height, days_passed = queue.popleft()
        
        if current_height == N:
            return days_passed
        
        sunny_height = current_height + previous_height
        if sunny_height not in visited:
            visited.add((sunny_height, current_height))
            queue.append((sunny_height, current_height, days_passed + 1))

        cloudy_height = max(1, current_height - 1)
        if cloudy_height not in visited:
            visited.add((cloudy_height, current_height))
            queue.append((cloudy_height, current_height, days_passed + 1))
        
        stormy_height = (previous_height + current_height) // 2
        if stormy_height not in visited:
            visited.add((stormy_height, current_height))
            queue.append((stormy_height, current_height, days_passed + 1))
    
    return -1

def main():
    T = int(input().strip())
    results = []

    for _ in range(T):
        N = int(input().strip())
        results.append(bfs_to_reach_height(N))

    for result in results:
        print(result)

if __name__ == "__main__":
    main()
