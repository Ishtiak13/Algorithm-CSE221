import sys
 
T = int(sys.stdin.readline())
 
for _ in range(T):
    N = int(sys.stdin.readline())
    total = N * (N + 1) // 2
    sys.stdout.write(str(total) + '\n')
