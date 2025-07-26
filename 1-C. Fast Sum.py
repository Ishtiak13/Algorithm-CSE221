import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    arr = [int(x) for x in input().split()]
    
    is_sorted = True
    for i in range(1, n):
        if arr[i] < arr[i - 1]:
            is_sorted = False
            break
    
    sys.stdout.write("YES\n" if is_sorted else "NO\n")
