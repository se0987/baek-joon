N = int(input())
Nlst = []
for i in range(N):
    Nlst.append((int(input())))

def my_sort(arr, N):
    for n in range(N-1):
        for m in range(n, N):
            if arr[n] > arr[m]:
                arr[n], arr[m] = arr[m], arr[n]
    return arr

print(*my_sort(Nlst, N), sep='\n')