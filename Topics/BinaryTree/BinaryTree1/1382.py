# # Definition for a binary tree node.
# 1st Solution
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def balanceBST(self, root: TreeNode) -> TreeNode:
#         arr = []
#         def dfs(root):
#             if root:
#                 arr.append(root.val)
#                 dfs(root.left)
#                 dfs(root.right)
#         dfs(root)
#         arr.sort()
#         fixed = len(arr) // 2
#         new_root = TreeNode(arr[len(arr) // 2])
#         def insert(new_root, value):
            
#             if new_root:
#                 if new_root.val > value and new_root.left:
#                     insert(new_root.left, value)
                    
#                 elif new_root.val < value and new_root.right:
#                     insert(new_root.right, value)

#                 elif new_root.val > value:
#                     new_root.left = TreeNode(value)
                    
#                 elif new_root.val < value:
#                     new_root.right = TreeNode(value)

#                 return new_root
#             return new_root



#         def divide(arr):
#             nonlocal fixed
#             if len(arr) >= 1 :
#                 mid = len(arr) // 2
#                 print(arr[mid])
#                 if mid != fixed:
#                     insert(new_root, arr[mid])
#                 divide(arr[:mid])
#                 divide(arr[mid+1:])
#         divide(arr)
#         print("Break")
#         return new_root
    
# def print_tree(root):
#     if root:
#         print(root.val, end = "  ")
#         print_tree(root.left)
#         print_tree(root.right)
#     print("None", end = " ")

# root = TreeNode(2)
# root.right = TreeNode(1)
# root.right.right = TreeNode(3)
# # root.right.right.right = TreeNode(4)
# # root.right.right.right.right = TreeNode(5)
# # root.right.right.right.right.right = TreeNode(6)
# # root.right.right.right.right.right.right = TreeNode(7)
# slv = Solution()
# root = slv.balanceBST(root)
# print_tree(root)


# 2nd Soltuion


# solution short and fast
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        arr = []
        def dfs(root):
            if root:
                dfs(root.left)
                arr.append(root)
                dfs(root.right)
        dfs(root)
        # print(arr)
        def new_root(l, r):
            if r >= l:
                mid = (l + r) // 2
                root = arr[mid]
                # print(root)
                root.left = new_root(l, mid -1)
                root.right = new_root(mid + 1, r)
                return root
        return new_root(0, len(arr) - 1)

root = TreeNode(2)
root.right = TreeNode(1)
root.right.right = TreeNode(3)
slv = Solution()
root = slv.balanceBST(root)
def print_tree(root):
    if root:
        print(root.val, end = "  ")
        print_tree(root.left)
        print_tree(root.right)
    print("None", end = " ")
print_tree(root)