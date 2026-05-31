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
from collections import Counter

t = inp()
for _ in range(t):
    n = inp()
    a = inlt()
    c = Counter(a)
    if len(c) == 1:
        print("YES")
    elif len(c) == 2:
        vals = list(c.values())
        if abs(vals[0] - vals[1]) <= 1:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")