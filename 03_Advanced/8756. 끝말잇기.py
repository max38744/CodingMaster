'''
가영과 나영이 영단어로 끝말잇기를 하고 있습니다. 

하지만 둘다 영어를 굉장히 못하기 때문에 노트에 영단어를 같이 적어둔 채로 끝말잇기를 하고 있습니다. 



당연하게도 앞에서 이미 나왔던 단어를 말하는 것은 허용되지 않으며, 상대가 마지막으로 말했던 단어의 맨 끝 알파벳으로 시작하는 영단어를 말해야 합니다. 

만약 그런 단어를 말할 수 없다면 패배입니다. 



몇 개 되지도 않는 노트의 단어들을 보며 진지하게 플레이하는 두 사람을 보던 다영은 저렇게 써두면 승부가 항상 정해진 것이 아닌가하는 생각이 들었습니다. 



노트에 쓰여진 단어가 주어졌을 때 가영과 나영 두 사람 중 어느 사람이 이기게 될지 예측하는 프로그램을 작성하세요. 



단, 가영과 나영은 항상 최선을 다해 플레이하며 항상 가영이가 턴을 시작합니다. 


예제 입력1

5
as
soon
never
radio
oasis
예제 출력1

gayeong

예제 입력2

4
one
each
heap
poo

예제 출력2

nayeong


입력값 설명

첫 번째 줄에 노트에 쓰여진 단어의 수를 의미하는 자연수 N이 주어집니다. (3 ≤ N ≤ 15)
두 번째 줄부터 N개의 줄에 걸쳐서 알파벳 소문자로 이루어진 영단어가 하나씩 주어집니다. 단, 각 영단어의 길이는 2 이상이고 10 이하 입니다.

출력값 설명

첫 번째 줄에 가영이 이긴다면 "gayeong", 나영이 이긴다면 "nayeong"을 출력합니다.
'''
# 그래프 생성 함수
def build_graph(words):
    graph = {word: [] for word in words}
  
    # {현재 단어 : 현재 단어의 첫자로 시작하는 단어들} 형태로 그래프 생성
    for word in words:
        last_char = word[-1]
        for next_word in words:
            if word != next_word and next_word[0] == last_char:
                graph[word].append(next_word)
    return graph
  
# 승리 여부 판단 함수
def can_win(current_word, graph, visited):
    visited.add(current_word)
    for next_word in graph[current_word]:
        if next_word not in visited:
            # 상대가 패배하면 
            if not can_win(next_word, graph, visited):
                visited.remove(current_word)
                return True
    visited.remove(current_word)
    return False

# 입력 처리 부분
import sys
input = sys.stdin.readline

n = int(input().strip())
words = [input().strip() for _ in range(n)]

# 그래프 빌드
graph = build_graph(words)

for word in words:
    visited = set()
    if not can_win(word, graph, visited):
        print("gayeong")
        break
else:
    print("nayeong")
