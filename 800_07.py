import sys
input = sys.stdin.readline

############ ---- Input Functions ---- ############
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def inpstr():
    return(input().strip())
def invr():
    return(map(int,input().split()))


############ ---- Solution ---- ############
t = inp()
for _ in range(t):
    n, m = invr()
    p = inpstr()
    target = inpstr()

    ops = 0
    while len(p) < m:
        p = p + p
        ops += 1
        if len(p) > 25 * 25:  # safety, n*m <= 25 so this is generous
            break

    if target in p:
        print(ops)
    elif target in p + p:
        print(ops + 1)
    else:
        print(-1)