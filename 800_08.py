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
    n, k = invr()
    a = inlt()
    c = Counter(a)
    if c.get(k, 0) > 0:
        print("YES")
    else:
        print("NO")

