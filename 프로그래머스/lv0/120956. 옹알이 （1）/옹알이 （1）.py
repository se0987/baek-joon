from itertools import permutations
def solution(babbling):
    answer = 0
    speak = ["aya","ye","woo","ma"]
    word = []
    
    for i in range(1, len(speak)+1): # 원소의 개수가 1 ~ 4 인 
        for j in permutations(speak, i): # speak의 순열 만들기
            word.append(''.join(j)) # 모든 경우 구해서 word에 추가

    for i in babbling: # babbling에서 
        if i in word: # 말할 수 있는 단어였다면
            answer += 1 # cnt +1

    return answer