W, H = map(int, input().split())
mapp = [[0] * W for _ in range(H)]

cut_w = [0, H] # 가로로 자르기 (세로 나누기)
cut_h = [0, W]

cut = int(input())
for tc in range(cut):
    a, cut_num = map(int, input().split())

    # 자르는 부위 w,h 별 저장
    if a == 1:  # 세로로 자르기 (w 나누기)
        cut_h.append(cut_num)
    else:  # 가로로 자르기 (h 나누기)
        cut_w.append(cut_num)

cut_h = sorted(cut_h)
cut_w = sorted(cut_w)

end_w = [] # 차이값 저장하기 위해
end_h = []

for w in range(len(cut_h)-1):
    end_w.append(cut_h[w+1] - cut_h[w])

for h in range(len(cut_w)-1):
    end_h.append(cut_w[h+1] - cut_w[h])

# 차이가 가장 큰 값들끼리 곱하기
print(max(end_w) * max(end_h))