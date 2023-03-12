# Given the root of a binary tree, return the inorder traversal of its nodes' values.

# Example 1:


# Input: root = [1,null,2,3]
# Output: [1,3,2]

# https://www.google.com/search?q=binary+tree+inorder+traversal&rlz=1C1CHBD_enIN920IN921&sxsrf=AJOqlzVtfsjsm_0MJo5y_K9ZIrveq3WIrw:1678592987940&source=lnms&tbm=vid&sa=X&ved=2ahUKEwjg5JKWvtX9AhVrUGwGHXPFCCAQ_AUoAnoECAEQBA&biw=1707&bih=828&dpr=1.13#fpstate=ive&vld=cid:033dcd0e,vid:g_S5WuasWUE

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
        inorder(root)
        return res