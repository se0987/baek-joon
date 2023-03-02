K = int(input())
tree = [0 for _ in range(2 ** K)]
nums = list(map(int, input().split()))

a = 0
def make_inorder(n):
    global a
    if n <= len(tree) - 1:
        make_inorder(n * 2)
        tree[n] = nums[a]
        a += 1
        make_inorder(n * 2 + 1)


make_inorder(1)
for i in range(K):
    print(*tree[2**i : 2**(i+1)])