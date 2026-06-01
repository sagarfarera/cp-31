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
n = inp()
a = inlt()
ans = float('inf')
for i in a:
    ans = min(ans, abs(i))
print(ans)
