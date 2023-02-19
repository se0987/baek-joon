N = int(input())
for _ in range(N):
    txt = input()
    cnt = 0


    def recursion(s, l, r):
        global cnt
        if l >= r:
            return 1
        elif s[l] != s[r]:
            return 0
        else:
            cnt += 1
            return recursion(s, l + 1, r - 1)


    def isPalindrome(s):
        global cnt
        a = recursion(s, 0, len(s) - 1)
        cnt += 1
        return a

    print(isPalindrome(txt), cnt)
