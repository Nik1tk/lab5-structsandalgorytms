from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def preorder(root):
    if root is None:
        return []
    
    result = [root.val]
    result.extend(preorder(root.left))
    result.extend(preorder(root.right))
    return result

def inorder(root):
    if root is None:
        return []
    
    result = inorder(root.left)
    result.append(root.val)
    result.extend(inorder(root.right))
    return result

def postorder(root):
    if root is None:
        return []
    
    result = postorder(root.left)
    result.extend(postorder(root.right))
    result.append(root.val)
    return result

def level_order(root):
    if root is None:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level = []
        level_size = len(queue)
        
        for i in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(level)
    
    return result

def diameter(root):
    result = 0
    
    def height(node):
        nonlocal result
        
        if node is None:
            return 0
        
        left_h = height(node.left)
        right_h = height(node.right)
        
        result = max(result, left_h + right_h)
        
        return max(left_h, right_h) + 1
    
    height(root)
    return result

def create_tree1():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    return root

def create_tree2():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.left.left = TreeNode(4)
    return root

def create_tree3():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    return root

def print_tree(node, level=0, side="Корень"):
    if node:
        print("  " * level + f"{side}: {node.val}")
        if node.left or node.right:
            print_tree(node.left, level + 1, "Левый")
            print_tree(node.right, level + 1, "Правый")

tree1 = create_tree1()
tree2 = create_tree2()
tree3 = create_tree3()

print("=" * 50)
print("ДЕРЕВО 1:")
print_tree(tree1)
print("\nПрямой обход:", preorder(tree1))
print("Симметричный обход:", inorder(tree1))
print("Обратный обход:", postorder(tree1))
print("Обход по уровням:", level_order(tree1))
print("Диаметр дерева:", diameter(tree1))

print("\n" + "=" * 50)
print("ДЕРЕВО 2:")
print_tree(tree2)
print("\nПрямой обход:", preorder(tree2))
print("Симметричный обход:", inorder(tree2))
print("Обратный обход:", postorder(tree2))
print("Обход по уровням:", level_order(tree2))
print("Диаметр дерева:", diameter(tree2))

print("\n" + "=" * 50)
print("ДЕРЕВО 3:")
print_tree(tree3)
print("\nПрямой обход:", preorder(tree3))
print("Симметричный обход:", inorder(tree3))
print("Обратный обход:", postorder(tree3))
print("Обход по уровням:", level_order(tree3))
print("Диаметр дерева:", diameter(tree3))
