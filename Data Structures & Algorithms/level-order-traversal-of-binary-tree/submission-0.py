

class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        

        queue = deque()
        result = []
        queue.append(root)

        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level)
        return result
