import sys
input = sys.stdin.readline

n = int(input())
arr = [int(i) for i in input().split()]

c = True
while c:
    c = False
    for i in range(n - 1):
        if arr[i] % 2 == arr[i + 1] % 2 and arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            c = True

sys.stdout.write(' '.join(map(str, arr)) + '\n')
