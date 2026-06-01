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
g = 10
score_map = {
    1:1,
    2:2,
    3:3,
    4:4,
    5:5,
    6:5,
    7:4,
    8:3,
    9:2,
    10:1
}
for _ in range(t):
    ans = 0
    for i in range(1,11):
        a = score_map[i]
        s = inpstr()
        for j in range(1,11):
            if s[j-1] == 'X':
                b = score_map[j]
                ans += min(b,a)
                
    print(ans)

# Claude --> 
# import sys
# input = sys.stdin.readline

# # Precompute score grid once
# score = [[min(min(r, 9-r), min(c, 9-c)) + 1 for c in range(10)] for r in range(10)]

# t = int(input())
# for _ in range(t):
#     grid = [input().strip() for _ in range(10)]
#     print(sum(score[r][c] for r in range(10) for c in range(10) if grid[r][c] == 'X'))