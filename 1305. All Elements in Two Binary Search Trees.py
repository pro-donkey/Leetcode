# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def inOrderTraversal(self, root:Optional[TreeNode],ans:List[int]):
        if root == None:
            return 
        
        self.inOrderTraversal(root.left,ans)
        ans.append(root.val)
        self.inOrderTraversal(root.right,ans)

    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:

        ans1 = []
        ans2 = []
        self.inOrderTraversal(root1,ans1)
        self.inOrderTraversal(root2,ans2)
        
        ans = []
        i,j = 0,0
        while i < len(ans1) and j < len(ans2):
            if ans1[i] > ans2[j]:
                ans.append(ans2[j])
                j += 1
            else:
                ans.append(ans1[i])
                i+=1 
        
        while i < len(ans1):
            ans.append(ans1[i])
            i += 1
        while j < len(ans2):
            ans.append(ans2[j])
            j += 1
        
        return ans 
        
