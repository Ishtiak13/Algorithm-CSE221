import sys

count = int(sys.stdin.readline())
for _ in range(count):
    n = int(sys.stdin.readline())
    if n%2==0:
        sys.stdout.write(f"{n} is an Even number.\n")
    else:
        sys.stdout.write(f"{n} is an Odd number.\n")
