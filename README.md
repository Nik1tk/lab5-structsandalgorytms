# Лабораторная работа 5

Тема:  Обход бинарного дерева

Выполнил Морозов Никита Дмитриевич, группа ИДБ-25-07

Базовая задача: Реализовать функции:
-   `preorder(root)`,  `inorder(root)`,  `postorder(root)`: прямой, симметричный и обратный обходы, возвращающие список значений.
-   `level_order(root)`: обход в ширину (BFS), выводящий элементы по уровням.
-   Создать несколько тестовых деревьев для проверки работы функций.

Вариативная часть: 
 -  Определить диаметр дерева


# Импорт 

`from collections import deque`

## Класс дерева
```
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
```
## Preorder - прямой обход
```
def preorder(root):
    if root is None:
        return []
    
    result = [root.val]
    result.extend(preorder(root.left))
    result.extend(preorder(root.right))
    return result

```
## Inorder - симметричный обход
```
def inorder(root):
    if root is None:
        return []
    
    result = inorder(root.left)
    result.append(root.val)
    result.extend(inorder(root.right))
    return result
```
## Postorder - обратный обход
```
def postorder(root):
    if root is None:
        return []
    
    result = postorder(root.left)
    result.extend(postorder(root.right))
    result.append(root.val)
    return result
```
## Level order - обход по уровням
```
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

```

# Diameter - диаметр дерева
Функция выводит значение диаметра данного дерева
```
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
```
## Деревья
Дерево №1
```
def create_tree1():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    return root
```
   Дерево №2
   ```
def create_tree2():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.left.left = TreeNode(4)
    return root
```

Дерево №3
```
def create_tree3():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    return root
```
