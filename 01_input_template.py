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
