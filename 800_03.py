import sys
input = sys.stdin.readline

############ ---- Input Functions ---- ############
def gen_single_input(class_type: type):
    return class_type(input())
def gen_multiple_input(class_type: type):
    return map(class_type, input().split())
def gen_list_input(class_type: type):
    return list(map(class_type, input().split()))
def string_input():
    return input().strip()

############ ---- Solution ---- ############
t = gen_single_input(int)
for _ in range(t):
    n = gen_single_input(int)
    s = string_input()
    if "..." in s:
        print(2)
    else:
        ans = s.count(".")
        print(ans)



    
    