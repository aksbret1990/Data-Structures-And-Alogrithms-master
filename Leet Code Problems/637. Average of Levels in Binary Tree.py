 #Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        
        queue = []
        child = []
        res = []
        
        child.append(root)
        
        
        #method1 BFS
#        while child:
#            while child:
#                queue.append(child.pop())
#            suma = 0 
#            count = 0
#            while queue:
#                x = queue.pop()
#                if x.left:
#                    child.append(x.left)
#                if x.right:
#                    child.append(x.right)
#                suma += x.val 
#                count += 1
#            res.append(suma/count)
#        return res
        
        
        #method2 DFS
        
        info = []
        def dfs(node, depth = 0):
            if node:
                if len(info) <= depth:
                    info.append([0, 0])
                info[depth][0] += node.val
                info[depth][1] += 1
                dfs(node.left, depth + 1)
                dfs(node.right, depth + 1)
        dfs(root)
    
        return [s/float(c) for s, c in info]
    
    
n3 = TreeNode(3)
n9 = n3.left = TreeNode(9)
n20 = n3.right = TreeNode(20)
n15 = n20.left = TreeNode(15)
n7 = n20.right = TreeNode(7)     
myobj = Solution()
res = myobj.averageOfLevels(n3)
print(res)