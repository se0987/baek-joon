def solution(sides):
    answer = 2
    sides.sort()
    if sum(sides[0:2]) > sides[2]:
        answer = 1
    return answer