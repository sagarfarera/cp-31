import sys
input = sys.stdin.readline
output = sys.stdout.write

def inp():
    return int(input())
def inlt():
    return list(map(int, input().split()))

t = inp()
out = []
for _ in range(t):
    n = inp()
    b = inlt()
    
    result = [b[0]]
    for i in range(1, n):
        if b[i] < b[i-1]:
            result.append(b[i])
        result.append(b[i])
    
    out.append(str(len(result)))
    out.append(" ".join(map(str, result)))

output("\n".join(out) + "\n")