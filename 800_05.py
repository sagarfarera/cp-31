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
    n = inp()
    arr = inlt()
    if arr[0] == 1:
        print("YES")
    else:
        print("NO")

    
