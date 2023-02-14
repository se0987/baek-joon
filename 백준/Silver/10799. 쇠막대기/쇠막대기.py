def cut(txt):
    cnt = 0
    total = 0
    # '()' -> 이전까지 '(' 수만큼 카운트, ')' -> '(' 하나 제거, 카운트 +1
    i = 0
    while i < len(txt):
        if (i + 1 < len(txt)) and (txt[i] + txt[i + 1] == '()'):
            i = i+2
            total += cnt
        elif txt[i] == '(':
            cnt += 1
            i += 1
        elif txt[i] == ')':
            cnt -= 1
            total += 1
            i += 1

    return total

txt = input()
ans = cut(txt)
print(ans)