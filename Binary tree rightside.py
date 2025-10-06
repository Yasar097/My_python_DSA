from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        q = deque([root])
        res = []

        while q:
            qLen = len(q)
            rightside = None  # store the rightmost node in this level

            for i in range(qLen):
                node = q.popleft()
                if node:
                    rightside = node
                    q.append(node.left)
                    q.append(node.right)

            # after finishing one full level
            if rightside:
                res.append(rightside.val)

        return res
