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
    n, k = invr()
    arry = inlt()
    if k == 1:
        print_yes = True
        for i in range(n-1):
            if arry[i] > arry[i+1]:
                print_yes = False
                break
        print("YES" if print_yes else "NO")
    else:
        print("YES")
