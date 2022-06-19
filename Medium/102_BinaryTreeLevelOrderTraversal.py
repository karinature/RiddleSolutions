#
#   Date - 16.06.2022
#
#
# 102. Binary Tree Level Order Traversal
# Medium
#
# Given the root of a binary tree, return the level order traversal of its nodes' values.
# (i.e., from left to right, level by level).
#
#
#
# Example 1:
#
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]
#
# Example 2:
#
# Input: root = [1]
# Output: [[1]]
#
# Example 3:
#
# Input: root = []
# Output: []
#
#
#
# Constraints:
#
#     The number of nodes in the tree is in the range [0, 2000].
#     -1000 <= Node.val <= 1000
#
#


import timeit
from typing import List, Optional


# Definition for singly-linked list.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def create_tree(root: List[int]) -> 'TreeNode':
        if not root:
            return TreeNode()
        head: TreeNode = TreeNode(root.pop(0), root.pop(1), root.pop(2))
        # for num in root[3:]:

    # def __eq__(self, other: List[int]):
    #     temp = self
    #     if not other: return temp.next is None
    #     for x in other:
    #         if x == temp.val:
    #             try:
    #                 temp = temp.next
    #             except:
    #                 return False
    #         else:
    #             return False
    #     return True


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        res: List[List[int]] = []
        st: List[TreeNode] = [root]

        while st:
            temp_res = []
            temp_st = []

            for node in st:
                if node:
                    temp_st += [node.left, node.right]
                    temp_res += [node.val]

            st = temp_st
            if temp_res:
                res.append(temp_res)

        return res

def testing():
    sol = Solution()

    # root = [0, 1, 0, 3, 12]
    # sol.some_function(TreeNode.create_tree(root))
    # assert ([1, 3, 12, 0, 0] == root)
    #
    # root = [0]
    # sol.some_function(TreeNode.create_tree(root))
    # assert ([0] == root)
    #
    # root = [0, -1]
    # sol.some_function(TreeNode.create_tree(root))
    # assert ([-1, 0] == root)
    #
    # root = [0, 0]
    # sol.some_function(TreeNode.create_tree(root))
    # assert ([0, 0] == root)


if __name__ == '__main__':
    print("\n Finished in --- %.5f seconds ---" % (
        timeit.timeit(testing, number=100)))
