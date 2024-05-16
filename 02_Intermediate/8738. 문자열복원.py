'''대민은 영어 소문자 알파벳으로 이루어진 문자열을 숫자로 인코딩하는 방법을 만들어냈습니다.

대민의 문자열 인코딩 방식은 아래와 같습니다.



1. 문자열의 왼쪽부터 문자열의 각 문자가 몇 번째 알파벳인지 알아낸다. 이 수를 a라고 하자.

2. a가 9 이하라면 a를 그대로 쓰고, a가 10 이상이라면 a를 쓰고 그 뒤에 0을 붙인다.



예를 들어, "park"를 인코딩하면 다음과 같이 진행됩니다.



1. p는 16번째 알파벳이다. 16을 쓴 후, 뒤에 0을 붙여서 160을 쓴다. (160)

2. a는 1번째 알파벳이다. 1을 쓴다. (1601)

3. r은 18번째 알파벳이다. 18을 쓴 후, 뒤에 0을 붙여서 180을 쓴다. (1601180)

4. k는 11번째 알파벳이다. 11을 쓴 후, 뒤에 0을 붙여서 110을 쓴다. (1601180110)



따라서, park를 인코딩한 결과는 1601180110입니다.



대민은 당신이 가지고 있던 소중한 문자열을 인코딩해버렸습니다.

당신은 이 인코딩된 문자열을 다시 원본 문자열로 바꿔야 합니다. 



어떤 문자열을 인코딩한 결과가 주어질 때, 

해당 문자열을 구하는 프로그램을 작성하세요.


예제 입력1

1601180110

예제 출력1

park

예제 입력2

2007200100

예제 출력2

tgtj


입력값 설명

원본 문자열을 인코딩한 결과가 주어집니다.
이 수는 50자리를 넘지 않습니다.

출력값 설명

원본 문자열을 출력합니다.
입력에 대해 이 원본 문자열은 무조건 유일하게 존재합니다.
반드시 소문자 알파벳으로 출력해야함에 유의하세요.'''

# -*- coding: utf-8 -*-
def make_alphabet():
    alphabet = {}
    
    for word in range(65, 91):
        if word - 64 < 10:
            alphabet[word-64] = chr(word).lower()
        else:
            alphabet[(word-64) * 10] = chr(word).lower()
    
    return alphabet

words = str(input())
alphabet = make_alphabet()
replace_word = list(alphabet.keys())[9:]

for key in replace_word:
    if str(key) in words:
        words = words.replace(str(key), alphabet[key])

for key in list(alphabet.keys()):
    words = words.replace(str(key), alphabet[key])
    
print(words)






#written by yong
'''
# -*- coding: utf-8 -*-
import sys

def encoding(a):
    
    a = str(a)
    
    answer = ''
    i = len(a)-1

    while i >= 0:
        if a[i] == '0':
            answer += chr(64+int(a[i-2:i]))
            i -= 3
        else:
            answer += chr(64+int(a[i]))
            i -= 1
    
    answer = answer[::-1].lower()
    return answer
            
a = int(sys.stdin.readline())

print(encoding(a))
'''