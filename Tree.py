class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Tree(object):
    def __init__(self, node):
        self.root = node

    def traversal(self, way='inorder'):
        def _inorder_traversal(root):
            if root is None:
                return []
            else:
                return [root.val] + _inorder_traversal(root.left) + _inorder_traversal(root.right)

        def _breadth_first(root):
            from Queue import Queue
            queue = Queue()

            bfs_order = []
            queue.push(root)
            while queue:
                node = queue.pop()
                bfs_order.append(node.val)

                if node.left:
                    queue.push(node.left)
                if node.right:
                    queue.push(node.right)
            
            return bfs_order

        flatten_tree = []
        if way == 'inorder':
            flatten_tree = _inorder_traversal(self.root)
        elif way == 'bfs':
            flatten_tree = _breadth_first(self.root)

        return flatten_tree

    def __str__(self):
        return str(self.traversal())


# root = TreeNode(3)
# root.left = TreeNode(9)
# root.right = TreeNode(20)
# root.left.right = TreeNode(1)
# root.right.left = TreeNode(15)
# root.right.right = TreeNode(7)

# tree = Tree(root)
# print(tree.traversal(way='bfs'))
# print(tree)
