'''작곡가 미넷은 지금까지 수많은 곡을 작곡 해 왔습니다. 더이상 새로운 창작물을 만들어 낼 수 없는 경지에 이르렀습니다. 더이상의 곡 진행을 떠올릴 수 없게 된 미넷은, 컴퓨터를 사용해 새로 작곡할 악곡의 코드 진행을 만들기로 했습니다.



미넷은 음악을 만드는 데 있어 총 14가지의 코드만을 사용합니다. 그것들은 A, B, C, D, E, F, G의 메이저 코드들과, Am, Bm, Cm, Dm, Em, Fm, Gm의 마이너 코드들입니다. 이 14가지의 코드들을 사용해 5마디로 나누어져 있는 악보를 제각기 다른 코드들로 채우려고 합니다. 예를 들어, 5마디를 다음과 같이 채울 수 있습니다.



F | Em | Am | C | Dm



그런데, 미넷은 권위있는 작곡가이기 때문에, 자신의 곡을 작곡할 때에 지키는 조건이 있습니다. 그 조건은 다음과 같습니다.



1. 14개의 코드들은 각각 한 번을 초과하여 사용할 수 없습니다.

2. "너무 뻔한 코드의 진행"을 사용하지 않습니다.

3. 메이저 코드와 마이너 코드는 a번을 초과하여 연속되어선 안 됩니다. (1 ≤ a ≤ 5)



"너무 뻔한 코드의 진행"이란, 작곡가 미넷이 지금껏 작곡을 해 오면서 너무나 자주 써 왔던 코드 진행을 말합니다. 이 "너무 뻔한 코드의 진행"은 코드 2개의 길이를 갖습니다.



"너무 뻔한 코드의 진행"의 예시는 다음과 같습니다.



F Cm

Cm G



메모의 각 줄은 "너무 뻔한 코드의 진행" 으로 첫 번째 줄은 F 코드 뒤에 Cm 코드가 나올 수 없음을 의미하고 두 번째 줄은 Cm 코드 뒤에 G 코드가 나올 수 없음을 의미합니다.



컴퓨터는 5마디로 구성된 여러 코드 진행들을 제안할 수도 있고, 제안할 수 있는 코드 구성이 존재하지 않을 수도 있습니다. 코드 2개로 구성된 "너무 뻔한 코드의 진행"이 N개 주어졌을 때, 작곡가 미넷이 제시하는 조건들을 만족하는 코드 진행이 몇 가지인지 구하는 프로그램을 작성하세요.


예제 입력1

2 1
F Cm
Cm G

예제 출력1

16290

예제 입력2

0 5

예제 출력2

240240


입력값 설명

입력의 첫째 줄에 미넷이 메모한 "너무 뻔한 코드의 진행"들의 개수 N과 메이저나 마이너 코드가 연속해서 나올 수 없는 횟수 a가 주어집니다. (0 ≤ N ≤ 50, 1 ≤ a ≤ 5)

두번째 줄부터 N개의 줄에 걸쳐 "너무 뻔한 코드의 진행"들이 주어집니다. "너무 뻔한 코드의 진행"의 코드들은 띄어쓰기로 구분되어 주어집니다.

출력값 설명

본문의 조건들을 만족하는 코드 진행의 수를 출력합니다.

만약 조건을 만족하는 코드 진행이 존재하지 않는 경우, 조건을 만족하는 코드 진행의 수는 0이므로, 0을 출력해야 합니다.

==========================================================================================백트랙킹사용'''

def good_going(N, a, going):
    codes = ["A", "B", "C", "D", "E", "F", "G", "Am", "Bm", "Cm", "Dm", "Em", "Fm", "Gm"]
    going_set = set(tuple(_.split()) for _ in going)
    
    def major(code):
        return code in {"A", "B", "C", "D", "E", "F", "G"}
    
    def backtrack(path, used, major_count, minor_count):
        if len(path) == 5:
            return 1

        count = 0
        for code in codes:
            if code in used:
                continue

            if len(path) > 0 and (path[-1], code) in going_set:
                continue

            if major(code):
                if major_count >= a:
                    continue
                next_major_count = major_count + 1
                next_minor_count = 0
            else:
                if minor_count >= a:
                    continue
                next_major_count = 0
                next_minor_count = minor_count + 1

            used.add(code)
            path.append(code)
            count += backtrack(path, used, next_major_count, next_minor_count)
            path.pop()
            used.remove(code)
        
        return count
    
    return backtrack([], set(), 0, 0)


N, a = map(int, input().split())
going = [input().strip() for _ in range(N)]

print(good_going(N, a, going))
