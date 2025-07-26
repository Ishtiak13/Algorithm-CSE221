import sys
count = int(sys.stdin.readline())
for _ in range(count):
    a = sys.stdin.readline().strip()
    arithmetic = a.split(' ')
    first = int(arithmetic[1])
    exp = arithmetic[2]
    second = int(arithmetic[3])
    if exp=="+":
        result = first + second
    elif exp == "-":
        result = first - second
    elif exp == '*':
        result = first * second
    elif exp=='/':
        result =first / second
    else:
        result = 'expression not valid'
    sys.stdout.write(str(result) + '\n')