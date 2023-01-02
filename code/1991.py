import sys

from sklearn import tree
sys.setrecursionlimit(10**9)

# n = int(input())
# tree_list = {chr(i): [] for i in range(65,91)}
# visit_order = []


# for i in range(n):
#     a,b,c = map(str,sys.stdin.readline().split())
#     tree_list[a] = b,c

# def Preorder(start):
#     visit_order.append(start)
#     for i in tree_list[start]:
#         if i != '.':
#             Preorder(i)

# def Inorder(start):
#     for i in range(0,2):
#         if tree_list[start][i] != '.':
#             if tree_list[start][0] == '.' and tree_list[start][1] != '.' and i == 1:
#                 visit_order.append(start)
#             Inorder(tree_list[start][i])
#             if i == 0:
#                 visit_order.append(start)
#     if tree_list[start][0] == '.' and tree_list[start][1] == '.':
#         visit_order.append(start)

# def Postorder(start):
#     for i in tree_list[start]:
#         if i != '.':
#             Postorder(i)
#     visit_order.append(start)


# Preorder('A')
# for i in visit_order:
#     print(i,end='')
# print()
# visit_order = []

# Inorder('A')
# for i in visit_order:
#     print(i,end='')
# print()
# visit_order = []

# Postorder('A')
# for i in visit_order:
#     print(i,end='')

n = int(input())

tree_list = {}

for _ in range(n):
    node, left, right = input().split()
    tree_list[node] = left, right

def Preorder(start):
    if start == '.':
        return
    print(start,end='')
    Preorder(tree_list[start][0])
    Preorder(tree_list[start][1])

def Inorder(start):
    if start == '.':
        return
    Preorder(tree_list[start][0])
    print(start,end='')
    Preorder(tree_list[start][1])

def Postorder(start):
    if start == '.':
        return
    Preorder(tree_list[start][0])
    Preorder(tree_list[start][1])
    print(start,end='')

Preorder('A')
print()
Inorder('A')
print()
Postorder('A')