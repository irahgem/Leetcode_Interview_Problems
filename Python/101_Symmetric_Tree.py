# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

# Example 1:

# Input: root = [1,2,2,3,4,4,3]
# Output: true

# Intuition
# To check whether a tree is mirror symmetric or not, we need to compare the left and right subtrees of each node. If they are mirror images of each other, then the tree is mirror symmetric.

# Approach
# In this code, we first check if the root of the tree is None, in which case we return True because an empty tree is mirror symmetric.

# Then, we define a helper function called isMirror which takes two nodes as input and checks whether they are mirror images of each other. If both nodes are None, we return True. If one of them is None, we return False because a node cannot be a mirror image of None.

# Otherwise, we check if the values of the nodes are equal and then recursively check whether the left subtree of the first node is a mirror image of the right subtree of the second node, and whether the right subtree of the first node is a mirror image of the left subtree of the second node.

# Finally, we call the isMirror function with the left and right subtrees of the root node and return the result. If the tree is mirror symmetric, the function will return True, otherwise it will return False.



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def isMirror(a, b):
            if not a and not b:
                return True
            if not a or not b:
                return False
            
            return a.val == b.val and isMirror(a.right, b.left) and isMirror(a.left, b.right)
        
        return isMirror(root, root)