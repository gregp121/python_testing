from operator import mul
import re

# build tree logic
class TreeNode:
    def __init__(self, val): # This creates a class
        self.val = val
        self.left = None
        self.right = None

def inorderTraversal(root):
    answer = []

    inorderTraversalUtil(root, answer)
    return answer

# Build traversal logic
def inorderTraversalUtil(root, answer):
    if root is None:
        return # This cleanly handles non-existent "nodes"

    inorderTraversalUtil(root.left, answer) # Makes left the root
    inorderTraversalUtil(root.right, answer)
    if root.val == "+":
        print('Add is: ', answer)
        answer.pop(1)
        x = answer[0]
        print("x is: ", x)
        y = answer[1]
        print("x is: ", y)
        sum1 = int(x) + int(y)
        answer = [sum1]
        print("Value is: ", answer)
        return answer
    if root.val == "*":
        print('Multi is: ', answer)
        product1 = mul(int(answer[0]),  int(answer[1]))
        answer[0] = product1
        answer.pop(1)
    answer.append(root.val)
    return answer

base = "4 * 5 + 1"

# Build sepator logic
def addSub(x):
    return re.split(r"([+-])", x[::-1], maxsplit=1)
def multiDiv(x):
    return re.split(r"([*/])", x[::-1], maxsplit=1)


# Build tree insertion
# Left node is the larger splice
def treeBuilder():
    if any(operator in base for operator in ('+', '-')):
        baseSplice = addSub(base)
        # ['1 ', '+', ' 5 * 4']
        root = TreeNode(baseSplice[1])
        root.right = TreeNode(baseSplice[0])
        root.left = TreeNode(baseSplice[2])
        if len(addSub(baseSplice[2])) > 1: 
            leftSplice = addSub(baseSplice[2])
            root.left.val = leftSplice[1]
            root.left.left = TreeNode(leftSplice[0])
            root.left.right = TreeNode(leftSplice[2])
        elif len(multiDiv(baseSplice[2])) > 1:
            leftSplice = multiDiv(baseSplice[2])
            root.left.val = leftSplice[1]
            root.left.left = TreeNode(leftSplice[0])
            root.left.right = TreeNode(leftSplice[2])
        else:
            root.left = TreeNode("0")
    else:
        root = TreeNode("+")
        root.right = TreeNode("0")
    return root

treeBuilder()
inorderTraversal(treeBuilder())