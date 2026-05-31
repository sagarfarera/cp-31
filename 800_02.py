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
def invr():
    return(map(int,input().split()))


############ ---- Solution ---- ############
t = inp()
for _ in range(t):
    n, x = invr()
    a = inlt()
    a.insert(0, 0)
    ans = -1
    for i in range(n):
        ans = max(ans, a[i+1] - a[i])
    ans = max(ans, 2 * (x - a[-1]))
    print(ans)

