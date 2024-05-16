
'''
8703. 일차원 세계의 섬


일차원 세계의 지형은 땅과 바다 둘뿐입니다. 
이 세계의 지도는 알파벳 소문자 'g'와 'o'로 이루어진 문자열입니다. 
'g'는 땅을, 'o'는 바다를 의미합니다.

그런데 재승이 지도에 잉크를 쏟아 일부 문자를 알아볼 수 없게 되었습니다.
지도에서 땅인지 바다인지 알 수 없게 된 부분은 'x'로 표시됩니다.

일차원 세계의 지도가 주어지면 가능한 섬의 개수의 최솟값과 최댓값을 알려주는 프로그램을 작성하세요. 
섬이란 양옆이 바다인 연속한 땅입니다.


예제 입력1
oxxxo

예제 출력1
0
2

예제 입력2
oggogogo

예제 출력2
3
3

[입력값 설명]

한 개의 줄에 일차원 세계의 지도가 주어집니다. (3 ≤ 지도의 길이 ≤ 100)
지도의 첫 문자와 마지막 문자는 'o'(바다)임을 보장합니다.

[출력값 설명]

첫번째 줄에 섬의 개수의 최솟값을 출력합니다.
두번째 줄에 섬의 개수의 최댓값을 출력합니다.

'''

# -*- coding: utf-8 -*-
import sys

arr = list(sys.stdin.readline().rstrip())
visited = [0 for _ in range(len(arr))]

def func(x, v):
    temp = []
    while arr[x] == v:
        visited[x] = 1
        temp.append(x)
        x += 1
    return temp

x_indices = []
for i in range(len(arr)):
    if arr[i] == 'x' and not visited[i]:
        x_indices.append(func(i, 'x'))

# minimun
min_arr = arr.copy()
min_v = [0 for _ in range(len(min_arr))]
min_c = 0
for x_index in x_indices:
    l, r = x_index[0]-1, x_index[-1]+1
    v = 'g' if min_arr[l] == min_arr[r] == 'g' else 'o'
    for x_idx in x_index:
        min_arr[x_idx] = v
for i in range(len(min_arr)):
    if min_arr[i] == 'g' and not min_v[i]:
        min_c += 1
        while min_arr[i] == 'g':
            min_v[i] = 1
            i += 1
print(min_c)

# maximun
max_c = 0
max_v = [0 for _ in range(len(arr))]
for x_index in x_indices:
    l, r = x_index[0]-1, x_index[-1]+1
    if arr[l] == arr[r] == 'g' or arr[l] != arr[r]:
        if arr[l] != arr[r] and len(x_index) % 2 == 0:
            max_c += len(x_index) // 2
        else:
            max_c += (len(x_index) - 1) // 2
    else:
        max_c += (len(x_index) + 1) // 2
for i in range(len(arr)):
    if arr[i] == 'g' and not max_v[i]:
        max_c += 1
        while arr[i] == 'g':
            max_v[i] = 1
            i += 1
print(max_c)
